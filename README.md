# django-collect-and-ignore
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
