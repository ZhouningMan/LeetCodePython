'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

from collections import defaultdict
import heapq

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        if not results:
            return {}
        id_to_scores = defaultdict(list)
        for st in results:
            id_to_scores[st.id].append(st.score)
        ans = {}
        for id, scores in id_to_scores.items():
            if len(scores) < 5:
                continue
            average = self.calc_average(scores)
            ans[id] = average
        return ans

    def calc_average(self, scores):
        top_k = []
        for s in scores:
            heapq.heappush(top_k, s)
            if len(top_k) > 5:
                heapq.heappop(top_k)
        return sum(top_k) / 5