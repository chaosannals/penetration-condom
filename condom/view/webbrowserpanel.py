from loguru import logger
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PySide6.QtWidgets import QWidget
from .webbrowserpanel_ui import Ui_WebBrowserPanel
from .webbrowserrequestinterceptor import WebBrowserRequestInterceptor

class WebBrowserPanel(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_WebBrowserPanel()
        self.ui.setupUi(self)
        self.ui.toolbar.clickedBrowse.connect(self.onClickBrowse)
        interceptor = WebBrowserRequestInterceptor(self.ui.view)
        QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)

    def toUrl(self, url):
        '''
        '''

        logger.info('to url: {}', url)
        # interceptor = WebBrowserRequestInterceptor(self.ui.view)
        # profile = QWebEngineProfile(self.ui.view)
        # profile.setUrlRequestInterceptor(interceptor)
        # page = QWebEnginePage(profile, self.ui.view)
        page = QWebEnginePage(self.ui.view)
        self.ui.view.setPage(page)
        page.setUrl(QUrl(url)) # 必须在 setPage 之后调用
        # page.load(QUrl(url)) # 必须在 setPage 之后调用
        self.ui.view.show()

    def onClickBrowse(self, data):
        '''
        '''

        self.toUrl(data['url'])