def answer(question):
    if not question.startswith('What is') or not question.endswith('?'):
        raise ValueError("unknown operation")
    question = question[8:-1]

    question = question.replace('plus', '+')
    question = question.replace('minus', '-')
    question = question.replace('multiplied by', '*')
    question = question.replace('divided by', '/')
    question = question.replace('raised to the', '^')
    question = question.replace('th power', '')
    question = question.replace('nd power', '')
    question = question.replace('rd power', '')
    question = question.split(' ')
    
    try:
        res = int(question[0])
    except:
        raise ValueError("syntax error")
    operators = {'+', '-', '*', '/', '^'}
    operator_bool = True
    operator = ''
    
    for item in question[1:]:
        if operator_bool:
            if item not in operators:
                try:
                    int(item)
                except:
                    raise ValueError("unknown operation")
                raise ValueError("syntax error")   
            else:
                operator = item
                operator_bool = not operator_bool
        else:
            try:
                num = int(item)
            except:
                raise ValueError("syntax error")
            if operator == '+':
                res += num
            elif operator == '-':
                res -= num
            elif operator == '*':
                res *= num
            elif operator == '/':
                res /= num
            else:
                res = pow(res, num)
            operator_bool = not operator_bool
    if not operator_bool:
        raise ValueError("syntax error")
    return res
