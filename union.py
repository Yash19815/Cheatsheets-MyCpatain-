# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Perform set operations
union = E.union(N)
intersection = E.intersection(N)
difference = E.difference(N)
sym_difference = E.symmetric_difference(N)

# Print the results
print(f"Union of E and N is {union}")
print(f"Intersection of E and N is {intersection}")
print(f"Difference of E and N is {difference}")
print(f"Symmetric difference of E and N is {sym_difference}")