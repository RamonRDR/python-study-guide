from collections import ChainMap


defaults = {"mode": "safe", "retries": 2, "region": "global"}
environment = {"retries": 4, "region": "test"}
command_line = {"mode": "fast"}

config = ChainMap(command_line, environment, defaults)

print(f"mode: {config['mode']}")
print(f"retries: {config['retries']}")
print(f"region: {config['region']}")

config["retries"] = 1

print(f"command-line map: {command_line}")
print(f"environment map: {environment}")
