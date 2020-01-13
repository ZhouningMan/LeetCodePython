class HeartBeat:

    def __init__(self):
        self.ip_to_last_ping = {}
        self.k = -1
    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """

    def initialize(self, slaves_ip_list, k):
        for ip in slaves_ip_list:
            self.ip_to_last_ping[ip] = 0
        self.k = k
    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """

    def ping(self, timestamp, slave_ip):
        if slave_ip in self.ip_to_last_ping:
            self.ip_to_last_ping[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """

    def getDiedSlaves(self, timestamp):
        corpses = []
        for ip, last in self.ip_to_last_ping.items():
            if timestamp - last >= 2 * self.k:
                corpses.append(ip)
        return corpses