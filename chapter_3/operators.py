from pythonds.basic.stack import Stack

print(Stack)


def infixToPostfix(infixexpr):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    print(tokenList)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix('5 * 3 ** ( 4 - 2 )'))


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def infixEvaluator(exp):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    operatorStack = Stack()
    operandStack = Stack()
    tokenList = exp.split()

    for token in tokenList:
        if token == '(':
            operatorStack.push(token)
        elif token == ')':
            topToken = operatorStack.pop()
            while topToken != '(':
                arg2 = operandStack.pop()
                arg1 = operandStack.pop()
                result = doMath(topToken, arg1, arg2)
                operandStack.push(result)
                topToken = operatorStack.pop()
        else:
            try:
                precedence = prec[token]
            except KeyError:
                operandStack.push(float(token))
            else:
                while (not operatorStack.isEmpty()) and \
                        (prec[operatorStack.peek()] >= precedence):
                    operator = operatorStack.pop()
                    arg2 = operandStack.pop()
                    arg1 = operandStack.pop()
                    result = doMath(operator, arg1, arg2)
                    operandStack.push(result)
                operatorStack.push(token)

    print(operatorStack, operandStack)
    while not operatorStack.isEmpty():
        operator = operatorStack.pop()
        arg2 = operandStack.pop()
        arg1 = operandStack.pop()
        result = doMath(operator, arg1, arg2)
        operandStack.push(result)
    if(operandStack.size() != 1):
        print('error')
    else:
        return operandStack.pop()


print(infixEvaluator('2 + 2'))
print(infixEvaluator('2 + 2 * 3'))
print(infixEvaluator('( 2 + 2 ) * 3'))
print(infixEvaluator('2 * ( 2 + 2 ) * 3 + 1'))
print(infixEvaluator('1 + ( 2 * ( 2 + 2 ) * 3 + 1 )'))
