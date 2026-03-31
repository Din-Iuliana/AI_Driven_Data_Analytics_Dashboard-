import random
from datetime import date, timedelta

random.seed(42)

first_names = [
    'Maria', 'Ion', 'Elena', 'Andrei', 'Ana', 'Mihai', 'Cristina', 'Alexandru',
    'Diana', 'Stefan', 'Laura', 'Gabriel', 'Adriana', 'Bogdan', 'Simona',
    'Catalin', 'Raluca', 'Dan', 'Ioana', 'Victor', 'Alina', 'George',
    'Monica', 'Florin', 'Carmen', 'Razvan', 'Daniela', 'Marius', 'Oana',
    'Vlad', 'Iulia', 'Robert', 'Roxana', 'Cosmin', 'Bianca', 'Lucian',
    'Valentina', 'Adrian', 'Denisa', 'Sorin', 'Larisa', 'Claudiu',
    'Andreea', 'Ciprian', 'Corina', 'Dragos', 'Irina', 'Liviu', 'Nicoleta', 'Paul'
]

last_names = [
    'Popescu', 'Ionescu', 'Dumitrescu', 'Popa', 'Georgescu', 'Stanescu',
    'Radu', 'Marin', 'Florea', 'Nistor', 'Dinu', 'Stoica', 'Matei',
    'Vlad', 'Dragomir', 'Neagu', 'Ene', 'Moldovan', 'Serban', 'Lazar',
    'Tanase', 'Barbu', 'Preda', 'Sandu', 'Voicu', 'Costea', 'Vasile',
    'Tudor', 'Mihai', 'Stan', 'Rusu', 'Oprea', 'Mocanu', 'Zamfir',
    'Lungu', 'Manole', 'Iacob', 'Chiriac', 'Pintilie', 'Grigorescu'
]

products = [
    ('Laptop Pro 15', 4500.00, 'Electronics'),
    ('Laptop Pro 17', 5200.00, 'Electronics'),
    ('Laptop Basic 14', 2500.00, 'Electronics'),
    ('Laptop Basic 15', 2800.00, 'Electronics'),
    ('Ultrabook Slim', 3800.00, 'Electronics'),
    ('Gaming Laptop', 6500.00, 'Electronics'),
    ('Monitor 27 4K', 1200.00, 'Electronics'),
    ('Monitor 24 FHD', 800.00, 'Electronics'),
    ('Monitor 32 Curved', 1800.00, 'Electronics'),
    ('Monitor 21 Basic', 500.00, 'Electronics'),
    ('Webcam HD', 200.00, 'Electronics'),
    ('Webcam 4K Pro', 450.00, 'Electronics'),
    ('External SSD 1TB', 400.00, 'Electronics'),
    ('External SSD 2TB', 700.00, 'Electronics'),
    ('External HDD 4TB', 350.00, 'Electronics'),
    ('Printer Laser', 600.00, 'Electronics'),
    ('Printer Inkjet', 300.00, 'Electronics'),
    ('Scanner A4', 250.00, 'Electronics'),
    ('UPS 1000VA', 400.00, 'Electronics'),
    ('Router WiFi 6', 350.00, 'Electronics'),
    ('Wireless Mouse', 50.00, 'Accessories'),
    ('Gaming Mouse', 150.00, 'Accessories'),
    ('Ergonomic Mouse', 120.00, 'Accessories'),
    ('Mechanical Keyboard', 350.00, 'Accessories'),
    ('Wireless Keyboard', 180.00, 'Accessories'),
    ('Gaming Keyboard RGB', 450.00, 'Accessories'),
    ('USB-C Hub 7-port', 150.00, 'Accessories'),
    ('USB-C Hub 4-port', 80.00, 'Accessories'),
    ('Docking Station', 500.00, 'Accessories'),
    ('Headphones Wireless', 300.00, 'Accessories'),
    ('Headphones Gaming', 400.00, 'Accessories'),
    ('Earbuds Pro', 250.00, 'Accessories'),
    ('Notebook Stand', 180.00, 'Accessories'),
    ('Laptop Cooling Pad', 100.00, 'Accessories'),
    ('Mousepad XL', 60.00, 'Accessories'),
    ('Webcam Light Ring', 80.00, 'Accessories'),
    ('Cable Management Kit', 40.00, 'Accessories'),
    ('Screen Protector 15', 30.00, 'Accessories'),
    ('Laptop Sleeve 15', 70.00, 'Accessories'),
    ('Laptop Backpack', 120.00, 'Accessories'),
    ('Office Desk 120cm', 900.00, 'Furniture'),
    ('Office Desk 160cm', 1200.00, 'Furniture'),
    ('Standing Desk', 1800.00, 'Furniture'),
    ('Corner Desk L-Shape', 1500.00, 'Furniture'),
    ('Compact Desk 100cm', 600.00, 'Furniture'),
    ('Ergonomic Chair Pro', 1500.00, 'Furniture'),
    ('Ergonomic Chair Basic', 800.00, 'Furniture'),
    ('Gaming Chair', 1200.00, 'Furniture'),
    ('Office Chair Standard', 500.00, 'Furniture'),
    ('Stool Adjustable', 300.00, 'Furniture'),
    ('Desk Lamp LED', 120.00, 'Furniture'),
    ('Desk Lamp Clip', 60.00, 'Furniture'),
    ('Monitor Arm Single', 200.00, 'Furniture'),
    ('Monitor Arm Dual', 350.00, 'Furniture'),
    ('Bookshelf 5-Tier', 400.00, 'Furniture'),
    ('Filing Cabinet', 450.00, 'Furniture'),
    ('Whiteboard 120x90', 250.00, 'Furniture'),
    ('Cork Board 90x60', 80.00, 'Furniture'),
    ('Footrest Ergonomic', 100.00, 'Furniture'),
    ('Cable Tray Under-Desk', 50.00, 'Furniture'),
    ('Wireless Charger Pad', 45.00, 'Gadgets'),
    ('Power Bank 20000mAh', 120.00, 'Gadgets'),
    ('Smart Plug WiFi', 35.00, 'Gadgets'),
    ('LED Strip 5m RGB', 55.00, 'Gadgets'),
    ('Bluetooth Speaker', 180.00, 'Gadgets'),
    ('Digital Clock Display', 90.00, 'Gadgets'),
    ('Mini Projector', 800.00, 'Gadgets'),
    ('Streaming Microphone', 350.00, 'Gadgets'),
    ('Green Screen', 150.00, 'Gadgets'),
    ('Air Purifier USB', 100.00, 'Gadgets'),
    ('Desk Fan USB', 40.00, 'Gadgets'),
    ('Hand Warmer USB', 25.00, 'Gadgets'),
    ('Digital Thermometer', 30.00, 'Gadgets'),
    ('Smart Light Bulb', 45.00, 'Gadgets'),
    ('Portable Monitor 15', 700.00, 'Gadgets'),
    ('eBook Reader', 500.00, 'Gadgets'),
    ('Drawing Tablet', 600.00, 'Gadgets'),
    ('VR Headset', 1200.00, 'Gadgets'),
    ('Fitness Tracker', 200.00, 'Gadgets'),
    ('Smart Watch', 350.00, 'Gadgets'),
    ('Noise Machine', 80.00, 'Gadgets'),
    ('A4 Paper Box 5000', 120.00, 'Supplies'),
    ('Sticky Notes Pack', 15.00, 'Supplies'),
    ('Pen Set Premium', 40.00, 'Supplies'),
    ('Marker Set 12', 25.00, 'Supplies'),
    ('Binder Clips Box', 10.00, 'Supplies'),
    ('Folders Pack 50', 30.00, 'Supplies'),
    ('Ink Cartridge Black', 80.00, 'Supplies'),
    ('Ink Cartridge Color', 95.00, 'Supplies'),
    ('Toner Cartridge', 200.00, 'Supplies'),
    ('Label Printer Tape', 35.00, 'Supplies'),
    ('Stapler Heavy Duty', 50.00, 'Supplies'),
    ('Paper Shredder', 300.00, 'Supplies'),
    ('Desk Organizer', 60.00, 'Supplies'),
    ('Planner 2025', 45.00, 'Supplies'),
    ('Whiteboard Markers 8', 20.00, 'Supplies'),
    ('Eraser Board', 12.00, 'Supplies'),
    ('Tape Dispenser', 18.00, 'Supplies'),
    ('Scissors Professional', 22.00, 'Supplies'),
    ('Glue Sticks Pack', 8.00, 'Supplies'),
    ('Rubber Bands Box', 5.00, 'Supplies'),
]

