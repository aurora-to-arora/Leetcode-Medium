class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # prune impossible lengths
        if len(s) < 4 or len(s) > 12:
            return res
        
        def backtrack(start, dots, path):
            if dots == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for end in range(start, min(start + 3, len(s))):
                segment = s[start:end+1]

                # too large
                if int(segment) > 255:
                    break

                # leading zero
                if segment[0] == "0" and len(segment) > 1:
                    break

                backtrack(end + 1, dots + 1, path + [segment])

        backtrack(0, 0, [])
        return res
