def isValid(s):
    pairs = { ")":"(", 
             "]":"[", 
             "}":"{"}
    stack = []
    for character in s:
        if character in pairs: #this is a closed bracket
            if stack and stack[-1] == pairs[character]:
                stack.pop()
            else:
                return False
        else: #this is an open bracket
            stack.append(character)
    if stack:
        return False
    else: 
        return True