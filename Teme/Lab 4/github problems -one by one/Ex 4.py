# 4 ---------------------------------------------------

def create_ast(expr):
    delims = "+-*/"
    operations = []
    for i in expr:
        if (i == "+" or i == "-" or i == "*" or i == "/"):
            operations.append(i)
    for delim in delims:
        expr = " ".join(expr.split(delim))
    numbers = expr.split()

    expr_list_form = [numbers[0]]
    for i in range(0, len(numbers) - 1):
        expr_list_form.append(operations[i])
        expr_list_form.append(numbers[i + 1])
    i = 1
    while i < len(expr_list_form) - 1:
        if expr_list_form[i] in ("*", "/"):
            new_node = [expr_list_form[i], expr_list_form[i - 1], expr_list_form[i + 1]]
            expr_list_form[i - 1] = new_node
            del expr_list_form[i:i + 2]
            i -= 1
        i += 1

    i = 1
    while i < len(expr_list_form) - 1:
        if expr_list_form[i] in ("+", "-"):
            new_node = [expr_list_form[i], expr_list_form[i - 1], expr_list_form[i + 1]]
            expr_list_form[i - 1] = new_node
            del expr_list_form[i:i + 2]
            i -= 1
        i += 1
    return expr_list_form[0]

def print_ast(node, jump = 0, prefix = "RT --- "):
    if isinstance(node, list):
        print("  " * jump + prefix + node[0])
        print_ast(node[1], jump + 2, "L --- ")
        print_ast(node[2], jump + 2, "R --- ")
    else:
        print("  " * jump + "N --- " + node)

def calc_ast(ast):
    if isinstance(ast, list):
        if ast[0] == "*":
            return int(calc_ast(ast[1])) * int(calc_ast(ast[2]))
        elif ast[0] == "/":
            return int(calc_ast(ast[1])) / int(calc_ast(ast[2]))
        if ast[0] == "+":
            return int(calc_ast(ast[1])) + int(calc_ast(ast[2]))
        elif ast[0] == "-":
            return int(calc_ast(ast[1])) - int(calc_ast(ast[2]))
    else:
        return ast

# ast = create_ast("13*2-11+5+21/7")
# print(ast)
# print_ast(ast)
# print("Result:", calc_ast(ast))
