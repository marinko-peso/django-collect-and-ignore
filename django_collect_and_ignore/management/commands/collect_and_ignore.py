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


class Command(BaseCommand):
    help = 'Perform collectstatic with ignoring unnecessary files'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        patterns = DEFAULT_PATTERNS
        if hasattr(settings, 'COLLECT_AND_IGNORE_PATTERNS'):
            patterns = settings.COLLECT_AND_IGNORE_PATTERNS

        no_input = True
        if hasattr(settings, 'COLLECT_AND_IGNORE_NO_INPUT'):
            no_input = settings.COLLECT_AND_IGNORE_NO_INPUT

        try:
            collect_args = []
            for p in patterns:
                collect_args.extend(['-i', p])
            if no_input:
                collect_args.append('--noinput')

            call_command('collectstatic', *collect_args)
        except Exception as e:
            print('collect_and_ignore FAILED with error: %s' % str(e))
