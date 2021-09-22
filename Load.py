import csv
import Customers
customer = Customers.Customer
masterWanList = []
listOfUrls = []

# Loads data from a csv file
def load():
    with open('hosts.csv', "r", ) as f:
        csv_file = csv.DictReader(f)
        for row in csv_file:
            _customer = Customers.Customer(row['Name'], row['Host'])
            masterWanList.append(_customer)
    return masterWanList



def loadWebsites():
    with open('WebsiteURLs.csv', "r",) as f:
        csv_file = csv.reader(f)
        for row in csv_file:
            listOfUrls.append(row)
    return listOfUrls


if __name__ == "__main__":
    pass