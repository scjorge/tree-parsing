import json

from tree_workflow.tree import Tree

lst = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]


def test_tree_from_list():
    tr = Tree()
    tree = tr.tree_from_list(lst)
    print(json.dumps(tree))


def test_list_from_tree():
    tr = Tree()
    tree = tr.tree_from_list(lst)
    lista = tr.list_from_tree(tree)
    print(json.dumps(lista))
