"""Storing High Scores for a Game."""


class Entry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name

    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)


class Scoreboard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        is_good = self._n < len(self._board) or self._board[-1].get_score() < score
        if is_good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            # we had already checked that score > self._board[j].get_score() in line 29, now start checking with j-1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry
