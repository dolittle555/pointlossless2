import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class Point_of_lossless(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.TFCLabel = QLabel('Постоянные расходы в месяц TFC, руб:')
        self.TFCEdit = QLineEdit()
        self.AVCLabel = QLabel('Переменные расходы на единицу товара AVC, руб:')
        self.AVCEdit = QLineEdit()
        self.PriceLabel = QLabel('Стоимость единицы товара P, руб:')
        self.PriceEdit = QLineEdit()


        self.resultLabel = QLabel(' ')
        self.calcButton = QPushButton('Рассчитать')
        self.calcButton.clicked.connect(self.calculatePOL)

        vbox = QVBoxLayout()
        vbox.addWidget(self.TFCLabel)
        vbox.addWidget(self.TFCEdit)
        vbox.addWidget(self.AVCLabel)
        vbox.addWidget(self.AVCEdit)
        vbox.addWidget(self.PriceLabel)
        vbox.addWidget(self.PriceEdit)


        vbox.addWidget(self.resultLabel)
        vbox.addWidget(self.calcButton)

        self.setLayout(vbox)
        self.setWindowTitle('Расчет точки безубыточности')
        self.show()

    def calculatePOL(self):
        TFC = float(self.TFCEdit.text())
        AVC = float(self.AVCEdit.text())
        Price = float(self.PriceEdit.text())

        POL = int(TFC / (Price - AVC))
        self.resultLabel.setText(f'Точка безубыточности: {POL}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Point_of_lossless()
    sys.exit(app.exec_())