def check_expression(exp):
    stack = []
    for i in exp:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if not stack:
                return False
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
