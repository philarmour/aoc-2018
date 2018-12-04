from pathlib import Path


def parse(line: str):
    tokens = line.split()
    xy = tokens[2][:-1].split(",")
    wh = tokens[3].split("x")
    return {
        'id': tokens[0],
        'location': tokens[2][:-1],
        'x': int(xy[0]),
        'y': int(xy[1]),
        'dims': tokens[3],
        'w': int(wh[0]),
        'h': int(wh[1])
    }


def load(file: str):
    input_txt = Path(file).read_text()
    claims = [parse(line) for line in input_txt.splitlines()]
    # print("all claims: {}".format(claims))
    return claims


def part_1(file: str):
    claims = load(file)

    unique_squares = set()
    conflict_squares = set()

    # brute force!
    for claim in claims:
        # x-axis
        for x in range(claim['w']):
            # y-axis
            for y in range(claim['h']):
                key = '{},{}'.format((claim['x'] + x), (claim['y'] + y))
                if key in unique_squares:
                    conflict_squares.add(key)
                else:
                    unique_squares.add(key)

    # print("Part 1 - unique squares: {}".format(unique_squares))
    # print("Part 1 - count of unique squares: {}".format(len(unique_squares)))
    print("Part 1 - conflicting square inches: {}".format(len(conflict_squares)))


def part_2(file: str):
    claims = load(file)

    unique_squares = {}

    # brute force!
    # step 1 - fill up the squares
    for claim in claims:
        # x-axis
        for x in range(claim['w']):
            # y-axis
            for y in range(claim['h']):
                key = '{},{}'.format((claim['x'] + x), (claim['y'] + y))
                if key in unique_squares:
                    unique_squares[key] = "{},{}".format(unique_squares[key], claim['id'])
                else:
                    unique_squares[key] = claim['id']

    # step 2 - check the squares again
    for claim in claims:
        conflict = False
        # x-axis
        for x in range(claim['w']):
            # y-axis
            for y in range(claim['h']):
                key = '{},{}'.format((claim['x'] + x), (claim['y'] + y))
                # check of the value of the ID is only this claim otherwise it's a conflict
                if unique_squares[key] != claim['id']:
                    conflict = True

        if not conflict:
            print("Part 2 - non-conflicting claim is: {}".format(claim))


def main():
    # load('day_03/input.txt')

    part_1('day_03/input.txt')

    part_2('day_03/input.txt')


if __name__ == "__main__":
    main()
