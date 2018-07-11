from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


DEFAULT_PATTERNS = [
    '__tests__',
    'tests',
    '*.test.js',
    '*.scss',
    '*.less',
    'config.rb'
]
patterns = DEFAULT_PATTERNS
# Use user defined patterns if they exist.
if hasattr(settings, 'COLLECT_AND_IGNORE_PATTERNS'):
    patterns = settings.COLLECT_AND_IGNORE_PATTERNS

is_interactive = False
# Use user defined interactive if it exists.
if hasattr(settings, 'COLLECT_AND_IGNORE_INTERACTIVE'):
    is_interactive = settings.COLLECT_AND_IGNORE_INTERACTIVE


class Command(BaseCommand):
    help = 'Perform collectstatic with ignoring unnecessary files'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        try:
            collect_args = []
            for p in patterns:
                collect_args.extend(['-i', p])
            call_command('collectstatic', *collect_args, interactive=is_interactive)
        except Exception as e:
            print('collect_and_ignore FAILED with error: %s' % str(e))
