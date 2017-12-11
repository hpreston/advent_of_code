#! /usr/bin/env python
"""
Solution for Day 8: I Heard You Like Registers
http://adventofcode.com/2017/day/8
"""

# Global Variables
registers = {}
max_value = 0


def file_pass(input_file):
    """
    Read in file and convert each line to a dictionary entry of details
    """
    # {
    #     "register": "name",
    #     "instruction": "inc" or "dec",
    #     "value": int,
    #     "condition": "condition"
    # }

    result = []

    with open(input_file) as f:
        for line in f:
            # print(line)
            # Turn line into list
            line_list = line.split()
            line_dict = {
                            "register": line_list[0],
                            "check_register": line_list[4],
                            "condition": (" ").join(line_list[5:7])
                        }
            if line_list[1] == "inc":
                line_dict["instruction"] = "+= {}".format(line_list[2])
            elif line_list[1] == "dec":
                line_dict["instruction"] = "-= {}".format(line_list[2])
            result.append(line_dict)
    return result

def execute_step(step):
    print("Testin: registers['{}'] {}".format(step["check_register"], step["condition"]))
    if eval("registers['{}'] {}".format(step["check_register"], step["condition"])):
        print("Executing: registers['{}'] {}".format(step["register"], step["instruction"]))
        exec("registers['{}'] {}".format(step["register"], step["instruction"]))
        if max(registers.values()) > globals()["max_value"]:
            globals()["max_value"] = max(registers.values())

def process(input_file):
    processed_file = file_pass(input_file)
    register_names = set([i["register"] for i in processed_file])
    print("Register Names: {}".format(register_names))
    for reg in register_names:
        registers[reg] = 0

    for step in processed_file:
        execute_step(step)

    result = max(registers.values())
    return result



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
        result = process(args.file)


    # elif args.style ==2:
    #     result1 = debugger_part1(args.file)
    #     result = debugger_part2(result1[1])
    #     print(result)


    print("Solution: {}".format(result))
    print("Max Value: {}".format(max_value))
