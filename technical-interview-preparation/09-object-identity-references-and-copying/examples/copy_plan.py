"""Copy a nested plan without sharing its mutable containers."""
from copy import deepcopy


def clone_plan(plan: dict) -> dict:
    return deepcopy(plan)


if __name__ == "__main__":
    original = {"steps": ["draft"]}
    cloned = clone_plan(original)
    cloned["steps"].append("review")
    print(original, cloned)
