from shiboken6 import getCppPointer, wrapInstance
from typing import Optional
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QTextOption
from PySide6.QtWidgets import QProxyStyle, QStyle, QStyleOption, QStyleOptionTab, QWidget

class TabStyle(QProxyStyle):
    '''
    
    '''

    def __init__(self):
        '''
        
        '''

        super().__init__()

    def sizeFromContents(self, type: QStyle.ContentsType, option: QStyleOption, size: QSize, widget: QWidget) -> QSize:
        s =  super().sizeFromContents(type, option, size, widget)
        if type == QStyle.CT_TabBarTab:
            s.transpose()
            s.setWidth(150)
            s.setHeight(35)
        return s

    def drawControl(self, element: QStyle.ControlElement, option: QStyleOption, painter: QPainter, widget: Optional[QWidget] = ...) -> None:
        if element == QStyle.CE_TabBarTabLabel:
            all_rect = option.rect
            (cpp_pointer,) = getCppPointer(option)
            tab = wrapInstance(cpp_pointer, QStyleOptionTab)
            if option.state & QStyle.State_Selected:
                painter.save()
                painter.setPen(QColor(0xdadbdc))
                painter.setBrush(QBrush(0xffffff))
                painter.drawRect(all_rect.adjusted(0, 0, 0, 0))
                painter.restore()

                painter.save()
                qto = QTextOption()
                qto.setAlignment(Qt.AlignCenter)
                painter.drawText(all_rect, tab.text, qto)
                painter.restore()

            elif option.state & QStyle.State_MouseOver:
                painter.save()
                qto = QTextOption()
                qto.setAlignment(Qt.AlignCenter)
                painter.drawText(all_rect, tab.text, qto)
                painter.restore()
            else:
                painter.save()
                painter.setPen(QColor(0xdadbdc))
                painter.setBrush(QBrush(0xf2f2f2))
                painter.drawRect(all_rect.adjusted(0, 0, 0, 0))
                painter.restore()

                painter.save()
                qto = QTextOption()
                qto.setAlignment(Qt.AlignCenter)
                painter.drawText(all_rect, tab.text, qto)
                painter.restore()
            return

        if element == QStyle.CE_TabBarTab:
            super().drawControl(element, option, painter, widget=widget)