# Tree Workflow

<p align="center">
    <img src="./assets/logo.png" width='200'/>
</p>

<center>

[![codecov](https://codecov.io/gh/scjorge/pydantic_br/branch/master/graph/badge.svg?token=1XVEXSBU69)](https://codecov.io/gh/scjorge/pydantic_br)
[![pypi](https://img.shields.io/pypi/v/pydantic-br)](https://pypi.org/project/pydantic-br/)
[![pypi](https://img.shields.io/pypi/pyversions/pydantic-br)](https://pypi.org/project/pydantic-br/)
[![license](https://img.shields.io/pypi/l/pydantic-br)](https://github.com/scjorge/pydantic_br/blob/master/LICENSE)

</center>

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