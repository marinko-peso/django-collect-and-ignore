from django.core.management.base import BaseCommand
from django.core.management import call_command


COLLECT_AND_IGNORE = [

]


class Command(BaseCommand):
    help = 'Perform collectstatic with ignoring unnecessary files'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        try:
            collect_args = ['-i', '__tests__', '-i', '*.scss']
            call_command('collectstatic', *collect_args, interactive=False)
        except Exception as e:
            print('collect_and_ignore FAILED with error: %s' % str(e))
