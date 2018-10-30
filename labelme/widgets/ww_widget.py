from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets


class WwWidget(QtWidgets.QSpinBox):

    def __init__(self, value=100):
        super(WwWidget, self).__init__()
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setRange(0, 600)
        self.setSuffix(' ')
        self.setValue(value)
        self.setToolTip('ww vlaue')
        self.setStatusTip(self.toolTip())
        self.setAlignment(QtCore.Qt.AlignCenter)

    def minimumSizeHint(self):
        height = super(WwWidget, self).minimumSizeHint().height()
        fm = QtGui.QFontMetrics(self.font())
        width = fm.width(str(self.maximum()))
        return QtCore.QSize(width, height)
