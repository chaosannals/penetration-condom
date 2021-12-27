from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from .mainwindow_ui import Ui_MainWindow
from .tabstyle import TabStyle

class MainWindow(QMainWindow):
    '''
    
    '''

    def __init__(self):
        '''
        
        '''

        super().__init__()
        self.setWindowIcon(QIcon(':/app.ico'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabbar.tabBar().setStyle(TabStyle())
        self.show()