start_date = date(2024, 1, 1)
end_date = date.today()
total_days = (end_date - start_date).days

customers = []
for i in range(500):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first.lower()}.{last.lower()}{i}@email.com"
    reg_offset = random.randint(0, int(total_days - 7))
    reg_date = start_date + timedelta(days=reg_offset)
    customers.append((first, last, email, reg_date))

sales = []
for i in range(1000):
    cust_index = random.randint(0, 499)
    cust_reg_date = customers[cust_index][3]
    days_available = (end_date - cust_reg_date).days
    if days_available < 1:
        days_available = 1
    sale_offset = random.randint(1, days_available)
    sale_date = cust_reg_date + timedelta(days=sale_offset)

    prod_index = random.randint(0, len(products) - 1)
    quantity = random.randint(1, 5)
    price = products[prod_index][1]
    total = round(price * quantity, 2)

    sales.append((cust_index + 1, prod_index + 1, quantity, sale_date, total))

with open('database/init.sql', 'w') as f:
    f.write("-- Database schema and seed data for AI Data Analytics Dashboard\n\n")

    f.write("""CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);\n\n""")

    f.write("""CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'RON',
    category VARCHAR(50)
);\n\n""")

    f.write("""CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL
);\n\n""")

    f.write("-- Customers (500)\n")
    f.write("INSERT INTO customers (first_name, last_name, email, created_at) VALUES\n")
    for i, (first, last, email, reg_date) in enumerate(customers):
        comma = "," if i < len(customers) - 1 else ";"
        f.write(f"('{first}', '{last}', '{email}', '{reg_date}'){comma}\n")

    f.write("\n-- Products (100)\n")
    f.write("INSERT INTO products (name, price, currency, category) VALUES\n")
    for i, (name, price, category) in enumerate(products):
        comma = "," if i < len(products) - 1 else ";"
        f.write(f"('{name}', {price}, 'RON', '{category}'){comma}\n")

    f.write("\n-- Sales (1000)\n")
    f.write("INSERT INTO sales (customer_id, product_id, quantity, sale_date, total_amount) VALUES\n")
    for i, (cust_id, prod_id, qty, s_date, total) in enumerate(sales):
        comma = "," if i < len(sales) - 1 else ";"
        f.write(f"({cust_id}, {prod_id}, {qty}, '{s_date}', {total}){comma}\n")

    f.write("\n-- Performance indexes\n")
    f.write("CREATE INDEX idx_sales_customer_id ON sales(customer_id);\n")
    f.write("CREATE INDEX idx_sales_product_id ON sales(product_id);\n")
    f.write("CREATE INDEX idx_sales_sale_date ON sales(sale_date);\n")
    f.write("CREATE INDEX idx_products_category ON products(category);\n")

print("init.sql generated: 500 customers, 100 products, 1000 sales")
print("All sales dates are chronologically after customer registration dates.")