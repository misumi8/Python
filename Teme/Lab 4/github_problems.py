# 1 ---------------------------------------------------
from pprint import pprint


def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    return b

# print(fib(2000))

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

# 3 ---------------------------------------------------

def create_bst(elems):
    bst = [elems[0], [], []]
    for elem in elems[1:]:
        if(elem < bst[0]):
            bst[1] = bst_insert(bst[1], elem)
        else:
            bst[2] = bst_insert(bst[2], elem)
    return bst

def bst_insert(node, elem):
    # print("bst_insert_l", node, elem)
    if (len(node) == 0):
        node = [elem, [], []]
    else:
        if(elem < node[0]):
            node[1] = bst_insert(node[1], elem)
        else:
            node[2] = bst_insert(node[2], elem)
    return node


def print_bst(tree, jump, subtree = "RT --- "):
    if not tree:
        return
    root = tree[0]
    left = tree[1]
    right = tree[2]
    print(" " * jump + subtree + str(root))
    if left:
        print_bst(left, jump + 6, "L --- ")
    if right:
        print_bst(right, jump + 6, "R --- ")

def inord_bst(tree):
    if not tree:
        return []
    return inord_bst(tree[1]) + [tree[0]] + inord_bst(tree[2])

# bst = create_bst([50,30,70,20,40,60,80,10,90,5,100,2,7,1,3])
# print_bst(bst, 0)
# print(inord_bst(bst))

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

# 5 ---------------------------------------------------

import struct

def bmp_text_form(bmp):
    with open(bmp, "rb") as f:
        data = f.read(14)
        # I - int, H - short, < - little endian
        header = struct.unpack("<2sIHHI", data)
        print("File size:", header[1])

        dib_header = f.read(40)
        dib_header_unpacked = struct.unpack("<IIIHHIIIIII", dib_header)
        print("Image width (pixel):", dib_header_unpacked[1])
        print("Image height (pixel):", dib_header_unpacked[2])
        print("Bits per pixel:", dib_header_unpacked[4])
        print("Image size:", dib_header_unpacked[6])

        print("\nImage data (1%): ")
        image_size = dib_header_unpacked[6]
        # move cursor to header[3] bytes
        f.seek(header[3])
        pixel_array = f.read(image_size // 100)
        pprint(" ".join([hex(byte).removeprefix("0x").zfill(2).upper() for byte in pixel_array]))

# bmp_text_form("python.bmp")
