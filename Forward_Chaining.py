# Forward Chaining Reasoning in Python

# Define facts and rules as dictionaries and lists
facts = {
    "American(Robert)": True,
    "Missile(T1)": True,
    "Owns(A, T1)": True,
    "Enemy(A, America)": True,
}

rules = [
    # Rule 1: All missiles are weapons
    {"if": ["Missile(x)"], "then": ["Weapon(x)"]},

    # Rule 2: A criminal is made if someone sells weapons to a hostile country
    {"if": ["American(p)", "Weapon(q)", "Sells(p, q, r)", "Hostile(r)"], "then": ["Criminal(p)"]},

    # Rule 3: Robert sells all missiles to country A
    {"if": ["Missile(x)", "Owns(A, x)"], "then": ["Sells(Robert, x, A)"]},

    # Rule 4: If someone is an enemy of America, they are hostile
    {"if": ["Enemy(x, America)"], "then": ["Hostile(x)"]},
]

# Query to be proved
query = "Criminal(Robert)"

# Helper function to unify facts with conditions
def unify_condition_with_fact(condition, fact):
    predicate_condition, args_condition = condition.split("(")
    predicate_fact, args_fact = fact.split("(")

    if predicate_condition != predicate_fact:
        return None  # Predicates must match

    args_condition = args_condition[:-1].split(",")
    args_fact = args_fact[:-1].split(",")

    if len(args_condition) != len(args_fact):
        return None

    substitutions = {}

    for var, constant in zip(args_condition, args_fact):
        if var.islower():  # If it's a variable, substitute it
            substitutions[var] = constant
        elif var != constant:  # If constants don't match, return None
            return None

    return substitutions

# Function to apply substitutions to a statement
def substitute_statement(statement, substitutions):
    predicate, args = statement.split("(")
    args = args[:-1].split(",")
    new_args = [substitutions.get(arg, arg) for arg in args]
    return f"{predicate}({', '.join(new_args)})"

# Forward chaining algorithm to derive facts
def perform_forward_chaining(facts, rules, query):
    inferred_facts = set(facts.keys())  # Start with the given facts

    while True:
        new_inferences = set()

        for rule in rules:
            # Process the "if" part of the rule
            conditions = rule["if"]
            possible_substitutions = [{}]

            for condition in conditions:
                temp_substitutions = []

                for fact in inferred_facts:
                    subs = unify_condition_with_fact(condition, fact)
                    if subs is not None:
                        # Combine existing substitutions with new ones
                        for existing_subs in possible_substitutions:
                            combined_subs = existing_subs.copy()
                            combined_subs.update(subs)
                            temp_substitutions.append(combined_subs)

                if not temp_substitutions:
                    break
                possible_substitutions = temp_substitutions

            # If conditions are satisfied, infer the "then" part
            if possible_substitutions:
                for subs in possible_substitutions:
                    for conclusion in rule["then"]:
                        new_fact = substitute_statement(conclusion, subs)
                        new_inferences.add(new_fact)

        # Add the newly inferred facts to the set of facts
        if query in new_inferences:
            return True  # The query has been proven

        # If no new facts were inferred, stop the process
        if not new_inferences - inferred_facts:
            return False  # The query cannot be proven

        inferred_facts.update(new_inferences)

# Run the forward chaining algorithm and check if the query can be proven
result = perform_forward_chaining(facts, rules, query)

# Output the result
if result:
    print(f"It is proven that'{query}' is true")
else:
    print(f"It is proven that '{query}' is false")
