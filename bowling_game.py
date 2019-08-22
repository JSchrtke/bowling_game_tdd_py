class BowlingGame:
    def __init__(self):
        self.scores = []

    def roll(self, pins_hit):
        self.scores.append(pins_hit)

    def score(self):
        final_score = 0
        i = 0
        f = 0
        while f < 10:
            if self.is_spare(i) and not self.is_strike(i):
                final_score += self.scores[i] + self.scores[i + 1] + self.scores[i + 2]
            elif self.is_strike(i):
                s = self.get_strike_index(i)
                final_score += self.scores[s] + self.scores[s + 1] + self.scores[s + 2]
                i -= 1
            else:
                final_score += self.scores[i] + self.scores[i + 1]
            i += 2
            f += 1
        return final_score

    def is_strike_on_first_roll(self, s):
        return s % 2 == 0

    def is_spare(self, i):
        return self.scores[i] + self.scores[i + 1] == 1

    def is_strike(self, i):
        b = self.scores[i] == 10 or self.scores[i + 1] == 10
        return b

    def get_strike_index(self, i):
        if self.scores[i] == 10:
            return i
        return i + 1

