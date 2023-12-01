numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class Operand:
    def __init__(self, value):
        self._value = int(value)
        self.operator = None

    def __repr__(self):
        return f"{self._value}"

    def calculate(self, value):
        if self.operator == "plus":
            self._value += value
        elif self.operator == "minus":
            self._value -= value
        elif self.operator == "times":
            self._value *= value

    def __getattribute__(self, name):
        if name == "_value" or name == "operator":
            return object.__getattribute__(self, name)

        elif name in ("plus", "minus", "times"):
            self.operator = name

        elif self.operator:
            self.operator = None
            # self.calculate(numbers[name])
        return self


(zero, one, two, three, four, five, six, seven, eight, nine) = (
    Operand(i) for i in range(0, 10)
)

print(two.minus.one)
