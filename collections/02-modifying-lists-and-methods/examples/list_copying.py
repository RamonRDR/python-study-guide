original = ["strings", "numbers"]
alias = original
independent = original.copy()

alias.append("lists")
independent.append("tuples")

print("Original:", original)
print("Alias:", alias)
print("Copy:", independent)
