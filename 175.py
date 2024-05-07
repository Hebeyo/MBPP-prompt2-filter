def is_valid_parenthese(s):
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif i == '}' and stack and stack[-1] == '{':
            stack.pop()
        elif i == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return stack == []
