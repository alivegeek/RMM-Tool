## Checks websites for HTTP response status codes
import requests
from Load import loadWebsites
listOfURLs = loadWebsites()

def checkWebsite():
    for i in listOfURLs:
       # print(str(i).strip("[]'")  )  #
        try:
            r = requests.get("https://" + str(i).strip("[]'"))
            if r.status_code == 200:
                pass
            else:
                print(r + " may be down")

        except:
            print(str(i) + " is down")
        #print(listOfURLs[])

if __name__ == "__main__":
    checkWebsite()
