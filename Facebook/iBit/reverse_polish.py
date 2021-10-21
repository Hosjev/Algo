class Solution:
    # @param A : list of strings
    # @return int
    def evalRPN(self, A):
        # Edge Case(s)

        # Prime
        idx = 0
        operators = set('-+*/')
        stack = []
        import math

        # Main - this rhythm (pull operands off by 2) allows
        #        us to organically use an operator in its nested order
        while not idx == len(A):
            item = A[idx]
            if item in operators:
                right = eval(stack.pop())
                left = eval(stack.pop())
                if item == "/":
                    #  dividend / divisor
                    div = (left / right)
                    # Negative number, b/c floor technically does right thing
                    if div < 0:
                        item = round(div)
                    else:
                        item = math.floor(div)
                else: item = eval(f'{left} {item} {right}') # >= 3.6
            stack.append(str(item))
            idx += 1

        return stack[0]


A = ["2", "1/4", "+", "3", "*"]
#A = ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
A = ["2", "2", "/"]
A = ["4","-2","/","2","-3","-","-"] # -7
A = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22
print(Solution().evalRPN(A))
