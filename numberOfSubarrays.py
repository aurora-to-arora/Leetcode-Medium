class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0
        result = 0

        for n in nums:
            prefix += (n%2)

            if prefix-k in count:
                result += count[prefix-k]
            count[prefix] = count.get(prefix,0)+1
        return result
