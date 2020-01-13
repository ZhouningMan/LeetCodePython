from random import randrange

class LoadBalancer:
    def __init__(self):
        self.machine_map = {}
        self.machine_list = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id in self.machine_map.keys():
            return
        idx = len(self.machine_list)
        self.machine_list.append(server_id)
        self.machine_map[server_id] = idx

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id not in self.machine_map.keys():
            return
        idx = self.machine_map.pop(server_id)
        last_server_id = self.machine_list.pop()
        # if the last server is the one we want remove, do nothing
        if last_server_id == server_id:
            return
        self.machine_list[idx] = last_server_id
        self.machine_map[last_server_id] = idx

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        i = randrange(len(self.machine_list))
        return self.machine_list[i]