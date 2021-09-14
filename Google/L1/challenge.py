# Due to the nature of the space station's outer paneling, all of its solar panels must be squares.
# Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors,
# and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares.
# For example, if you had a total area of 12 square yards of solar material, you would be able to make one
# 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into
# three 1x1 square solar panels.

# Write a function solution(area) that takes as its input a single unit of measure representing the total
# area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the
# largest squares you could make out of those panels, starting with the largest squares first.
# So, following the example above, solution(12) would return [9, 1, 1, 1].

# highest square root that doesn't go over, remaining would then find the highest


def solution(area):
    arr = []
    while area > 0:
        sqrtRound = int(area ** 0.5)
        sqrtRound *= sqrtRound
        arr.append(sqrtRound)
        area -= sqrtRound
    return arr