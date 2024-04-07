def evaluate_expression(n, tokens):
    stack = []
    
    def apply_operation():
        b = stack.pop()
        op = stack.pop()
        a = stack.pop()
        if op == '+':
            stack.append(a + b)
        elif op == '-':
            stack.append(a - b)
        elif op == '*':
            stack.append(a * b)
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ['+', '-', '*']:
            while stack and stack[-1] in ['+', '-', '*'] and (token == '*' or (token in ['+', '-'] and stack[-1] in ['+', '-'])):
                apply_operation()
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-2] != '(':

                apply_operation()
            stack.pop(0)
    
    while len(stack) > 1:
        apply_operation()
    
    return stack[0] % (10 ** 9 + 7)

n = int(input())
tokens = input().split()

result = evaluate_expression(n, tokens)
print(result)