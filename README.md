# django-collect-and-ignore
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![license](https://img.shields.io/github/license/marinko-peso/django-collect-and-ignore.svg)](https://github.com/marinko-peso/django-collect-and-ignore/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/django-collect-and-ignore.svg)](https://pypi.org/project/django-collect-and-ignore/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-collect-and-ignore.svg)](https://pypi.org/project/django-collect-and-ignore/)
[![Last Commit](https://img.shields.io/github/last-commit/marinko-peso/django-collect-and-ignore.svg?maxAge=3600)](https://github.com/marinko-peso/django-collect-and-ignore/commits/master)

Custom collectstatic for django with ignoring commonly copied unnecessary files


## Installation

Available via PyPi, supports Python 2.x and 3.x.
```sh
pip install django-collect-and-ignore
```


## Usage

```sh
./manage.py collect_and_ignore --additional_options
```

Can be tweaked from settings:
- COLLECT_AND_IGNORE_PATTERNS [patters to ignore, needs to be a list of strings]
- COLLECT_AND_IGNORE_NO_INPUT [wheter to ask for input, boolean, default is False]

```python
DEFAULT_PATTERNS = [
    '__tests__',
    'tests',
    '*.test.js',
    '*.scss',
    '*.less',
    'config.rb'
]
```


## License

MIT.
