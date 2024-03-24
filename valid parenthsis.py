s='()'
def valid(s):
    stack=[]
    dit={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for i in s:
        if i in dict:
            if stack and stack[-1]==dit[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

