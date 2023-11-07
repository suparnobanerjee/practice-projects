from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Button Holder App")
    self.button = QPushButton("Press me!")
    self.button.clicked.connect(self.clicked_button)  
    self.setCentralWidget(self.button)

  def clicked_button(self):
    print("Button CLICKED!")
    
  
