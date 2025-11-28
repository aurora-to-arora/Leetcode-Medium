class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=sorted(strs)

        first=s[0]
        last=s[-1]

        n = min(len(first), len(last))
        ans=''
        for i in range(n):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]

        return ans
