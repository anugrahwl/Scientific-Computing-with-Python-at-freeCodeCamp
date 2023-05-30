def arithmetic_arranger(expression, solution=False):

    result = []
    container = []
    length = len(expression)

    first_line  = ""
    second_line = ""
    third_line  = ""
    forth_line  = ""

    ## Check for errors
    # Error: Too many problems.
    if length > 5:
        return "Error: Too many problems."

    for i in range(length):
        expression[i] = expression[i].split()

        # Error: Operator must be '+' or '-'.
        # Calculate for result
        # Error: Numbers must only contain digits.
        try:
            if expression[i][1] == '+':
                result_ = int(expression[i][0]) + int(expression[i][2])
            elif expression[i][1] == '-':
                result_ = int(expression[i][0]) - int(expression[i][2])
            else:
                return "Error: Operator must be '+' or '-'."
        except:
            return "Error: Numbers must only contain digits."

        result.append(str(result_))

        # Error: Numbers cannot be more than four digits.
        if len(expression[i][0]) > 4 or len(expression[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    ## Formatting
        # Calculate the container sizes
        length_1 = len(expression[i][0])
        length_2 = len(expression[i][2])

        if length_1 > length_2:
            container.append(length_1 + 2)
        else:
            container.append(length_2 + 2)

        # First line of the output
        first_line += ' ' * (container[i] - length_1) + expression[i][0] + "    " # double space
        # Second line of the output
        second_line += expression[i][1] + ' ' * (container[i] - length_2 - 1) + expression[i][2] + "    " # double space
        # Third line of the output
        third_line += '-' * container[i] + "    " # double space
        # Forth line of the output
        forth_line += ' ' * (container[i] - len(result[i])) + result[i] + "    " # double space

    output = first_line[:-4] + '\n' + second_line[:-4] + '\n' + third_line[:-4]
    if solution:
        output += '\n' + forth_line[0:-4]

    return output
