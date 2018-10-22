# Ventera Developer Challenge

My solution is in the file transformData.py. It is written in Python 3

The function transformData takes in a string as the location of the old json, and a string as the location for the new json.
Calling this function will generate a json file that follows the solution instructions.

Next with what extra time I had, I completed the second story from the problem.
I structured this solution as a class to make it more scalable and modular. I also made the solutions able to answer broader queries than just the ones that were asked.

Call the class method howManySold(itemname) with the parameter of the name of the item you want the data on

Calling the method totalRevenue() will return the total revenue of all the elements

highestRevenueVendor() Gives the vendor from the data with the highest revenue

mostItemInMonthID(itemStr,monthStr) returns the customer ID of whoever bought the most of a specific item in a specific month

All of these functions are demonstrated in test.py