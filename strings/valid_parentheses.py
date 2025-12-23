def is_valid_parentheses(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in pairs:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False
        else:
            stack.append(ch)

    if len(stack) == 0:
        return True
    return False


# Sample test cases
print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))
