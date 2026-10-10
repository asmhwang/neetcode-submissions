class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {'+','-','*','/'}
        for a in tokens:
            if a not in ops:
                stack.append(int(a))
            else:
                f = stack.pop()
                s = stack.pop()
                if a=="+":
                    stack.append(f+s)
                elif a=='-':
                    stack.append(s-f)
                elif a=="*":
                    stack.append(f*s)
                else:
                    stack.append(int(s/f))
        return stack.pop()