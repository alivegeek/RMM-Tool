from Load import load
import Customers

#vars
#loadHosts = Load.Load
#list of customer objects
masterWanList = load()

for each in masterWanList:
    print(each.name())
