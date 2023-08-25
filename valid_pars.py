# Input: s = "()[]{}"
# Output: true
import re
s = "()[]{}()()"

def isValid(str):
    stack_open = []
    stack_close = []
    for char in str:
        if char == '(' or char == '{' or char == '[':
            stack_open.append(char)
        if char == ')' or char == '}' or char == ']':
            stack_close.append(char)
    print('open: ', stack_open)
    print('close: ', stack_close)
    validity = True
    while validity == True:
        opening = stack_open.pop()
        closing = stack_close.pop()
        if ord(closing) - ord(opening) == 1:
            continue
        else:
            validity = False
    return validity


print(isValid(s))