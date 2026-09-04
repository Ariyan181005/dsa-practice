class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        for i in range(len(expression)):
            if expression[i] in "+-*":                
                lt = self.diffWaysToCompute(expression[:i])
                rt = self.diffWaysToCompute(expression[i + 1:])                
                for a in lt:
                    for b in rt:                        
                        if expression[i] == '+':
                            ans.append(a + b)
                        elif expression[i] == '-':
                            ans.append(a - b)
                        else:
                            ans.append(a * b)
        if not ans:
            ans.append(int(expression))
        return ans