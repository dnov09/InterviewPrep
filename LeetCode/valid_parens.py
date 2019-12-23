'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''


def isValid(s):
    # the stack will keep track of all our open parens
    stack = []
    # if the value is an open paren, append to stack
    for char in s:
        if isOpen(char):
            stack.append(char)
        # else pop the top value and check
            # to see if it matches a close paren
        else:
            # if the list has one paren we will popping an empty list
            if len(stack) == 0:
                return False

            top_val = stack.pop()
            close_paren = char
            if not matches(top_val, close_paren):
                return False
    return len(stack) == 0


def isOpen(char):
    open_parens = ['[', '{', '(']
    if char in open_parens:
        return True
    return False


def matches(op, cl):
    parens = {'{': '}', '[': ']', '(': ')'}
    # check if the open paren matches the close paren
    for k, v in parens.items():
        # if they do return True
        if op == k and cl == v:
            return True
    # return false
    return False


print("First test: ", isValid("([{({})}])"))
print("Second test: ", isValid("()[]"))
print("Third test: ", isValid("()[]{"))
print("Fourth test: ", isValid("()[]"))
print("Fifth test: ", isValid("]"))

