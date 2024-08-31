class Solution(object):
    def findRelativeRanks(self, score):
        indexed_scores = [(s, i) for i, s in enumerate(score)]
        indexed_scores.sort(reverse=True, key=lambda x: x[0])
        ranks = [""] * len(score)
        
        for rank, (s, i) in enumerate(indexed_scores):
            if rank == 0:
                ranks[i] = "Gold Medal"
            elif rank == 1:
                ranks[i] = "Silver Medal"
            elif rank == 2:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(rank + 1)
        
        return ranks
        