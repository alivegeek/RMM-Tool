import Report
from Load import load
import Customers
import Ping
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#vars
pingsBeforeDown = 10
masterWanList = load()
wanIsDownMessage = ""
teams = Report.SendToTeams.send

def testCSV():
    for each in masterWanList:
        print(each.name() + " " + each.wanIP())


def healthCheck(host):
    ping = Ping.ping(str(host.wanIP()))
    if ping is False:
        for x in range(pingsBeforeDown):
            print("Retry.." + str(x + 1) + " of " + str(pingsBeforeDown))
            if Ping.ping(str(host.wanIP())) is True:
                host.lastReport(now)
                return
            elif x >= pingsBeforeDown - 1:
                host.setState("Down")
                host.setLastReport(now)
                teams(str(host.name()) + "is down at " + str(dt_string))

if __name__ == "__main__":
    #initFromCSV()

    while True:
        for each in masterWanList:
            healthCheck(each)



