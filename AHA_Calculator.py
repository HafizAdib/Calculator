from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys 
from functools import partial
import kivy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AHA - CALCULATOR")
        self.setGeometry(100, 100, 400, 500)
        self.setWindowIcon(QIcon("./ico.png"))

        
        self.CalculatorUIStyles()
        self.CalculatorUI()
        self.show()
    
    def CalculatorUIStyles(self):
        self.setStyleSheet(
        """
            QMainWindow{
                background-color: fefefe;
                border-radius: 5px;
            }

            #display {
                font-size: 34px;
                padding: 10px;
                border: 2px solid #333;
                border-radius: 5px;
            }
            QPushButton{
                font-size: 20px;
                padding: 10px;
                border: 2px solid #333;
                border-radius: 5px;
                font-weight: bold;
                color: #fff;
            }
            QPushButton:pressed{
                background-color: #111;
                color: #000;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #000;
            }
            #keys{
                border: 2px solid #333;
                border-radius: 5px;
            }
        """
        )

    def CalculatorUI(self):
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout() 
        self.mainLayout.setObjectName("calculator")   

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setObjectName("display")
        self.display.setReadOnly(True)

        self.keys = QGridLayout()
        self.keys.setObjectName("keys")
        buttons = {
                          "CE" : (0, 0), "x" : (0, 1), "/": ( 0, 3),
            "7" : (1, 0),  "8" : (1, 1), "9" : (1, 2), "*": ( 1, 3),
            "4" : (2, 0),  "5" : (2, 1), "6" : (2, 2), "-": ( 2, 3),
            "1" : (3, 0),  "2" : (3, 1), "3" : (3, 2), "+": ( 3, 3), 
            "0" : (4, 0),  ".": ( 4, 1),               "=": ( 4, 2)

        }
        
        for button, (row, col) in buttons.items():
            self.button = QPushButton(button)

            if button == "=":
                self.button.clicked.connect(self.calculate)
                self.keys.addWidget(self.button, row, col, 1, 2)  # Prend 2 colonnes
            else:            
                self.button.clicked.connect(partial(self.typeToDisplay, button))
                self.keys.addWidget(self.button, row, col)
        
        self.mainLayout.addWidget(self.display)
        self.mainLayout.addLayout(self.keys)

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)
        
    def typeToDisplay(self, button):
        if "=" in self.display.text():
                    self.display.clear()    
        elif "ERREUR"in self.display.text():
                    self.display.clear() 

        if button == "CE":
            self.display.clear()
        elif button == "x":
            if self.display.text():
                self.display.setText(f"{self.display.text()[:-1]}")
        else:
            self.display.setText(f"{self.display.text()}{button}")

    def calculate(self):
        try:    
            solution = eval(self.display.text())
            self.display.setText(f"= {solution}")  
        except(SyntaxError, NameError, ZeroDivisionError):
            self.display.setText(f"ERREUR")  
 


app = QApplication(sys.argv)
window = MainWindow()

sys.exit(app.exec())
