from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from .mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    '''
    
    '''

    def __init__(self):
        '''
        
        '''

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.browser = QWebEngineView(self)
        self.setCentralWidget(self.browser)
        self.browser.load(QUrl('https://baidu.com'))
        self.show()


