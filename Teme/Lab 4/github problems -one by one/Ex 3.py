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
