from pathlib import Path


def load(file: str):
    input_txt = Path(file).read_text()
    return [str(i) for i in input_txt.split()]


def part_1(file: str):
    print("Part 1 - check_sum is {}".format(file))


def part_2(file: str):
    print("Part 1 - check_sum is {}".format(file))


def main():

    part_1('day_02/input.txt')

    part_2('day_02/input.txt')


if __name__ == "__main__":
    main()
