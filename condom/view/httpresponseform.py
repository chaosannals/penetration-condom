from PySide6.QtWidgets import QWidget
from .httpresponseform_ui import Ui_HttpResponseForm

class HttpResponseForm(QWidget):
    '''
    
    '''

    def __init__(self, parent=None):
        '''
        
        '''

        super().__init__(parent)
        self.ui = Ui_HttpResponseForm()
        self.ui.setupUi(self)
        