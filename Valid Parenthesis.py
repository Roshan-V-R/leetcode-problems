def Valid(s):
    stack = []
    mapping = {'}':'{',']':'[',')':'('}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return not stack

print(Valid("{[]}"))