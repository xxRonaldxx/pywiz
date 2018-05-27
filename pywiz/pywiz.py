#############################################################################
##
## pywiz is a python PyQt5 wizard module used to display a sequence of pages
## in a dialog box to help guide a user through a step by step process.
##
## Initially, I was using a series of simple message boxes to walk me through
## updating an excel spreadsheet done on a monthly basis.
##
## This module enabled me to replace each of my msgbox(title,text) functions
## with an addPage(title, text) function, making it easy to change my scripts
## to use the PyQt5 QWizard class.
##
##    Usage example:
##    >>>> Import pywiz
##
##    >>>> pywiz.setWizardTitle(“Your first wizard”)
##
##    >>>> pywiz.addPage(“wizard page 1 title”, ”wizard page 1 text”)
##    >>>> pywiz.addPage(“wizard page 2 title”, ”wizard page 2 text”)
##    >>>> pywiz.addPage(“wizard page 3 title”, ”wizard page 3 text”)
##         . . .
##
##    >>>> pywiz.runWizard()
##


from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout,
                            QWizard,QWizardPage)
from PyQt5.QtGui import QFont


def addPage(title,text):
    page = QWizardPage()
    page.setTitle(title)
    label = QLabel(text)
    label.setWordWrap(True)
    label.setOpenExternalLinks(True)
    #label.setFont(QtGui.QFont('SansSerif', 12,QtGui.QFont.Bold))
    label.setFont(QFont('SansSerif', 10))
    wizard.setSubTitleFormat(0)
    layout = QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)
    wizard.addPage(page)


def setWizardTitle(name):
    wizard.setWindowTitle(name)


def runWizard():
    #wizard.move(2100,200)  ## If you have two monitors
    #wizard.resize(360,240) ## Smaller Wizard box
    wizard.show()
    sys.exit(app.exec_())


if __name__ == 'pywiz':
    import sys
    app = QApplication(sys.argv)
    wizard = QWizard()
    #wizard.setWindowTitle('Please use "setWindowTitle()" to give this wizard a title.')


if __name__ == '__main__':
    print("Useage: import pywiz\n\tpywiz.createPage(title,text)"+
    "\n\tpywiz.setWizardTitle(title)\n\tpywiz.runWizard()")

##  This code is a modified version of the following:
## https://github.com/baoboa/pyqt5/blob/master/examples/dialogs/trivialwizard.py
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################
