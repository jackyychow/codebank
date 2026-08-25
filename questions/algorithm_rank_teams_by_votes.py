# Question: Rank teams from voting strings with deterministic tie-breaking.
#

from typing import List
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        scoreboard=defaultdict(lambda: [0] * 26)

        for vote in votes:
            for rank, team in enumerate(vote):
                scoreboard[team][rank]+=1

        temp_arr=[]
        for k,v in scoreboard.items():
            temp_arr.append((v,k))
        temp_arr.sort(key=lambda x: (x[0],ord('A')-ord(x[1])),reverse=True)

        return ''.join([x[1] for x in temp_arr])