## TIdy
*An easy python formatter TM1 TurboIntegrator processes*

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dpebert7/TIdy/master?filepath=Main.ipynb)

### Features

- Keyword Highlighting

- Indentation

- Deploy Jupyter Notebook quickly using [Binder](https://ovh.mybinder.org/): [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dpebert7/TIdy/master?filepath=Main.ipynb)

- Automatically copy results to clipboard using pyperclip (Available only when running locally)


### Example
```python
from TI import TI
ti = TI(text = "")
ti.set_tab("\t")

string = """
if (1=0) ;
ASCIIOUTPUT('zz.txt', 'Hello world!');
endif;
"""

ti.text = string.split('\n')
ti.tidy()
ti.print_output()
```

Output:
```
IF (1 = 0);
	ASCIIOutput('zz.txt', 'Hello world!');
ENDIF;
```

### Known Issues/Improvement Plans

* [ ] Need to include and document options for removing extra whitespace, shortening comment headers, etc.

* [ ] Further testing required when processing raw .rux files.

* [ ] Add formatting for rules files


### Fixed Issues

* [x] \n interpreted as new line, especially when passing string rather than file path. E.g. `nResult = nNumerator\nDivisor;` will split into separate lines.

* [x] Capitalization of non-keywords still isn't sorted when alternate keyword matches start of word. E.g. `stringtonumber (pEndYear)` incorrectly changes to `STRingToNumber (pEndYear)`
