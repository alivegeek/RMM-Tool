## Checks websites for HTTP response status codes
import requests
from Load import loadWebsites
listOfURLs = loadWebsites()

def checkWebsite(url):
    # for i in listOfURLs:
    #    # print(str(i).strip("[]'")  )  #
    try:
        r = requests.get(url)

  #  r = requests.get("https://" + str(i).strip("[]'"))
        if r.status_code == 200:
            return True
        else:
            return False

    except:
        return False
        #print(url + " is down")
        #print(listOfURLs[])

if __name__ == "__main__":
    checkWebsite()
