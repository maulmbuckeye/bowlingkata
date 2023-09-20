
def score(*b):
    bowls = list(b)
    return Bowling(bowls).score()


class Bowling:

    def __init__(self, bowls, this_frame=1):
        self.bowls = bowls
        self.this_frame = this_frame
        pass

    def score(self):
        if not self.bowls or self.this_frame > 10:
            return []

        if self.is_strike:
            balls_to_score, balls_in_frame = 3, 1
        elif self.is_spare:
            balls_to_score, balls_in_frame = 3, 2
        else:
            balls_to_score, balls_in_frame = 2, 2

        score_for_frame, remaining_bowls = self.how_to_score(balls_to_score, balls_in_frame)

        next_frame = self.this_frame + 1
        return [score_for_frame] + Bowling(remaining_bowls, next_frame).score()

    def how_to_score(self, balls_to_score, balls_in_frame):
        score_for_frame = self.score_next(balls_to_score)
        remaining_bowls = self.bowls[balls_in_frame:]
        return score_for_frame, remaining_bowls

    @property
    def is_spare(self):
        return self.score_next(2) == 10

    @property
    def is_strike(self):
        return self.score_next(1) == 10

    def score_next(self, balls=3):
        if len(self.bowls) < balls:
            return 'open'
        return sum(self.bowls[0:balls])


def scoring(bowls, this_frame=1):

    if len(bowls) == 0 or this_frame > 10:
        return []
    if len(bowls) == 1:
        return ['open']
    next_frame = this_frame + 1
    if bowls[0] == 10:
        remaining_bowls = bowls[1:]
        if len(bowls) >= 3:
            this_frame = sum(bowls[0:3])
        else:
            this_frame = 'open'
    elif sum(bowls[0:2]) == 10:
        remaining_bowls = bowls[2:0]
        if len(bowls) >= 3:
            this_frame = sum(bowls[0:3])
        else:
            this_frame = 'open'
    else:
        remaining_bowls = bowls[2:]
        this_frame = sum(bowls[0:2])

    return [this_frame] + scoring(remaining_bowls, next_frame)
