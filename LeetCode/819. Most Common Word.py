# 2021-01-27
# https://leetcode.com/problems/most-common-word/

from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        
        parag = [word for word in re.sub("[\W]", ' ', paragraph).lower().split()
                if word not in banned]
        
        parag_cnt = Counter(parag)
        
        return parag_cnt.most_common(1)[0][0]
        
