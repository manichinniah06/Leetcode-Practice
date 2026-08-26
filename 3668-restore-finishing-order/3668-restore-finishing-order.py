class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        index = {}

        for i in friends:
            for j in range(len(order)):
                if order[j] == i:
                    index[i] = j

        sorted_index = sorted(index.items(), key=lambda x: x[1])

        return [x[0] for x in sorted_index]
        

