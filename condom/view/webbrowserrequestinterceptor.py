from loguru import logger
from PySide6.QtWebEngineCore import QWebEngineUrlRequestInterceptor, QWebEngineUrlRequestInfo

class WebBrowserRequestInterceptor(QWebEngineUrlRequestInterceptor):
    '''
    
    '''

    def __init__(self, parent=None):
        super().__init__(parent)

    def interceptRequest(self, info: QWebEngineUrlRequestInfo) -> None:
        logger.info(' type: {}, url: {}', info.requestUrl(), info.resourceType())
        