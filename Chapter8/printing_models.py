# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing modles: {current_design}")
#     completed_models.append(current_design)

# #Display all completed models.
# print(f"\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# ---------------- Fuction Section --------------------

def print_models(unprinted_designs, completed_models):
    """Simulate printing eaqch design, untull none are left."""
    """Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Print Model : {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the modles that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahredon']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)