import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web View Example")
        self.setGeometry(100, 100, 640, 480)

        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("http://www.facebook.com/"))  # Cambia la URL por la que desees mostrar
        self.setCentralWidget(self.web_view)

def main():
    app = QApplication(sys.argv)
    window = WebWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


