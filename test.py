from transformData import *

transformData("data.json","test_data.json")

test = FormattedData("data-transformed.json")

print("Total Revenue:")
print(test.totalRevenue())

print("Vendor With Most Revenue:")
print(test.highestRevenueVendor())

print("Quantity of Hats Sold:")
print(test.howManySold("hat"))

print("ID of Customer that bought the most ice in October:")
print(test.mostItemInMonthID("ice","08"))