import math


def parse_order(items_csv):
    """Return {name: qty}. Malformed items are skipped; non-string input gives {}."""
    order = {}
    if not isinstance(items_csv, str):
        return order
    for item in items_csv.split(','):
        name, sep, qty = item.partition(':')
        name = name.strip()
        if not sep or not name:
            continue
        try:
            qty = int(qty)
        except ValueError:
            continue
        if qty > 0:
            order[name] = qty
    return order


def delivery_eta(distance_km):
    """Return ETA in minutes, or None if the distance is not a valid non-negative number."""
    try:
        distance = float(distance_km)
    except (TypeError, ValueError):
        return None
    minutes = 15 + distance * 4
    if distance < 0 or not math.isfinite(minutes):
        return None
    return int(minutes)


def coupon_discount(code):
    """Return the discount for a SAVE<number> code, or 0 for anything else."""
    if not isinstance(code, str):
        return 0
    code = code.strip().upper()
    if not code.startswith('SAVE'):
        return 0
    amount = code[4:]
    if not (amount.isascii() and amount.isdigit()):
        return 0
    try:
        return int(amount)
    except ValueError:  # too many digits for int()
        return 0


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result if result else "No valid items found")

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result if result is not None else "Invalid distance")

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result if result else "Invalid coupon code")


if __name__ == "__main__":
    main()
