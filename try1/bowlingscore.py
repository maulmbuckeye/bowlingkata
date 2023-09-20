
def score(*b):
    bowls = list(b)
    return scoring(bowls)


def scoring(bowls, frame=1):
    if len(bowls) <= 1 or frame > 10:
        return []
    next_frame = frame + 1
    if bowls[0] == 10:
        remaining_bowls = bowls[1:]
        this_frame = sum(bowls[0:3])
        return [this_frame] + scoring(remaining_bowls, next_frame)
    this_frame = bowls[0] + bowls[1]
    remaining_bowls = bowls[2:]
    if this_frame == 10:
        this_frame += bowls[2]
    return [this_frame] + scoring(remaining_bowls, next_frame)


