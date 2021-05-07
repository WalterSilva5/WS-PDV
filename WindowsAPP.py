from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

import os
import sys


class CustomWebEnginePage(QWebEnginePage):
    """ Custom WebEnginePage to customize how we handle link navigation """
    # Store external windows.
    external_windows = []

    def acceptNavigationRequest(self, url,  _type, isMainFrame):
       
        def onLoadFinished(ok):
            if ok:
                self.w.page().runJavaScript("document.getElementById('cupom')", imprimir)
        def imprimir(html):
            print(html)
                 
        if _type == QWebEnginePage:
            self.w = QWebEngineView()
            self.w.setUrl(url)
            self.w.loadFinished.connect(onLoadFinished)
            self.w.setGeometry(100, 100, 600, 400)
            self.w.showMaximized()

            # Keep reference to external window, so it isn't cleared up.
            #self.external_windows.append(self.w)
            return False
        return super().acceptNavigationRequest(url,  _type, isMainFrame)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setPage(CustomWebEnginePage(self))
        self.browser.setUrl(QUrl("http://localhost"))
        self.setCentralWidget(self.browser)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()