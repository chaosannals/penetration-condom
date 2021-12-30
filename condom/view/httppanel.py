from PySide6.QtWidgets import QWidget
from .httppanel_ui import Ui_HttpPanel

class HttpPanel(QWidget):
    '''
    
    '''

    def __init__(self, parent=None):
        '''
        
        '''

        super().__init__(parent)
        self.ui = Ui_HttpPanel()
        self.ui.setupUi(self)
        