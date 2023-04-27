"""Some simple edit modes to text"""

from functional_part import Commands


class TextEditor:
    def __init__(self):
        self.text = ""
        self.commands = ["!begin", "!done", "!help"]
        self.logs = []
        self.help_text = """All variants to change text in this editor:
        1. Plain - piece of raw text
        2. Bold - some text which need more attention
        3. Italic - some text with italics
        4. Link - some link to web-service
        5. Header - the text that will be placed at the beginning
        6. Unordered-list - some set of values without a clearly established order
        7. Ordered-list - some set of values with their correct positions
        8. New-line - change this line to next"""
        self.c = Commands()

    def begin(self):
        """ Main program work space both of editor"""
        while True:
            command = input("Enter command: ")
            if command == "!done":
                break
            if command == "!!plain":
                text = input("Enter text: ")
                self.c.add_plain(text)
            elif command == "!!bold":
                text = input("Enter text: ")
                self.c.add_bold(text)
            elif command == "!!italic":
                text = input("Enter text: ")
                self.c.add_italic(text)
            elif command == "!!header":
                text = input("Enter text: ")
                level = int(input("Enter level (1-6): "))
                self.c.add_header(text, level)
            elif command == "!!link":
                label = input("Enter label: ")
                url = input("Enter URL: ")
                self.c.add_link(label, url)
            elif command == "!!code":
                text = input("Enter text: ")
                self.c.add_inline_code(text)
            elif command == "!!ordered":
                items = []
                while True:
                    item = input("Enter item (press enter to finish): ")
                    if not item:
                        break
                    items.append(item)
                self.c.add_ordered_list(items)
            elif command == "!!unordered":
                items = []
                while True:
                    item = input("Enter item (press enter to finish): ")
                    if not item:
                        break
                    items.append(item)
                self.c.add_unordered_list(items)
            elif command == "!!new":
                self.c.add_new_line()
            else:
                print("Invalid command. Try again.")
        with open("formatted_text.md", "w") as file:
            file.write(self.c.text)

    def help(self):
        """To show Guide about commands in program"""
        print(self.help_text)

    def run(self):
        """Function which check correct of program"""
        print("Enter !begin, !help or !done option.")
        while True:
            option = input(">>>")
            if option in self.commands:
                self.logs.append(option)
                if option == "!begin":
                    self.begin()
                elif option == "!help":
                    self.help()
            else:
                self.logs.append(option + " - Incorrect!")
                print("Unknown formatting type or command!")

            if option == "!done":
                break

        log_filename = "text_editor_log.txt"
        with open(log_filename, "w") as log_file:
            for i, cmd in enumerate(self.logs, start=1):
                log_file.write(f"{i}. {cmd}\n")


if __name__ == "__main__":
    editor = TextEditor()
    editor.run()
