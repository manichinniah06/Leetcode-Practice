class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}

        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        return [item[0] for item in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:k]]
            

        