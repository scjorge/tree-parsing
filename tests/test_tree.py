import json

from tree_workflow.tree import Tree

lst = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]


final_tree_with_flow_key = [
    {
        "id": 1,
        "parent": 0,
        "flow": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "flow": "1-1",
                "children": [{"id": 4, "parent": 2, "flow": "1-1-1"}],
            },
            {"id": 3, "parent": 1, "flow": "1-2"},
        ],
    },
    {"id": 5, "parent": 0, "flow": "2"},
]


final_tree_without_flow_key = [
    {
        "id": 1,
        "parent": 0,
        "children": [
            {"id": 2, "parent": 1, "children": [{"id": 4, "parent": 2}]},
            {"id": 3, "parent": 1},
        ],
    },
    {"id": 5, "parent": 0},
]


def test_tree_from_list_without_flow_key():
    trr = Tree(flow=False)
    tree = trr.tree_from_list(lst)
    assert tree == final_tree_without_flow_key


def test_tree_from_list():
    tr = Tree()
    tree = tr.tree_from_list(lst)
    assert tree == final_tree_with_flow_key


def test_list_from_tree():
    tr = Tree()
    tree = tr.tree_from_list(lst)
    lista = tr.list_from_tree(tree)
    print(json.dumps(lista))
