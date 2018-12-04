from pathlib import Path

def load(file: str):
    input_txt = Path(file).read_text()
    return [str(i) for i in input_txt.split()]


def safe_add(num_or_null):
    val = 1
    if num_or_null:
        val = num_or_null + 1
    return val


def check_name(name: str):
    bag = {}
    is_two = False
    is_three = False
    for i in name:
        bag[i] = safe_add(bag.get(i))
    for c in bag.keys():
        if not is_two and bag[c] == 2:
            is_two = True
        if not is_three and bag[c] == 3:
            is_three = True
        if is_two and is_three:
            break
    return is_two, is_three


def part_1(file: str):
    names = load(file)
    twos = 0
    threes = 0
    for name in names:
        is_two, is_three = check_name(name)
        twos += int(is_two)
        threes += int(is_three)

    check_sum = twos * threes
    print("Part 1 - check_sum is {}".format(check_sum))


def check_names(n1: str, n2: str):
    # print("Comparing: {} and {}".format(n1, n2))
    for i, c in enumerate(n1):
        r1 = n1[:i] + n1[i+1:]
        r2 = n2[:i] + n2[i+1:]
        if r1 == r2:
            print("Match! {} (from: {} & {}".format(r1, n1, n2))


def part_2(file: str):
    names = load(file)
    print("length of names list {} ".format(len(names)))

    for idx, n1 in enumerate(names):
        # print("checking {} - {}".format(n1, idx))
        for n2 in names[idx+1:]:
            check_names(n1, n2)



def main():

    # input_arr = load('day_02/input.txt')
    # print("values loaded is {}".format(input_arr))

    part_1('day_02/input.txt')

    part_2('day_02/input.txt')


if __name__ == "__main__":
    main()
