"""
    Deque Implementations in Python
    @Author: Federico Baù
    @Creation Date: 19 - Jan - 2021
    @Updated: N/a
    
"""


class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

s = Stack()

print(s.is_empty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

def par_checker(symbol_string):
    """Function that check if a block of Parentheses are Balanced Parentheses
        NOTE: This --> (()()()()) are balanced Parenthesis this--> ((((((()) aren't

        Reads a string of parentheses from left to right,  the most recent opening parenthesis must match the next closing symbol

        :param symbok_string (str): string of parentheses 
        :return: (bool)
    """
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()

print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False

# ------------------ Mix Type Parenthesus

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


def balance_checker(symbol_string):
    """Function that check if a block of Mix Parentheses are Balanced Parentheses
        NOTE: This --> (()()()()) are balanced Parenthesis this--> ((((((()) aren't

        Reads a string of parentheses from left to right,  the most recent opening parenthesis must match the next closing symbol

        :param symbok_string (str): string of parentheses 
        :return: (bool)
    """
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False

    return s.is_empty()


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))


# ========================= < Convertin Decimanl To binary Numbers > ========================= #

def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print(divide_by_2(42))
print(divide_by_2(31))

# ========================= < Convertin Decimanl To Any base number > ========================= #
def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_converter(25, 2))
print(base_converter(25, 16))

# ========================= < Infix, Prefix, and Postfix > ========================= #
# Reference ---> https://runestone.academy/runestone/books/published/pythonds3/BasicDS/InfixPrefixandPostfixExpressions.html

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

infix_to_postfix("( A + B ) * ( C + D )") # 'A B + C D + *'
infix_to_postfix("( A + B ) * C") # 'A B + C *'
infix_to_postfix("A + B * C") # 'A B C * +'

# ------------------- postfix_eval

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))