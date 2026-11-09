
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
