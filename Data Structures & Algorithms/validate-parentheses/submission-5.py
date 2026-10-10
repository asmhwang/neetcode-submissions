class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a==']':
                if not stack or stack[-1]!='[':
                    return False
                stack.pop()    
            elif a=='}':
                if not stack or stack[-1]!='{':
                    return False
                stack.pop() 
            elif a==')':
                if not stack or stack[-1]!='(' :
                    return False
                stack.pop() 
            else:
                stack.append(a)
        return not stack