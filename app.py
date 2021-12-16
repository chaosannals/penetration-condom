from PySide6.QtWidgets import QApplication
from condom.view.mainwindow import MainWindow

def main():
    '''
    
    '''

    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()

if __name__ == '__main__':
    main()