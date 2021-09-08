from Load import load
import Customers

#vars

masterWanList = load()

for each in masterWanList:
    print(each.name() + " " + each.wanIP())
