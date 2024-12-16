import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from firebase_service import register_user, login_user, send_message, listen_to_messages, find_user
from screen import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Butterfly Chat")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._current_user = None
        self.selected_user = None
        self.listener = None
        self.last_sender = None  # Son mesajı gönderen kullanıcıyı saklamak için değişken

        # Giriş ekranındaki bileşenler
        self.ui.pushButton.clicked.connect(self.login)  # "Giriş Yap" butonu
        self.ui.pushButton_2.clicked.connect(self.register)  # "Kaydol" butonu

        # Sohbet ekranındaki bileşenler
        self.ui.pushButton_3.clicked.connect(self.search_user)  # Kullanıcı arama butonu
        self.ui.pushButton_4.clicked.connect(self.send_message)  # Mesaj gönderme butonu

        # Login ekranına geçiş
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def register(self):
        username = self.ui.lineEdit_2.text()  # Kullanıcı adı alanı
        email = self.ui.lineEdit_5.text()  # Email alanı
        if username and email:
            success = register_user(username, email)
            if success:
                self.ui.listWidget.addItem("Kayıt başarılı! Giriş yapabilirsiniz.")
            else:
                self.ui.listWidget.addItem("Bu kullanıcı adı zaten alınmış.")
        else:
            self.ui.listWidget.addItem("Lütfen kullanıcı adı ve email girin.")

    def login(self):
        username = self.ui.lineEdit_2.text()  # Kullanıcı adı alanı
        email = self.ui.lineEdit_5.text()  # Email alanı
        if username and email:
            success = login_user(username, email)
            if success:
                self.set_current_user(username)
                self.switch_to_chat()
            else:
                self.ui.listWidget.addItem("Giriş başarısız. Kullanıcı adı veya email hatalı.")
        else:
            self.ui.listWidget.addItem("Lütfen kullanıcı adı ve email girin.")

    def set_current_user(self, username):
        self._current_user = username

    def get_current_user(self):
        return self._current_user

    def switch_to_chat(self):
        self.ui.stackedWidget.setCurrentIndex(1)  # Sohbet ekranına geçiş

    def search_user(self):
        username = self.ui.lineEdit_3.text()
        if username:
            find_user(username, self.user_found)

    def user_found(self, user):
        if user:
            self.selected_user = user['username']
            self.ui.listWidget.addItem(f"Mesaj atmak için {self.selected_user} seçildi.")

            # Eski dinleyiciyi iptal et
            if self.listener:
                self.listener.unsubscribe()

            # Yeni dinleyiciyi başlat
            self.listener = listen_to_messages(
                self.get_current_user(),
                self.selected_user,
                self.on_message_received
            )
        else:
            self.ui.listWidget.addItem("Kullanıcı bulunamadı.")

    def send_message(self):
        content = self.ui.lineEdit_4.text()
        current_user = self.get_current_user()  # Mevcut kullanıcıyı alıyoruz
        
        if self.selected_user and content:
            if current_user:
                # Mesajı gönderme işlemi
                send_message(current_user, self.selected_user, content)
                # Sadece yeni gönderilen mesajı eklemek için
                self.ui.listWidget.addItem(f"{current_user} (Siz): {content}")
                
                self.ui.lineEdit_4.clear()
            else:
                # Kullanıcı bilgisi yoksa uyarı
                self.ui.listWidget.addItem("Kullanıcı bilgisi alınamıyor.")
        elif not self.selected_user:
            self.ui.listWidget.addItem("Önce bir kullanıcı seçin.")
        elif not content:
            self.ui.listWidget.addItem("Mesaj içeriği boş olamaz.")

    def on_message_received(self, doc):
        if doc.exists:  # `doc` bir `DocumentSnapshot` nesnesiyse ve varsa
            message = doc.to_dict()
            sender = message.get('sender', 'Bilinmeyen')
            content = message.get('content', '')

            # Tüm gelen mesajları ekle
            self.ui.listWidget.addItem(f"{sender}: {content}")

# PyQt uygulamasını başlatma
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
