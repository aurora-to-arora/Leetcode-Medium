class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[""]
        for c in s:
            temp=[]
            if c.isalpha():
                for r in res:
                    temp.append(r+c.lower())
                    temp.append(r+c.upper())
            else:
                for r in res:
                    temp.append(r+c)
            res=temp

        return res


#or

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def bkt(sub='', i=0):
            if len(sub)==len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    bkt(sub+s[i].swapcase(), i+1)
                bkt(sub+s[i], i+1)
        res=[]
        bkt()
        return res


                
