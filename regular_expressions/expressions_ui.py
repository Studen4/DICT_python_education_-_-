"""Visual of regular expression checker"""
from regular_expressions import RegularExpressionMatcher


class RegularExpressionMatcherUI:
    """Class with methods which works basically with prints"""
    def __init__(self):
        self.matcher = RegularExpressionMatcher()

    def process_input(self, input_string):
        """Function to check correct of raw input"""
        if '|' not in input_string:
            print("Invalid input. Please use '|' as a delimiter between two expressions.")
            return
        expression1, expression2 = input_string.split('|')
        result = self.matcher.compare_patterns(expression1, expression2)
        print(f"Result: {result}")

    def edit_file(self, filename):
        """Editor to write text in files or paste it"""
        print(f"Edit the content of {filename}. Enter '!quit' to finish editing.")
        content = ''
        while True:
            line = input()
            if line == '!quit':
                break
            content += line + '\n'
        self.matcher.save_file(filename, content)
        print(f"Editing of {filename} completed.")

    def file_check(self, variant):
        """Visual part function which show acts of creating files to user"""
        expression = '.*'
        filename1 = input("Enter filename 1: ")
        filename2 = input("Enter filename 2: ")
        if variant == 1:
            expression = input("Enter your expression: ")
        self.matcher.create_file(filename1)
        self.matcher.create_file(filename2)
        print(f"Created {filename1} and {filename2}")
        input(f"Please edit the content of {filename1} and press Enter to continue...")
        self.edit_file(filename1)
        input(f"Please edit the content of {filename2} and press Enter to continue...")
        self.edit_file(filename2)
        match variant:
            case 1:
                result = self.matcher.check_expression_file(expression, filename1, filename2)
                print(f"Result: {result}")
            case 2:
                result = self.matcher.check_simple_file(filename1, filename2)
                print(f"Result: {result}")
        self.start()

    def start(self):
        """Main function which starts program"""
        mode = input("Select mode: (1) Raw-String input, (2) Double input,"
                     " (3) Expression file input, (4) Basic file input"
                     ">>> ")
        match mode:
            case "1":
                input_string = input("Enter expression: ")
                self.process_input(input_string)
                self.start()
            case '2':
                input_string1 = input("Enter expression 1: ")
                input_string2 = input("Enter expression 2: ")
                self.process_input(input_string1 + '|' + input_string2)
                self.start()
            case '3':
                self.file_check(1)
            case '4':
                self.file_check(2)
            case _:
                print("Invalid mode. Please select '1', '2', '3' or '4'.")
                self.start()


if __name__ == '__main__':
    matcher_ui = RegularExpressionMatcherUI()
    matcher_ui.start()
