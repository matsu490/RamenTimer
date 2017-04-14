# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2017-04-15
#
# Copyright (C) 2017 Taishi Matsumura
#
import sys
import PySide.QtGui
import PySide.QtCore
from MainDialog import Ui_Dialog


class MainForm(PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)

    main_form = MainForm()
    main_form.show()

    sys.exit(app.exec_())
