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

### Known Issues/Improvements

* [ ] Add hanging indentation for long `ExecuteProcess` statements.

* [ ] Include and document options for removing extra whitespace, shortening comment headers, etc.

* [ ] Include formatting for rule files

* [ ] Expanded testing


### Fixed Issues

* [x] Operators within quotes should not be spaced, E.g. `path = '\\main-directory\test.txt';`

* [x] Allow passing of raw `.pro` files. Note: This is working, but is generally dangerous and should only be with proper testing.

* [x] `\n` must not be interpreted as new line, especially when passing string rather than file path. E.g. `nResult = nNumerator\nDivisor;` should not split into two lines.

* [x] Correct capitalization at start of word. E.g. `stringtonumber (pEndYear)` should not become `STRingToNumber (pEndYear)`

* [x] Single line if statments, E.g. `IF(nCondition = 1, ProcessBreak, 0);` should handle indentation correctly



