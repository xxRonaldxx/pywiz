# pywiz
**python PyQt5 wizard module used to display a sequence of pages in a dialog box to help guide a user through a step by step process.**

[![Latest PyPI version](https://img.shields.io/badge/pypi-v0.2-green.svg)](https://pypi.org/project/pywiz/)
[![License: MIT](https://img.shields.io/dub/l/vibe-d.svg)](https://opensource.org/licenses/MIT)

Initially, I used a python script containing a series of message boxes to walk through updating an excel spreadsheet done on a monthly basis.  This module enabled me to replace each of my msgbox(title,text) functions with an addPage(title, text) function, easily modifying the scripts to use the PyQt5 QWizard class.


### Usage example:

    >>>> from pywiz import pywiz

    >>>> pywiz.setWizardTitle(“Your first wizard”)

    >>>> pywiz.addPage(“wizard page 1 title”, ”wizard page 1 text”)
    >>>> pywiz.addPage(“wizard page 2 title”, ”wizard page 2 text”)
    >>>> pywiz.addPage(“wizard page 3 title”, ”wizard page 3 text”)
         . . .

    >>>> pywiz.runWizard()

### Installation:

From PyPI: Get the latest stable version of ``pywiz`` package using pip:

    pip install pywiz

From code: Download/clone the project, go to ``pywiz`` folder that contains setup.py then:
- You can use *setup* script and pip install.
    ```bash
    pip install .
    ```

- Or, you can use the *setup* script with python:
    ```bash
    python setup.py install
    ```
