def ordered_sandwiches(*sandwiches):
    print(f"Here are the ordered sandwich")
    for sandwich in sandwiches:
        print(f"- {sandwich}")

ordered_sandwiches('vegetable', 'beef')
ordered_sandwiches('chiken', 'cheese', 'double beef')