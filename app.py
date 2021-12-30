import asset_rc
from loguru import logger
from PySide6.QtWidgets import QApplication
from condom.view.mainwindow import MainWindow

def main():
    '''
    
    '''
    
    logger.add(
        'log/condom.log',
        level='TRACE',
        # rotation='00:00',
        rotation='2000 KB',
        retention='7 days',
        encoding='utf8'
    )

    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()

if __name__ == '__main__':
    main()