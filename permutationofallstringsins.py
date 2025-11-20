#User function Template for python3


class Solution:

    def permutation(self, s):
        # code here
        res=[]
        def bakt(i,path):
            if i == len(s):
                res.append(path)
                return
            bakt(i+1,path+s[i])
            bakt(i+1, path+" "+s[i])
        bakt(1, s[0])
        res.sort()
        return res
