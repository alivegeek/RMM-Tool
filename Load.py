import csv
import Customers
customer = Customers.Customer
masterWanList = []


# Loads data from a csv file
def load():
    with open('hosts.csv', "r", ) as f:
        csv_file = csv.DictReader(f)
        for row in csv_file:
            _customer = Customers.Customer(row['Name'], row['Host'])
            masterWanList.append(_customer)
    return masterWanList


