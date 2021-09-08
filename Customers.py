import ipaddress
class Customer():
    # Variables
    data = []

    #init
    def __init__(self, name, wanIP):

        #validate state
        #if state is not True or False or None:
            #raise ValueError("Must be True False or NULL")
        #handle incorrectly formatted IPs
        try:
            ipaddress.ip_address(wanIP)
        except:
            ValueError("WAN IP Address must be in CIDR notation i.e. 0.0.0.0")

        self._name = name
        self._wanIP = wanIP
        lastReport = ""
        state = ""

    def name(self):
        return self._name

    def wanIP(self):
        return self._wanIP

    def lastReport(self):
            return self._lastReport

    def state(self):
        return self._state

    def add(self, name, wanIP):
        self.data.extend((name, wanIP))

