# Tree Workflow

[![CI](https://github.com/scjorge/tree-workflow/workflows/CI/badge.svg?event=push)](https://github.com/scjorge/tree-workflow/actions)
[![codecov](https://codecov.io/gh/scjorge/tree-workflow/branch/master/graph/badge.svg?token=0HF8XRJDV1)](https://codecov.io/gh/scjorge/tree-workflow)
[![pypi](https://img.shields.io/pypi/v/tree-workflow)](https://pypi.org/project/tree-workflow/)
[![pypi](https://img.shields.io/pypi/pyversions/tree-workflow)](https://pypi.org/project/tree-workflow/)
[![license](https://img.shields.io/pypi/l/tree-workflow)](https://github.com/scjorge/pydantic_br/blob/master/LICENSE)


<p align="center">
    <img src="./docs/assets/logo.png" width='200'/>
</p>

---

This library lets you work with trees and lists.

So you can:

- Make tree when you have all nodes on the list
- Convert the Tree to lists of nodes
- Customize how to generate 'flow key'
- Do something for each node


## Exemplos

### Tree From List 

```python
import json
from tree_workflow.tree import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]

tr = Tree(id_key="id", parent_key="parent", parent_start="0")
tree = tr.tree_from_list(list_tree)
print(json.dumps(tree, indent=4))
```

Output:

```
[
    {
        "id": 1,
        "parent": 0,
        "flow": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "flow": "1-1",
                "children": [
                    {
                        "id": 4,
                        "parent": 2,
                        "flow": "1-1-1"
                    }
                ]
            },
            {
                "id": 3,
                "parent": 1,
                "flow": "1-2"
            }
        ]
    },
    {
        "id": 5,
        "parent": 0,
        "flow": "2"
    }
]
```

### List From Tree

```python
import json
from tree_workflow.tree import Tree


my_tree = [
    {
        "id": 1,
        "parent": 0,
        "flow": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "flow": "1-1",
                "children": [
                    {
                        "id": 4,
                        "parent": 2,
                        "flow": "1-1-1"
                    }
                ]
            },
            {
                "id": 3,
                "parent": 1,
                "flow": "1-2"
            }
        ]
    },
    {
        "id": 5,
        "parent": 0,
        "flow": "2"
    }
]

tr = Tree(id_key="id", parent_key="parent", child_key="children")
list_tree = tr.list_from_tree(my_tree)
print(json.dumps(list_tree, indent=1))
```

Output:

```
[
 {
  "id": 1,
  "parent": 0,
  "flow": "1"
 },
 {
  "id": 2,
  "parent": 1,
  "flow": "1-1"
 },
 {
  "id": 4,
  "parent": 2,
  "flow": "1-1-1"
 },
 {
  "id": 3,
  "parent": 1,
  "flow": "1-2"
 },
 {
  "id": 5,
  "parent": 0,
  "flow": "2"
 }
]
```