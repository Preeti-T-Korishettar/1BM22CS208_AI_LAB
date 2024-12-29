#1.
import itertools

variables = ['a', 'b', 'c']

def knowledge_base(assignment):
    a = assignment['a']
    b = assignment['b']
    c = assignment['c']
    return (not a or b) and (not b or not a) and (a or c)

def hypothesis(assignment):
    a = assignment['a']
    b = assignment['b']
    c = assignment['c']
    return not b or c

def validate_implication():
    all_possible_assignments = list(itertools.product([False, True], repeat=3))

    truth_assignments = [dict(zip(variables, assignment)) for assignment in all_possible_assignments]

    for assignment in truth_assignments:
        if knowledge_base(assignment):
            if not hypothesis(assignment):
                return False

    return True


if validate_implication():
    print("The knowledge base implies the hypothesis.")
else:
    print("The knowledge base does not imply the hypothesis.")
