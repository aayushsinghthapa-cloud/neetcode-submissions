class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for k in tokens:
            if not (k == "+" or k == "-" or k == "*" or k == "/"):
                stack.append(int(k))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if k == "+":
                    stack.append(num1 + num2)
                elif k == "-":
                    stack.append(num1 - num2)
                elif k == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return stack[0]

