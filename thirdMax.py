class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = None

        for n in nums:
            if n == m1 or n == m2 or n == m3:
                continue  # skip duplicates

            if m1 is None or n > m1:
                m3 = m2
                m2 = m1
                m1 = n
            elif m2 is None or n > m2:
                m3 = m2
                m2 = n
            elif m3 is None or n > m3:
                m3 = n

        return m3 if m3 is not None else m1
