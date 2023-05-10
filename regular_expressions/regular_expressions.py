"""Module with logic and algorithm for regular expressions with same name module"""
import re


class RegularExpressionMatcher:
    """Class to work basically with re module"""
    def __init__(self):
        self.result = None

    def compare_patterns(self, expression, string):
        """Compares the regular expression pattern against the given string.

        Args:
            expression (str): The regular expression pattern to compare.
            string (str): The string to search for a match.

        Returns:
            bool: True if a match is found, False otherwise.
        """
        self.result = bool(re.search(expression, string))
        return self.result

    @staticmethod
    def create_file(filename):
        """Creates an empty file with the given filename."""
        with open(filename, 'w', encoding='utf-8'):
            pass

    @staticmethod
    def save_file(filename, content):
        """Saves the content to a file"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

    def check_expression_file(self, expression, filename1, filename2):
        """Checks if the regular expression matches the content of the given files.

        Args:
            expression (str): The regular expression to match.
            filename1 (str): The name of the first file.
            filename2 (str): The name of the second file.

        Returns:
            bool: True if a match is found in either file, False otherwise.
        """
        with open(filename1, 'r', encoding='utf-8') \
                as file1, open(filename2, 'r', encoding='utf-8') as file2:
            content1 = file1.read()
            content2 = file2.read()

        self.result = bool(re.search(expression, content1)) or bool(re.search(expression, content2))
        return self.result

    @staticmethod
    def check_simple_file(filename1, filename2):
        """Checks if the content of the given files is the same."""
        with open(filename1, 'r', encoding='utf-8') \
                as file1, open(filename2, 'r', encoding='utf-8') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

        return lines1 == lines2
