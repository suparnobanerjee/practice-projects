from PySide6.QtWidgets import QApplication
import sys
from button_holder import ButtonHolder

if __name__=="__main__":
  app = QApplication(sys.argv)
  window = ButtonHolder()
  window.show()
  sys.exit(app.exec())
