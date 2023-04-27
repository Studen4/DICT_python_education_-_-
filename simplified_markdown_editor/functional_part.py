"""All commands after !begin"""


class Commands:
    """Functionality"""

    def __init__(self):
        self.text = ""

    def add_plain(self, text):
        """Add plain text to the document"""
        self.text += text

    def add_bold(self, text):
        """Add bold text to the document"""
        self.text += f"**{text}**"

    def add_italic(self, text):
        """Add italic text to the document"""
        self.text += f"*{text}*"

    def add_header(self, text, level):
        """Add header text to the document"""
        if level < 1 or level > 6:
            raise ValueError("Level must be between 1 and 6")
        self.text += "#" * level + " " + text + "\n"

    def add_link(self, label, url):
        """Add link to the document"""
        self.text += f"[{label}]({url})"

    def add_inline_code(self, text):
        """Add inline code to the document"""
        self.text += f"`{text}`"

    def add_ordered_list(self, items):
        """Add ordered list to the document"""
        for i, item in enumerate(items):
            self.text += f"{i + 1}. {item}\n"

    def add_unordered_list(self, items):
        """Add unordered list to the document"""
        for item in items:
            self.text += f"* {item}\n"

    def add_new_line(self):
        """Add new line to the document"""
        self.text += "\n"
