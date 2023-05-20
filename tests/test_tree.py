from tree_tools import Tree

list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]

list_tree_1 = [
    {"id_key": 1, "father": None},
    {"id_key": 2, "father": 1},
    {"id_key": 3, "father": 1},
    {"id_key": 4, "father": 2},
    {"id_key": 5, "father": None},
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

final_tree_change_id_key = [
    {
        "id_key": 1,
        "father": None,
        "flow": "1",
        "child_tree": [
            {
                "id_key": 2,
                "father": 1,
                "flow": "1-1",
                "child_tree": [{"id_key": 4, "father": 2, "flow": "1-1-1"}],
            },
            {"id_key": 3, "father": 1, "flow": "1-2"},
        ],
    },
    {"id_key": 5, "father": None, "flow": "2"},
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


def test_tree_from_list():
    tr = Tree()
    tree = tr.tree_from_list(list_tree)
    assert tree == final_tree_with_flow_key


def test_tree_from_list_without_flow_key():
    tr = Tree(flow=False)
    tree = tr.tree_from_list(list_tree)
    assert tree == final_tree_without_flow_key


def test_tree_from_list_change_flow_key():
    tr = Tree(flow_key="sequence")
    tree = tr.tree_from_list(list_tree)
    assert "sequence" in tree[0]


def test_tree_from_list_change_id_key():
    tr = Tree(flow_key="sequence")
    tree = tr.tree_from_list(list_tree)
    assert "sequence" in tree[0]


def test_tree_from_list_change_id_key_parent_key_parent_start():
    tr = Tree(
        id_key="id_key", parent_key="father", parent_start=None, child_key="child_tree"
    )
    tree = tr.tree_from_list(list_tree_1)
    assert tree == final_tree_change_id_key


def test_list_from_tree():
    tr = Tree()
    list_tree_new = tr.list_from_tree(final_tree_without_flow_key)
    assert list_tree == sorted(list_tree_new, key=lambda x: x["id"])
