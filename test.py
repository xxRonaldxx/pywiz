from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout,
                            QWizard,QWizardPage)
from unittest import TestCase, main
import pywiz

class pywizTest(TestCase):

    def setUp(self):
        pass

    def test_setWizardTitle(self):
        pywiz.setWizardTitle('test_text')
        self.assertEqual(pywiz.wizard.windowTitle(),'test_text')

    def test_addPage(self):
        pywiz.addPage('title_text', 'message_text')
        pywiz.wizard.show()
        self.assertEqual(pywiz.wizard.currentPage().title(),'title_text')
        self.assertEqual(pywiz.wizard.findChildren(QLabel)[0].text(),'message_text')


if __name__ == '__main__':
    main()
