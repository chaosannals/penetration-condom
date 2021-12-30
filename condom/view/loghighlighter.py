from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat

class LogHighlighter(QSyntaxHighlighter):
    '''
    
    '''

    def __init__(self, parent):
        '''
        
        '''

        super().__init__(parent)
        self.fmt_date = QTextCharFormat()
        self.fmt_date.setFontWeight(QFont.Bold)
        self.fmt_date.setForeground(Qt.blue)
        self.rep_date = QRegularExpression('\\[\\d{4}-[01]\\d-[0-3][0-9]\s+\\d{2}:\\d{2}:\\d{2}\\]')


    def highlightBlock(self, text: str) -> None:
        '''
        '''

        rep_date_iter =self.rep_date.globalMatch(text)
        while rep_date_iter.hasNext():
            m = rep_date_iter.next()
            self.setFormat(m.capturedStart(), m.capturedLength(), self.fmt_date)
