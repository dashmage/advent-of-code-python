## advent of code 2021
## https://adventofcode.com/2021
## day 08


from unicodedata import digit


def parse_input(lines):
    return [line.split("|") for line in lines]


def part1(patterns):
    count_unique = 0
    easy_digits = [2, 4, 3, 7]
    for p in patterns:
        digits = p[1].strip().split()
        for d in digits:
            if len(d) in easy_digits:
                count_unique += 1
    return count_unique


def display_segments(segments):
    """
      Prints segments according to position in the list provided as argument.

          0
        =====
    1  |     |  2
       |     |
        =====
    3  |     |  4
       |     |
        =====
          6

    """

    print()
    segments_str = "".join(["".join(x) for x in segments])
    for i in range(7):
        print("  ", end="")
        if i == 0:
            print(f" {segments_str[0] * 4} ")
        elif i == 1 or i == 2:
            print(f"{segments_str[1]}    {segments_str[2]}")
        elif i == 3:
            print(f" {segments_str[3] * 4} ")
        elif i == 4 or i == 5:
            print(f"{segments_str[4]}    {segments_str[5]}")
        elif i == 6:
            print(f" {segments_str[6] * 4} ")
    print()


def part2(patterns):
    # wires used for each segment of the display
    segments = [set() for _ in range(7)]

    # digit_mappings = maps each digit to the wires that it comprises of
    # {0: '', 1: '', 2: '', ... 9: ''}
    digit_mapping = dict.fromkeys(range(10), set())

    # unique digits = number of wires(letters) : digit it generates
    unique_digits = {2: 1, 4: 4, 3: 7, 7: 8}
    final_sum = 0
    for p in patterns:
        # ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']
        input_signals = p[0].strip().split()

        # ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']
        output_signals = p[1].strip().split()

        for signal in input_signals:
            if len(signal) in unique_digits:
                digit = unique_digits[len(signal)]
                digit_mapping[digit] = set(signal)

        # {0: set(), 1: {'b', 'e'}, 2: set(), 3: set(), 4: {'c', 'b', 'g', 'e'}, 5: set(), 6: set(), 7: {'b', 'd', 'e'}, 8: {'b', 'e', 'f', 'd', 'a', 'c', 'g'}, 9: set()}

        # get s0 by comparing digits 7 and 1
        segments[0] = set(x for x in digit_mapping[7] if x not in digit_mapping[1])
        # From digit 1 we have 2 possibilities for both s2, s5
        s_25 = digit_mapping[1]
        # Comparing digits 4 and 1 we have 2 possibilities for both s1, s3
        s_13 = set(x for x in digit_mapping[4] if x not in digit_mapping[1])

        # get digit map for 9 and s6 wire
        incomplete_9 = digit_mapping[4].union(digit_mapping[7])
        for digit in input_signals:
            if len(digit) == 6:
                digit = set(digit)
                if len(digit - incomplete_9) == 1:
                    segments[6] = digit - incomplete_9
                    digit_mapping[9] = digit
                    break

        #  {0: set(), 1: {'b', 'e'}, 2: set(), 3: set(), 4: {'b', 'c', 'e', 'g'}, 5: set(), 6: set(), 7: {'b', 'd', 'e'}, 8: {'b', 'c', 'f', 'a', 'd', 'e', 'g'}, 9: {'b', 'c', 'f', 'd', 'e', 'g'}}

        # get digit map for 0 and s4, s1, s3 wires
        incomplete_0 = s_25.union(segments[0], segments[6])
        for digit in input_signals:
            if len(digit) == 6 and set(digit) != digit_mapping[9]:
                digit = set(digit)
                if len(digit - incomplete_0) == 2:
                    diff_14 = digit - incomplete_0
                    segments[4] = diff_14 - s_13
                    segments[3] = s_13 - diff_14
                    segments[1] = diff_14 - segments[4]
                    digit_mapping[0] = digit
                    break

        # get digit map for 6
        for digit in input_signals:
            digit = set(digit)
            if (
                len(digit) == 6
                and digit != digit_mapping[9]
                and digit != digit_mapping[0]
            ):
                digit_mapping[6] = digit
                segments[2] = s_25 - digit
                segments[5] = s_25 - segments[2]
                break

        digit_mapping[2] = segments[0].union(
            segments[2], segments[3], segments[4], segments[6]
        )
        digit_mapping[3] = segments[0].union(
            segments[2], segments[3], segments[5], segments[6]
        )
        digit_mapping[5] = segments[0].union(
            segments[1], segments[3], segments[5], segments[6]
        )

        # print("digit_mapping", "\n", digit_mapping, "\n\n", "segment", "\n", segment)
        output_signals = map(lambda x: set(x), output_signals)
        final_val = ""
        for signal in output_signals:
            i = 0
            for val in digit_mapping.values():
                if signal == val:
                    final_val += str(i)
                i += 1
        final_sum += int(final_val)
    return final_sum
