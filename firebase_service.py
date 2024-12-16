import firebase_admin
from firebase_admin import credentials, firestore

# Firebase bağlantısını başlatma
cred = credentials.Certificate("butterfly-e6e77-firebase-adminsdk-shrw3-46e5f3fa7e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def register_user(username, email):
    # Yeni kullanıcıyı Firestore'a kaydetme
    users_ref = db.collection('users')
    doc = users_ref.document(username).get()
    if doc.exists:
        return False  # Kullanıcı zaten varsa kaydetme
    else:
        users_ref.document(username).set({
            'username': username,
            'email': email,
        })
        return True

def login_user(username, email):
    # Kullanıcıyı kontrol etme ve giriş yapma
    users_ref = db.collection('users').document(username)
    doc = users_ref.get()
    if doc.exists and doc.to_dict().get('email') == email:
        return True  # Giriş başarılı
    else:
        return False  # Giriş başarısız

def find_user(username, callback):
    # Kullanıcı adını arar ve sonucunu callback ile döner
    users_ref = db.collection('users').document(username)
    doc = users_ref.get()
    if doc.exists:
        callback(doc.to_dict())
    else:
        callback(None)

def send_message(sender, receiver, content):
    # Gönderici ve alıcıyı belirten mesaj gönderme işlevi
    messages_ref = db.collection('messages')
    messages_ref.add({
        'sender': sender,
        'receiver': receiver,
        'content': content,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    

def listen_to_messages(current_user, selected_user, callback):
    messages_ref = db.collection('messages').where(
        'sender', 'in', [current_user, selected_user]
    ).where(
        'receiver', 'in', [current_user, selected_user]
    ).order_by('timestamp')

    def on_snapshot(snapshot, changes, read_time):
        for doc in snapshot:  # Doğrudan snapshot üzerinde döngü yapıyoruz
            callback(doc)  # Belirli bir belge için callback fonksiyonunu çağırıyoruz
    
    return messages_ref.on_snapshot(on_snapshot)


