from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget
from .webbrowserpanel_ui import Ui_WebBrowserPanel

class WebBrowserPanel(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_WebBrowserPanel()
        self.ui.setupUi(self)
        self.ui.view.load(QUrl('https://baidu.com'))