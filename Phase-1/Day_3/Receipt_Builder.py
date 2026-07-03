def build_receipt(**details):
    width = 40
    lines = [
        "=" * width,
        "RECEIPT".center(width),
        "=" * width,
    ]

    for key, value in details.items():
        lines.append(f"{key.capitalize():<15}: {value}")

    lines.append("-" * width)
    lines.append("Thank you for your purchase!".center(width))
    lines.append("=" * width)

    return "\n".join(lines)

# Call it with different sets of details
print(build_receipt(name="Salman", amount=250, type="Grocery"))
print() 
print(build_receipt(name="Saif", amount=1200, type="Electronics", store="Croma"))