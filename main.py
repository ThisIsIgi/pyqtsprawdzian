import sys
import random
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog


class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton.clicked.connect(self.form)

    def form(self):

        lekarz = ''
        dni: int = 5
        amount: int = 0
        dni = random.randrange(0, 1000)

        if self.ui.wizyta.isChecked():
            amount += 200
            dni = random.randrange(0, 14)
            return amount, dni

        if self.ui.pediatra.isChecked():
            amount += 100
            lekarz = 'pediatra'
            return amount, lekarz
        elif self.ui.dermatolog.isChecked():
            amount += 150
            lekarz = 'dermatolog'

            return amount, lekarz
        elif self.ui.internista.isChecked():
            amount += 200
            lekarz = 'internista'
            return amount, lekarz

        if self.ui.pushButton.clicked:
            text = f'Pomyslnie zerzerwoano wiytzte u lekarza {lekarz} termin wiyty wypada za {dni} dni cena to {amount}'
            self.ui.resoult.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())
