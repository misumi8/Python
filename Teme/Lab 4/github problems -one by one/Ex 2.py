# 2 ---------------------------------------------------

def solve_expr(expr):
    delims = "+-*/"
    operations = []
    for i in expr:
        if(i in "+-*/"):
            operations.append(i)
    for delim in delims:
        expr = " ".join(expr.split(delim))
    numbers = expr.split()
    expr_list_form = [numbers[0]]

    for i in range(0, len(numbers) - 1):
        expr_list_form.append(operations[i])
        expr_list_form.append(numbers[i + 1])

    i = 0
    while i < len(expr_list_form):
        if expr_list_form[i] == "*":
            expr_list_form[i - 1] = int(expr_list_form[i - 1]) * int(expr_list_form[i + 1])
            del expr_list_form[i:i + 2]
            i -= 1
        elif expr_list_form[i] == "/":
            expr_list_form[i - 1] = int(expr_list_form[i - 1]) / int(expr_list_form[i + 1])
            del expr_list_form[i:i + 2]
            i -= 1
        else:
            i += 1
    i = 0
    while i < len(expr_list_form):
        if expr_list_form[i] == "+":
            expr_list_form[i - 1] = int(expr_list_form[i - 1]) + int(expr_list_form[i + 1])
            del expr_list_form[i:i + 2]
            i -= 1
        elif expr_list_form[i] == "-":
            expr_list_form[i - 1] = int(expr_list_form[i - 1]) - int(expr_list_form[i + 1])
            del expr_list_form[i:i + 2]
            i -= 1
        else:
            i += 1

    return expr_list_form

# print(solve_expr("4+17-9*2+16/4"))
# print(solve_expr("121*2+15*6-20-21+4-3*4*2"))
# print(solve_expr("36/6+5*2-8-4-2*2+2"))
