# business_card.py
# Task 3 -- Digital Business Card (Dictionary)
# Real-world use: a reusable tool for your own LinkedIn/resume details.

card = {
    "name": "Salman",
    "role": "AI & Data Science Student",
    "email": "your.email@example.com",
    "phone": "+91-XXXXXXXXXX",
    "linkedin": "linkedin.com/in/your-profile"
}

def print_card(data):
    print("-" * 30)
    print(f"Name     : {data['name']}")
    print(f"Role     : {data['role']}")
    print(f"Email    : {data['email']}")
    print(f"Phone    : {data['phone']}")
    print(f"LinkedIn : {data['linkedin']}")
    print("-" * 30)

print_card(card)

# Update role, then reprint to confirm the change
card["role"] = "Generative AI Developer"
print_card(card)