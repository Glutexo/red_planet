from collections import namedtuple
from enum import auto
from enum import Enum


class Commands(Enum):
    EXIT = auto()


class State(
    namedtuple("State", ["player_count", "active_player", "previous"], defaults=(2, 0, []))
):
    def _next(self, **fields):
        return self._replace(previous=self.history, **fields)

    def next_player(self):
        next_player = self.active_player + 1
        if next_player == self.player_count:
            next_player = 0
        return self._next(active_player=next_player)

    @property
    def history(self):
        return self.previous + [self]


def loop(state, callback):
    while True:
        command = callback(state)
        if command is Commands.EXIT:
            return state

        state = state.next_player()
