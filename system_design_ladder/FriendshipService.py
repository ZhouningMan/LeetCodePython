class FriendshipService:

    def __init__(self):
        self.user_followings = {}
        self.user_followers = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """

    def getFollowers(self, user_id):
        return sorted(self.user_followers.get(user_id, set()))

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """

    def getFollowings(self, user_id):
        return sorted(self.user_followings.get(user_id, set()))

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, to_user_id, from_user_id):
        followings = self.user_followings.get(from_user_id, set())
        followings.add(to_user_id)
        self.user_followings[from_user_id] = followings
        followers = self.user_followers.get(to_user_id, set())
        followers.add(from_user_id)
        self.user_followers[to_user_id] = followers

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, to_user_id, from_user_id):
        followings = self.user_followings.get(from_user_id, set())
        if to_user_id in followings:
            followings.remove(to_user_id)
        self.user_followings[from_user_id] = followings
        followers = self.user_followers.get(to_user_id, set())
        if from_user_id in followers:
            followers.remove(from_user_id)
        self.user_followers[to_user_id] = followers

