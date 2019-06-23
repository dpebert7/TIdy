"""
pytest:
 - File name must have _test in it.
 - Function name must have test in it
 - Call `pytest` to execute tests
"""

from TI import TI
from defaults import DEFAULT_OUTDIR, DEFAULT_TAB

blank_TI = TI([''])
if_TI = TI(['if(1=0)'])
indent_TI = TI(['IF(1=0);', "ASCIIOutput('zz.txt', 'Hello world!');", 'ENDIF;'])
trailing_whitespace_TI = TI(['#Comment          '])
comment_TI = TI(['### Constants'])


def test_default_tab():
    assert blank_TI.tab == DEFAULT_TAB

def test_default_outdir():
    assert blank_TI.outdir == DEFAULT_OUTDIR

def test_tab_change():
    blank_TI.set_tab('xxx')
    assert blank_TI.tab == 'xxx'

def test_set_outfile():
    blank_TI.set_outfile('xxx')
    assert blank_TI.outfile == 'xxx'

def test_set_outdir():
    blank_TI.set_outfile('xxx')
    assert blank_TI.outfile == 'xxx'

def test_keyword_capitalization():
    if_TI.capitalize_keywords()
    assert if_TI.text == ['IF(1=0)']

def test_indentation():
    indent_TI.indent()
    assert indent_TI.text == ['IF(1=0);', DEFAULT_TAB + "ASCIIOutput('zz.txt', 'Hello world!');", 'ENDIF;']

def test_trailing_whitespace():
    trailing_whitespace_TI.remove_trailing_whitespace()
    assert trailing_whitespace_TI.text == ['#Comment']

def test_capitalization_context():
    comment_TI.tidy()
    assert comment_TI.text != ['### ConsTANts']