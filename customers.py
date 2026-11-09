
# ISM 2411 - Lab 11
# Name: Jackson Thom

# Reflection 1:
# I would use .get() when I am not sure if a customer has
# information saved, like an email or phone number. I would
# use brackets when I know the information should be there
# because it will show an error if something is missing.

# Reflection 2:
# This reminds me of using a PivotTable in Excel to organize
# sales by category or region. Python could be more useful
# for large datasets because it can automatically calculate
# totals without manually updating a spreadsheet.


# Exercise 1: One Customer

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and Add

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe Lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email is not in the dictionary")


# Exercise 4: Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys.
# With .items(), we get both the keys and values.

for key in customer:
    print(key)


# Exercise 5: Lookup Table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)

print("Tier:", tier)
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of Dicts

customer2 = {"name": "Bob", "tier": "silver"}
customer3 = {"name": "Charlie", "tier": "gold"}

customers = [customer, customer2, customer3]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{name}: {tier}, Discount: ${discount_amount:.2f}")


# Exercise 7: Nested Catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}, Stock: {details['stock']}")


# Exercise 8: Sales by Region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")
