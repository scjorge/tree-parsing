## Do something on the node

### New Node From List

You can change the "new_node" method to do something with the node when creating a tree from a list.

In this example, if the node id is "2", a new key will be added to the node.


```{.py3 linenums=1}
import json

from typing import Dict

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]


class MyTree(Tree):
    def new_node(self, node: Dict) -> None:
        if node['id'] == 2:
            node['new_key'] = 'new value'
        

tr = MyTree()
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
                "new_key": "new value",
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

### New Node From Tree

You can change the "new_node_list" method to do something with the node when creating a list from a tree.

In this example, if the node id is "3", a new key will be added to the node.

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

class MyTree(Tree):
    def new_node_list(self, node: Dict) -> None:
        if node['id'] == 3:
            node['new_key'] = 'new value'
            
tr = MyTree()
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
  "parent": 1,
  "new_key": "new value"
 },
 {
  "id": 4,
  "parent": 0
 }
]
```

## Changing the flow key

To change the logic of the sequence you can change the methods "make_parent_flow" and "make_child_flow".

Let's see the original implementation:

```{.py3 linenums=1}
class MixinTree:
    def __init__(self) -> None:
        self._flow_key: str

    def make_parent_flow(self, node: Dict, parent_number: int) -> None:
        node[self._flow_key] = f"{parent_number + 1}"

    def make_child_flow(
        self, node: Dict, child_number: int, parent_number: int
    ) -> None:
        flow = f"{parent_number}-{child_number + 1}"
        node[self._flow_key] = flow
```

Now you can change it according to your need.


In this example, the parent node will start with the value "0" and we change the string format by replacing the character "-" with "_"


```{.py3 linenums=1}
import json

from typing import Dict

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]


class MyTree(Tree):
    def make_parent_flow(self, node: Dict, parent_number: int) -> None:
        node[self._flow_key] = f"{parent_number}"

    def make_child_flow(
        self, node: Dict, child_number: int, parent_number: int
    ) -> None:
        flow = f"{parent_number}_{child_number}"
        node[self._flow_key] = flow
        

tr = MyTree()
tree = tr.tree_from_list(list_tree)
print(json.dumps(tree, indent=4))
```

Output:

```
[
    {
        "id": 1,
        "parent": 0,
        "flow": "0",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "flow": "0_0",
                "children": [
                    {
                        "id": 4,
                        "parent": 2,
                        "flow": "0_0_0"
                    }
                ]
            },
            {
                "id": 3,
                "parent": 1,
                "flow": "0_1"
            }
        ]
    },
    {
        "id": 5,
        "parent": 0,
        "flow": "1"
    }
]
```