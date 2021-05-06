import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


def callback_function(html):
    arq=open("cupom.txt", 'w')
    arq.write(str(html))
    arq.close()



def on_load_finished():
    web.page().runJavaScript("document.documentElement.outerHTML", callback_function)


app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("http://localhost"))
web.show()
#web.loadFinished.connect(on_load_finished)

sys.exit(app.exec_())