class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        output = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for i in range(k):
            most_frequent = max(freq, key=freq.get)
            output.append(most_frequent)
            freq[most_frequent] = -1

        return output