class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                a = stk.pop()
                b = stk.pop()

                if t == "+":
                    stk.append(b + a)
                elif t == "-":
                    stk.append(b - a)
                elif t == "*":
                    stk.append(b * a)
                else:  # division
                    stk.append(int(b / a))  # truncate toward zero
            else:
                stk.append(int(t))

        return stk[-1]
