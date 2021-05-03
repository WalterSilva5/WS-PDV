import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://localhost"))
web.setWindowTitle("WALTERSILVA5 PDV")
web.setMinimumSize(1270, 720)
web.setMaximumSize(1270, 720)
web.show()

sys.exit(app.exec_())