"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    Example 1:
        Input: s = "()"
        Output: true
    Example 2:
        Input: s = "()[]{}"
        Output: true
    Example 3:
        Input: s = "(]"
        Output: false
    Example 4:
        Input: s = "([])"
        Output: true
            Constraints:
            1 <= s.length <= 104
            s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    stack = []
    mapping = {
                ')': '(',
                '}': '{',
                ']': '['
            }

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


def anotherWay_IsValid(s = str) -> bool:
    pairs = {
                ")" : "(",
                "]" : "[",
                "}" : "{"
            }
    stack = []
    
    for char in s:
        if char in pairs.values(): # If is open character
            stack.append(char)
        elif char in pairs.keys(): # If is close character
            # Verify if the stack isn't empty and the top of the stack
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
        else:
            return False
        
    return not stack

if isValid("()[]{}"):
    print("true")
else:
    print("false")


if anotherWay_IsValid("{([])}"):
    print("true")
else:
    print("false")
