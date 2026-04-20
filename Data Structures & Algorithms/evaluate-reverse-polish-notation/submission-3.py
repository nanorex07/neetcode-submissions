class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []

        for token in tokens:
            if token in {"+", "-", "/", "*"}:
                a = op_stack.pop()
                b = op_stack.pop()
                val = a*b
                if token == "+":
                    val = b+a
                elif token == "/":
                    val = int(b/a)
                elif token == "-":
                    val = b-a
                op_stack.append(val)
            else:
                op_stack.append(int(token))
        return int(op_stack[-1])