import sys
import math

print(sys.version)


def distance(x, y):
    return math.sqrt(x**2 + y**2)


def main(lines):

    #stones = [tuple(map(float, input().split())) for _ in range(16)]
    stones=[tuple(map(float, lines.split()))]
    yellow_stones = stones[::2]
    red_stones = stones[1::2]

    yellow_stones_in_house = [
        stone for stone in yellow_stones if distance(*stone) <= 10]
    red_stones_in_house = [
        stone for stone in red_stones if distance(*stone) <= 10]

    if not yellow_stones_in_house and not red_stones_in_house:
        print("0 0")
        return

    sorted_yellow = sorted(yellow_stones_in_house,
                           key=lambda stone: distance(*stone))
    sorted_red = sorted(red_stones_in_house,
                        key=lambda stone: distance(*stone))

    closest_yellow_distance = distance(
        *sorted_yellow[0]) if sorted_yellow else float("inf")
    closest_red_distance = distance(
        *sorted_red[0]) if sorted_red else float("inf")

    yellow_score = sum(1 for stone in yellow_stones_in_house if distance(
        *stone) < closest_red_distance)
    red_score = sum(1 for stone in red_stones_in_house if distance(
        *stone) < closest_yellow_distance)

    print(yellow_score, red_score)
    
    print(lines)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
