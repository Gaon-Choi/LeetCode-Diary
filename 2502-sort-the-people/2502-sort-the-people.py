class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []

        for i in range(len(names)):
            arr.append((names[i], heights[i]))
        
        arr.sort(key = lambda x : -x[1])

        return [x[0] for x in arr]