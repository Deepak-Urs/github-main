######## PLEASE NOTE: RUN THE FOLLOWING COMMAND TO GET THE REQUIRED OUPTUT
# >> (Using Python3 for solution)
# python3 findPyramidDescent.py < [sample-input-file-name].txt



import sys

def findPyramidDescent():

    ######## CODE TO READ THE INPUT VIA TERMINAL
    # Read the input lines
    lines = sys.stdin.read().splitlines()
    lines = [line.strip() for line in lines if line.strip() != '']

    # Extract the target value
    target_line = next((line for line in lines if line.startswith("Target:")), None)
    if target_line is None:
        print("No target specified.")
        return
    target = int(target_line[len("Target:"):].strip())

    # Build the pyramid
    pyramid_lines = lines[lines.index(target_line) + 1:]
    pyramid = []
    for line in pyramid_lines:
        row = [int(x.strip()) for x in line.split(',')]
        pyramid.append(row)
    
    # Recursive function to find the path
    def find_path(level, index, current_product, path):
        current_number = pyramid[level][index]
        new_product = current_product * current_number

        # Prune paths where the product exceeds the target
        if new_product > target:
            return None

        # Prune paths where the target is not divisible by the new product
        if target % new_product != 0:
            return None

        if level == len(pyramid) - 1:
            if new_product == target:
                return path
            else:
                return None
        else:
            for move in ['L', 'R']:
                next_index = index if move == 'L' else index + 1

                if next_index >= len(pyramid[level + 1]):
                    continue

                result = find_path(level + 1, next_index, new_product, path + move)
                if result is not None:
                    return result
            return None

    # Start the search from the top of the pyramid
    result = find_path(0, 0, 1, '')
    print(result if result is not None else "null")

findPyramidDescent()
