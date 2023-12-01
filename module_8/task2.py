class ParseError(Exception):
    """Error while parsing file"""
        
    def __init__(self, *args, line_no=None, text=None):
        super().__init__(*args)
        self.line_no = line_no
        self.text = text

    def __str__(self):
        if not self.line_no and not self.text:
            return super().__str__()
        elif not self.line_no:
            return f"cannot parse text: '{self.text}'"
        elif not self.text:
            return f"cannot parse text on line {self.line_no}"
        else:
            return f"cannot parse text on line {self.line_no}: '{self.text}'"


# raise ParseError()
# raise ParseError('some standard message')
# raise ParseError(line_no=10)
# raise ParseError(text='abc')
# raise ParseError(line_no=10, text='...')