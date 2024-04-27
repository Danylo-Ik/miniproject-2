"""calculator"""
def calculate_expression(expression:str)-> int:
    """
    str -> int
    create a program that will calculate string expressions 

    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    """
    operators = ('+', '-', '*', '/')
    operators_ = None
    count = 0
    wrong = 'Неправильний вираз!'

    if isinstance(expression, str):
        expression = expression.replace("відняти", "-")
        expression = expression.replace('мінус', '-')
        expression = expression.replace('додати','+')
        expression = expression.replace('помножити на','*')
        expression = expression.replace('поділити на','/')
        expression = expression.replace('Скільки буде', '')
        expression = expression.replace('?', ' ')

        exp_s = expression.split()
        if len(exp_s) > 1:
            if exp_s[-1] == '+' or exp_s[-1] == '-' or exp_s[-1] == '*' or\
                exp_s[-1] == '/' or expression[-1] !=' ' or exp_s[1] in operators and\
                exp_s[2] in operators or exp_s[1] not in operators:
                return wrong
        else:
            return int(exp_s[-1]) if exp_s != [] else wrong

        for exp in exp_s:
            if exp in operators:
                operators_ = exp
            else:
                num = int(exp)

                if operators_ is None:
                    count = num
                if operators_ == '+':
                    count += num
                if operators_ == '-':
                    count -= num
                if operators_ == '*':
                    count *= num
                if operators_ == '/':
                    if num == 0:
                        return wrong
                    count //= num

        return count
    else:
        return wrong
