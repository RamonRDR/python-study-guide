# Compare comments that narrate each line with code that explains itself.


def calculate_total_with_noise(item_prices):
    # Create a total.
    total = 0

    # Loop through the prices.
    for item_price in item_prices:
        # Add the price to the total.
        total += item_price

    # Return the total.
    return total


def calculate_total(item_prices):
    return sum(item_prices)


prices_in_cents = [1250, 725, 300]

assert calculate_total_with_noise(prices_in_cents) == 2275
assert calculate_total(prices_in_cents) == 2275

print(calculate_total(prices_in_cents))
