from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
import sys
from view import Ui_MainWindow
import random
import os
import ctypes

class App(QMainWindow):

    START_SPEED = 50 # ms
    MIN_STEPS = 20
    PARTICIPANTS_FILENAME = "participants.txt"

    def resource_path(self, relative_path):
        """ PyInstaller ile oluşturulan exe için dosya yolunu bulur. """
        try:
            # PyInstaller temp klasörü yaratır ve yolu _MEIPASS içine atar
            base_path = sys._MEIPASS
        except Exception:
            # Normal çalışıyorsa mevcut klasörü alır
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        myappid = 'mycompany.giveaway.program.v1' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon_path = self.resource_path("app_icon.ico")

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            
            print(f"İkon bulunamadı: {icon_path}")

        self.ui.btnAddParticipant.clicked.connect(self.add_participant) 
        self.ui.btnStartDraw.clicked.connect(self.start_draw)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_tick)
        self.counter = 0
        self.current_speed = 0

        self.get_old_participants()

        

    def get_old_participants(self):
        if os.path.isfile(self.PARTICIPANTS_FILENAME):
            names = []
            try:
                with open(self.PARTICIPANTS_FILENAME, "r", encoding="utf-8") as file:
                    names = file.readlines()

                for name in names:
                    cleaned_name = name.strip()
                    if cleaned_name:
                        self.ui.listParticipants.addItem(cleaned_name)
            except Exception as e:
                self.show_msg("Hata", f"Dosya okunurken hata oluştu: {e}", QMessageBox.Icon.Warning)
    
    def add_to_file(self, name):
        try:
            with open(self.PARTICIPANTS_FILENAME, "a", encoding="utf-8") as file:
                    file.write(name + "\n")
        except Exception as e:
            print(f"Kayıt hatası: {e}")

    def add_participant(self):
        name_input = self.ui.txtName
        name = name_input.text().strip()
        
        if name:
            self.ui.listParticipants.addItem(name)
            self.ui.txtName.clear()

            self.add_to_file(name)
        else:
            self.show_msg(title="Yanlış Kullanıcı Girdisi", message="Lütfen geçerli bir katılımcı ismi giriniz.", icon=QMessageBox.Icon.Critical)
    
    def start_draw(self):
        lst = self.ui.listParticipants
        count = lst.count()
        if count <= 1:
            self.show_msg("Yetersiz Katılımcı", "Lütfen en az iki katılımcı ekleyin.", QMessageBox.Icon.Critical)
            return

        self.counter = 0
        self.current_speed = self.START_SPEED

        self.timer.start(self.current_speed) 
        self.ui.lblWinner.setText("Çekiliş yapılıyor...")


    def on_timer_tick(self):
        lst = self.ui.listParticipants
        count = lst.count()
        
        random_index = random.randrange(count)
        lst.setCurrentRow(random_index)

        self.counter += 1

        self.current_speed += 20
        self.timer.setInterval(self.current_speed)
        
        if self.counter > self.MIN_STEPS and self.current_speed >= 500:
            self.timer.stop()
            
            winner_name = lst.item(random_index).text()
            self.ui.lblWinner.setText(f"Kazanan: {winner_name}!")

            if os.path.isfile(self.PARTICIPANTS_FILENAME):
                os.remove(self.PARTICIPANTS_FILENAME)

    def show_msg(self, title, message, icon: QMessageBox.Icon):
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

        return msgBox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())