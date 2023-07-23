from PyQt5 import QtWidgets

import sys

def transfer():
    global b
    b = Src.text()
    Form.close()

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QMainWindow()

Form.setWindowTitle('Sun')
Form.setGeometry(300, 250, 200, 190)

Sen = QtWidgets.QLabel(Form)
Sen.setGeometry(20, 20, 71, 20)
Sen.setObjectName("Sen")

Btn = QtWidgets.QPushButton(Form)
Btn.setGeometry(60, 90, 75, 25)
Btn.setObjectName("Btn")
Btn.clicked.connect(transfer)

Src = QtWidgets.QLineEdit(Form)
Src.setGeometry(40, 60, 113, 25)
Src.setText("")
Src.setObjectName("Src")

Form.setWindowTitle("Sun")
Btn.setText("Пошук")
Sen.setText("Sunnyland.ua")
Src.setPlaceholderText("Введіть назву міста:")

Form.show()
app.exec_()