from PySide6.QtWidgets import QApplication
import sys
from button_holder import ButtonHolder

def main():
  app = QApplication(sys.argv)
  window = ButtonHolder()
  window.show()
  return app.exec()

if __name__=="__main__":
  sys.exit(main())
