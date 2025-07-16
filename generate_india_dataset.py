import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('en_IN')

# ✅ Indian States & Cities
states_cities = {
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Prayagraj"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
    "Delhi": ["New Delhi", "Dwarka", "Karol Bagh", "Rohini", "Saket"],
    "Karnataka": ["Bengaluru", "Mysuru", "Mangalore", "Hubli", "Belagavi"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem", "Trichy"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Ajmer", "Udaipur"],
    "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Darbhanga"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain"],
    # Add more states with 4-5 cities each for full coverage
}

customer_types = ["Member", "Normal"]
genders = ["Male", "Female"]
product_lines = ["Food & Beverages", "Health & Beauty", "Electronic Accessories",
                 "Home & Lifestyle", "Sports & Travel", "Fashion & Clothing"]
payments = ["Cash", "UPI", "Credit Card", "Debit Card", "Net Banking"]

num_rows = 50000
data = []

for _ in range(num_rows):
    state = random.choice(list(states_cities.keys()))
    city = random.choice(states_cities[state])
    customer_type = random.choice(customer_types)
    gender = random.choice(genders)
    product = random.choice(product_lines)
    unit_price = round(random.uniform(50, 5000), 2)
    quantity = random.randint(1, 10)
    cogs = unit_price * quantity
    tax = round(cogs * 0.18, 2)
    sales = cogs + tax
    gross_income = round(cogs * 0.05, 2)
    date = fake.date_between(start_date="-6y", end_date="today")
    time = fake.time()
    payment = random.choice(payments)
    rating = round(random.uniform(4, 10), 1)

    data.append([
        fake.uuid4(), state, city, customer_type, gender, product,
        unit_price, quantity, tax, sales, date, time, payment, cogs,
        4.7619, gross_income, rating
    ])

columns = ["invoice id", "state", "city", "customer type", "gender", "product line",
           "unit price", "quantity", "tax 18%", "sales", "date", "time", "payment",
           "cogs", "gross margin percentage", "gross income", "rating"]

df = pd.DataFrame(data, columns=columns)

df.to_csv("india_supermarket_sales.csv", index=False, encoding="utf-8-sig")

print("✅ Dataset Created: india_supermarket_sales.csv with", num_rows, "rows")
