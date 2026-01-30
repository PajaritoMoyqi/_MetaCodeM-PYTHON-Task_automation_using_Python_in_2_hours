import openpyxl
import random

# Make new excel file
wb = openpyxl.Workbook()

# Select activated current sheet
ws = wb.active

# Change sheet name
ws.title = 'Orders'

# Add headers
ws.append(["Number", "Category", "Price", "Amount", "Total"])

# Product list
product_list = ["Keyboard", "Mouse", "USB", "Earphone"]

for i in range(random.randint(5, 10)):
  name = random.choice(product_list)
  price = random.randrange(10000, 101000, 1000)
  ws.append([i+1, name, price, random.randint(1, 5), f'=C{i+2}*D{i+2}'])

# Save the file
wb.save("Orders.xlsx")