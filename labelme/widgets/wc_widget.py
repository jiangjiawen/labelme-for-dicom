from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets


class WcWidget(QtWidgets.QSpinBox):

    def __init__(self, value=100):
        super(WcWidget, self).__init__()
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setRange(-100, 300)
        self.setSuffix(' ')
        self.setValue(value)
        self.setToolTip('wc value')
        self.setStatusTip(self.toolTip())
        self.setAlignment(QtCore.Qt.AlignCenter)

    def minimumSizeHint(self):
        height = super(WcWidget, self).minimumSizeHint().height()
        fm = QtGui.QFontMetrics(self.font())
        width = fm.width(str(self.maximum()))
        return QtCore.QSize(width, height)
