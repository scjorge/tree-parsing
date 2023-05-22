## Tree class

When instantiating a class, you can use some settings

`id_key`

&emsp; Id of the node.

`parent_key`

&emsp; Parent node id. This id has to match the id_key that identifies a parent node.


`child_key`

&emsp; When you create a tree from a list, this value will be the name of the key which will be a list of child nodes. If used when creating a list from a tree, this value will be used to identify the key that contains the list with the child nodes.


`parent_start`

&emsp; This is the value that defines a parent node. Ex: "0", "None".

`flow_key`

&emsp; when a tree is created from a list, will automatically be created in the key in the dictionary called "flow" that contains the
current node sequence. Ex: "flow": "1-1-2".

`flow`

&emsp; Receives a boolean value that generates the flow_key or not.

--- 

The default values ​​are:

```{.py3 linenums=1}
id_key: str = "id"

parent_key: str = "parent"

parent_start: Any = "0"

child_key: str = "children"

flow_key: str = "flow"

flow: bool = True
```

---

## Tree from List

### Default values 

In this example contains 2 trees in the list.

- The value "0" will be used to identify the parent node.
- The value of the key that contains the id of the node is "id"
- The value of the key that contains the id of the parent node is "parent"
- The key value that will be created with the list of child nodes will be "children"
- A key named "flow" will be automatically created with the current sequence of each node

```{.py3 linenums=1}
import json

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
    {"id": 6, "parent": 5},
    {"id": 7, "parent": 5},
]

tr = Tree(id_key="id", parent_key="parent", parent_start="0", child_key="children")
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
        "flow": "2",
        "children": [
            {
                "id": 6,
                "parent": 5,
                "flow": "2-1"
            },
            {
                "id": 7,
                "parent": 5,
                "flow": "2-2"
            }
        ]
    }
]
```

---

### Flow Key

In this example the value of the key flow will be changed to sequence.

```{.py3 linenums=1}
import json

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 0},
]

tr = Tree(flow_key="sequence")
tree = tr.tree_from_list(list_tree)
print(json.dumps(tree, indent=4))
```

Output:

```
[
    {
        "id": 1,
        "parent": 0,
        "sequence": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "sequence": "1-1"
            },
            {
                "id": 3,
                "parent": 1,
                "sequence": "1-2"
            }
        ]
    },
    {
        "id": 4,
        "parent": 0,
        "sequence": "2"
    }
]
```

---

You can disable the "flow_key".

```{.py3 linenums=1}
import json

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 0},
]

tr = Tree(flow=False)
tree = tr.tree_from_list(list_tree)
print(json.dumps(tree, indent=4))
```

Output:

```
[
    {
        "id": 1,
        "parent": 0,
        "children": [
            {
                "id": 2,
                "parent": 1
            },
            {
                "id": 3,
                "parent": 1
            }
        ]
    },
    {
        "id": 4,
        "parent": 0
    }
]
```

## List from Tree

Maybe you already have a tree and want to turn it into a list with all the nodes. Then you can pass a list of trees to turn into a list of nodes.

```{.py3 linenums=1}
import json

from tree_parsing import Tree

my_tree = [
    {
        "id": 1,
        "parent": 0,
        "children": [
            {
                "id": 2,
                "parent": 1
            },
            {
                "id": 3,
                "parent": 1
            }
        ]
    },
    {
        "id": 4,
        "parent": 0
    }
]

tr = Tree()
list_tree = tr.list_from_tree(my_tree)
print(json.dumps(list_tree, indent=1))
```

Output:

```
[
 {
  "id": 1,
  "parent": 0
 },
 {
  "id": 2,
  "parent": 1
 },
 {
  "id": 3,
  "parent": 1
 },
 {
  "id": 4,
  "parent": 0
 }
]
```

