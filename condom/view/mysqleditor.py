from PySide6.QtWidget import QTextEdit
from .mysqlsyntaxhighlighter import MySQLSyntaxHighlighter


class MySQLEditor(QTextEdit):
    '''

    '''

    def __init__(self, parent=None):
        '''

        '''

        super().__init__(parent)
        self.highlighter = MySQLSyntaxHighlighter(self.document())

    def format(self):
        '''

        '''
