class Player:
    id: int
    name: str
    scores: int
    games: list

    def __init__(self, id: int, name: str) -> None:
        self.id: int = id
        self.name: str = name
        self.scores: int = 0
        self.games: list = []

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores

    def get_mean(self) -> float:
        return self.scores / len(self.games)


class Power:
    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost

    def use(self, player: Player) -> None:
        if isinstance(self, MagicPower):
            player.scores += 1

        elif isinstance(self, PhysicalPower):
            self.players.setdefault(player.id, self.count)

            if self.players.get(player.id) > 0:
                self.players[player.id] -= 1
            else:
                return print(f"{player.name} cannot use {self.name}")

        print(f"{player.name} used {self.name}")


class PhysicalPower(Power):
    def __init__(self, name: str, cost: int, count: int):
        super().__init__(name, cost)
        self.count = count
        self.players: dict[str, int] = {}


class MagicPower(Power):
    pass


# p1 = Player(1, "Bilbo")
# p2 = Player(2, "Mark")
# t = PhysicalPower("teleport", 10, count=1)
# t.use(p1)
# t.use(p1)
# t.use(p2)
# t.use(p2)
# t.use(p2)
# print(p1.scores)
# print(p2.scores)

# b = MagicPower("black magic", 200)
# b.use(p1)
# print(p1.scores)
# b.use(p1)
# print(p1.scores)
