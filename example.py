"""
    Basic example to demonstrate the usage of the pywiz module
"""
#   1) import pywiz
#   2) add a page for each step of the wizard
#   3) tell pywiz it's time to run the wizard
#
# To run this example
# $> python example.py

import pywiz

pywiz.setWizardTitle("Your First Wizard")
pywiz.addPage("Test wizard",'First attempt at a wizard!  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR '+
                            'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, '+
                            'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE '+
                            'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER '+
                            'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'+
                            'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE '+
                            'SOFTWARE.')

pywiz.addPage("Next step",'How to make <a href="https://stackoverflow.com/questions/18291597/how-to-make-links">'+
                          'links</a> in a <font color="maroon">QWizards</font> subtitle clickable.')
pywiz.runWizard()
