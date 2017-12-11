#! /usr/bin/env python
"""
Solution for Day 7: Recursive Circus
http://adventofcode.com/2017/day/7
"""

def file_pass(input_file):
    """
    Read in file and convert each line to a dictionary entry of details
    """
    # {
    #     "program_name": "name",
    #     "program_weight": weight,
    #     "holding": [
                    #     {"program_name": "name"}
                    # ]
    # }

    result = {}

    with open(input_file) as f:
        for line in f:
            # print(line)
            # Turn line into list
            line_list = line.split()
            line_dict = {
                            "program_name": line_list[0],
                            "program_weight": int(line_list[1][1:line_list[1].index(")")]),
                            "holding": {}
                        }
            if len(line_list) > 2:
                for i in range(3, len(line_list)):
                    sub_program = line_list[i]
                    if sub_program[len(sub_program) - 1] == ",":
                        sub_program = sub_program[0:len(sub_program) - 1]
                    # line_dict["holding"].append({"program_name": sub_program})
                    line_dict["holding"][sub_program] = {"program_name": sub_program}
            # result.append(line_dict)
            result[line_dict["program_name"]] = line_dict

    return result

def build_base(input_list):
    """
    Create a base dictionary representing the base tree.
    """
    # Get list of all sub programs
    sub_programs = []
    for program in input_list.values():
        for sub_program in program["holding"].values():
            sub_programs.append(sub_program["program_name"])

    # print("Subprograms")
    # print(sub_programs)

    # Find the bottom program (ie not in list of sub_programs)
    for program in input_list.values():
        # print(program)
        if program["program_name"] not in sub_programs:
            # print("found bottom")
            bottom_program = program

    # Build build
    tower = process_sub(bottom_program, input_list)

    # Complete the Tree
    # for sub_program in bottom_program["holding"].keys():
    #     # fill in details of sub_program
    #     print("Processing sub program: " + sub_program)
    #     bottom_program["holding"][sub_program] = input_list[sub_program]

    return tower

def process_sub(program, input_list):
    """
    Take the input sub_program, and add any holding to it
    """
    # Complete the Tree
    for sub_program in program["holding"].keys():
        # fill in details of sub_program
        # print("Processing sub program: " + sub_program)
        if len(input_list[sub_program]["holding"]) != 0:
            proc_sub_prog = process_sub(input_list[sub_program], input_list)
        else:
            proc_sub_prog = input_list[sub_program]
        program["holding"][sub_program] = proc_sub_prog
    return program

def calc_weight(program, input_list):
    """
    Add "total_weight" to each program.
    It equals programs own weight, plus the weight of all programs on it.
    """
    total_program_weight = program["program_weight"]
    if len(program["holding"]) != 0:
        for sub_program in program["holding"].keys():
            # print(sub_program)
            proc_sub_prog = calc_weight(program["holding"][sub_program], input_list)
            total_program_weight += proc_sub_prog["total_weight"]

    program["total_weight"] = total_program_weight
    return program

def find_heavy(program):
    weights = []
    max_program = {}
    max_weight = 0
    min_weight = 10000000000000000
    for sub_program in program["holding"].keys():
        weights.append((sub_program, program["holding"][sub_program]["total_weight"]))
    for i in weights:
        print("{} weighs {}".format(i[0], i[1]))
        if i[1] > max_weight:
            max_weight = i[1]
            max_program = program["holding"][i[0]]
        if i[1] < min_weight:
            min_weight = i[1]

    print("Heaviest Program is {} at {}\n".format(max_program["program_name"], max_program["total_weight"]))
    print("It weighs {} more than the others.".format(max_weight - min_weight))

    find_heavy(max_program)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Advent of Code Day 5.')
    parser.add_argument("--file", type=str, help="File name to test.")
    parser.add_argument('--style', type=int, default=1,
                        help="Style of test")

    args = parser.parse_args()
    print("Input file: {}".format(args.file))
    print("Test Style: {}".format(args.style))

    if args.style == 1:
        processed_file = file_pass(args.file)
        base = build_base(processed_file)
        base = calc_weight(base, processed_file)
        result = base["program_name"]
        find_heavy(max_program)
    # elif args.style ==2:
    #     result1 = debugger_part1(args.file)
    #     result = debugger_part2(result1[1])
    #     print(result)


    print("Solution: {}".format(result))
