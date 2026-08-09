backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

shared = backend & data
combined = backend | data
backend_only = backend - data
exclusive = backend ^ data

print("Shared:", shared == {"python", "sql"})
print("Combined:", combined == {"python", "sql", "git", "pandas"})
print("Backend only:", backend_only == {"git"})
print("Exclusive:", exclusive == {"git", "pandas"})
print("Core subset:", {"python", "sql"} <= backend)
