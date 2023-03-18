import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QLineEdit,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        grid = QGridLayout()
        self.setLayout(grid)
        self.result = QLineEdit("0")
        self.result.setAlignment(Qt.AlignRight)
        self.result.setFixedHeight(50)
        self.result.setFont(QFont("Arial", 20))
        self.result.setMaxLength(8)
        grid.addWidget(self.result, 0, 0, 1, 4)
        names = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "=",
            "+",
        ]
        positions = [(i, j) for i in range(1, 5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            button.setFixedSize(50, 50)
            button.setStyleSheet(
                """
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #333;
                    border-radius: 5px;
                    font-size: 20px;
                    font-weight: bold;
                    color: #333;
                }
                QPushButton:hover {
                    background-color: #333;
                    color: #f0f0f0;
                }
                """
            )
            grid.addWidget(button, *position)
            button.clicked.connect(self.buttonClicked)
        clearButton = QPushButton("C")
        clearButton.setFixedSize(50, 50)
        clearButton.setStyleSheet(
            """
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #333;
                border-radius: 5px;
                font-size: 20px;
                font-weight: bold;
                color: #333;
            }
            QPushButton:hover {
                background-color: #333;
                color: #f0f0f0;
            }
            """
        )
        grid.addWidget(clearButton, 4, 3)
        clearButton.clicked.connect(self.clearClicked)
        self.show()

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == "=":
            result = str(eval(self.result.text()))
            self.result.setText(result)
        elif key == "C":
            self.result.setText("0")
        else:
            if self.result.text() == "0":
                self.result.setText(key)
            else:
                self.result.setText(self.result.text() + key)

    def clearClicked(self):
        self.result.setText("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    calc = Calculator()
    sys.exit(app.exec_())
