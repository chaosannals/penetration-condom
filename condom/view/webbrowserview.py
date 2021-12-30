from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView

class WebBrowserView(QWebEngineView):
    '''
    
    '''

    def __init__(self, parent=None):
        '''
        '''

        super().__init__(parent)
        # page = QWebEnginePage(self)
        # page.setUrl(QUrl('http://html5test.com'))