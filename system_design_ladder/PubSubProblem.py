'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''

class PushNotification:
    @classmethod
    def notify(user_id, message):
        pass

class PubSubPattern:
    def __init__(self):
        self.subscription = {}

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def subscribe(self, channel, user_id):
        if channel not in self.subscription:
            self.subscription[channel] = set()
        self.subscription[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
        if channel not in self.subscription:
            return
        if user_id in self.subscription[channel]:
            self.subscription[channel].remove(user_id)

    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """
    def publish(self, channel, message):
        if channel not in self.subscription:
            return
        for user_id in self.subscription[channel]:
            PushNotification.notify(user_id, message)