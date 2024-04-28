def check_brackets(expression):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in matching_bracket.values():
           
            stack.append(char)
        elif char in matching_bracket:
            
            if not stack or stack.pop() != matching_bracket[char]:
                return "Несиметрично"
    
    
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


expressions = {
    "( ){[ 1 ]( 1 + 3 )( ){ }}": "( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично",
    "( 23 ( 2 - 3);": "( 23 ( 2 - 3);: Несиметрично",
    "( 11 }": "( 11 }: Несиметрично"
}

for exp, result in expressions.items():
    print(f"{exp}: {check_brackets(exp)}")