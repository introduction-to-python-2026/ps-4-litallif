def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    if not formula:
        return []

    for i in range(len(formula)):
        if formula[i].isupper() and i > 0:
            split_formula.append(formula[start:i])
            start = i

    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    if not formula:
        return "", 1

    digit_location = -1

    for i in range(len(formula)):
        if formula[i].isdigit():
            digit_location = i
            break 

    if digit_location == -1:
        return formula, 1
    else:
 
        a1= formula[:digit_location]
        a2 = formula[digit_location:]
        return a1, int(a2)
