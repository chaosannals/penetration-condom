from PySide6.QtWidgets import QWidget
from .webbrowsertoolbar_ui import Ui_WebBrowserToolbar

class WebBrowserToolbar(QWidget):
    '''
    
    '''

    def __init__(self, parent):
        '''
        
        '''

        super().__init__(parent)
        self.ui = Ui_WebBrowserToolbar()
        self.ui.setupUi(self)