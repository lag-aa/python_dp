class Lucas:
    def __init__(self, u0, u1, p, q, n):
        self.u0 = u0
        self.u1 = u1
        self.p = p
        self.q = q
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if index >= len(self) or index < -len(self):
            raise IndexError("Index out of range")
        index %= len(self)

        if index == 0 or index == 1:
            return (self.u0, self.u1)[index]
        else:
            return self.p * self[index - 1] - self.q * self[index - 2]


# l = Lucas(2, 1, 1, -1, 10)
# print(list(l))
