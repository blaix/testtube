"""Renderer that outputs formatted messaging for end users."""
import sys

from termcolor import colored

from testtube.conf import Settings

# For python3 support, we must use print as a function rather than a statement


class Renderer(object):

    """Utility that outputs formatted messages."""

    def failure(self, message=''):
        """Print the passed message in red."""
        print(colored(message, 'red'))

    def notice(self, message=''):
        """Print the passed message."""
        print(message)

    def success(self, message=''):
        """Print the passed message in green."""
        print(colored(message, 'green'))

    def divider(self):
        """Print a divider."""
        print('=' * 71)

    def report(self, results):
        """Print a test report."""
        self.notice("Test Report\n")

        for count, group in enumerate(results, 1):
            results = (self._format_test(test, res) for test, res in group)
            results = (', ').join(results)
            self.notice("Test group %s:\t%s" % (count, results))

        self.divider()

    def audible_alert(self, count):
        """Beep the number of times specified."""
        sys.stdout.write('\a' * count)

    def _format_test(self, test, result):
        color = 'green' if result else 'red'
        files = ''

        if not test.all_files:
            files = ' (%s)' % Settings.short_path(test.changed)

        return colored('%s%s' % (test.name, files), color)
