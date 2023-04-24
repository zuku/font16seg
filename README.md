# font16seg

font16seg is a 16-segment font implementation for M5Stack devices using MicroPython.

This is not a font file.
This module draws a letter as 16-segmented figures.


# Usage

You can download the font16seg archive package file from the [release page](https://github.com/zuku/font16seg/releases/latest).
The file can be found in the _Assets_ section. (file name format is `font16seg-vN.N.N.zip`)

Unarchive the file, you will find two types of files in it.

* `font16seg.mpy`
    * `.mpy` is a precompiled binary container file format.
    * This file is smaller, faster and more efficient than `font16seg.py`. However, it is not editable and has version restrictions.
    * See [MicroPython .mpy files](https://docs.micropython.org/en/latest/reference/mpyfiles.html)
* `font16seg.py`
    * MicroPython source code file.

Copy `font16seg.mpy` (or `font16seg.py`) to the directory listed in `sys.path`.

Then run the following code on your M5Stack device.

```python
import font16seg

font16seg.text(10, 10, "FONT16SEG")
```

# Supported versions

* M5Stack UIFlow (Micropython-1.12) official firmware.

Currently, this module has been tested on M5StickC Plus (UIFlow_StickC_Plus v1.11.5) only.
It may work on other models and versions.

# Defined letters

# Functions

# Develop

## Tests
```
$ pipenv run test
```

## Build
```
$ pipenv run build
```

## Package
```
$ pipenv run package
```

# License

This module is released under the MIT license.
