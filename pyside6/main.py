from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys

# # Without OOP
# app = QApplication(sys.argv)

# window = QMainWindow()
# window.setWindowTitle("Main Window App :)")
# button = QPushButton()
# button.setText("Press this button!")
# window.setCentralWidget(button)
# window.show()
# app.exec()

# With OOP
class ButtonHolder(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Main Window App :)")
    button = QPushButton("Press Me!")
    self.setCentralWidget(button)

if __name__=="__main__":
  app = QApplication(sys.argv)
  window = ButtonHolder()
  window.show()
  sys.exit(app.exec())
