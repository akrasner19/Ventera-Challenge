import json

#Function to transform the data into the new format
def transformData(jsonFileName, outputFileName):
	with open(jsonFileName, 'r') as content:
		jdata = content.read()
		data = json.loads(jdata)
		fixedData = []
		for element in data:
			fixedElement = {}
			fixedElement["id"] = element["id"]
			fixedElement["vendor"] = element["vendor"]
			fixedElement["date"] = element["date"]
			fixedElement["customerId"] = element["customer"]["id"]
			fixedElement["order"] = []
			for key in element["order"].keys():
				item = {}
				item["item"] = key
				item["quantity"] = element["order"][key]["quantity"]
				item["price"] = element["order"][key]["price"]
				item["revenue"] = item["quantity"]*item["price"]
				fixedElement["order"].append(item)
			fixedData.append(fixedElement)

		with open(outputFileName, 'w') as outFile:
			outFile.write(json.dumps(fixedData, indent=1))

#A class that contains the data from a the json
#allows for access to the underlying data for answering as well as the ability to ex
class FormattedData:
	def __init__(self, jsonFileName):
		with open(jsonFileName, 'r') as content:
			jdata = content.read()
			self.data = json.loads(jdata)
			#Technically the access time for each piece of data could be faster if all of
			#the relevant questions were calculated here in advance. However, this limits the
			#scalability of the solution.

	def howManySold(self, itemname):
		total = 0
		for element in self.data:
			for item in element["order"]:
				if item["item"] == itemname:
					total += item["quantity"]
					break
		return total

	def totalRevenue(self):
		total = 0
		for element in self.data:
			for item in element["order"]:
				total += item["revenue"]
		return total

	def highestRevenueVendor(self):
		vendors = {}
		for element in self.data:
			if not element["vendor"] in vendors:
				vendors[element["vendor"]] = 0
			for item in element["order"]:
				vendors[element["vendor"]] += item["revenue"]

		bestRev = 0
		bestVen = None
		for key in vendors.keys(): #brute force, could be solved faster given more time
			if vendors[key] > bestRev:
				bestRev = vendors[key]
				bestVen = key

		return bestVen

	def mostItemInMonthID(self,itemStr,monthStr):
		customers = {}
		for element in self.data:
			date = element["date"].split('/')
			if date[0] == monthStr:
				if not element["customerId"] in vendors:
					customers[element["customerId"]] = 0
				for item in element["order"]:
					if item["item"] == itemStr:
						customers[element["customerId"]] += item["quantity"]
						break

		bestQuant = 0
		bestCust = None
		for key in customers.keys(): #brute force, could be solved faster given more time
			if customers[key] > bestQuant:
				bestQuant = customers[key]
				bestCust = key

		return bestCust