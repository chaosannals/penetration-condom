from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from .webbrowsertoolbar_ui import Ui_WebBrowserToolbar


class WebBrowserToolbar(QWidget):
    '''

    '''

    clickedBrowse = Signal(dict)

    def __init__(self, parent):
        '''

        '''

        super().__init__(parent)
        self.ui = Ui_WebBrowserToolbar()
        self.ui.setupUi(self)
        self.ui.browseEdit.setText('http://html5test.com')
        self.ui.browseButton.clicked.connect(self.onClickBrowseButton)

    def onClickBrowseButton(self):
        '''

        '''

        self.clickedBrowse.emit({
            'url': self.ui.browseEdit.text()
        })
