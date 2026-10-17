# yuno-playground

A tiny Python package used to exercise Yuno's project-repository feature. Agents clone it,
implement a task on a branch and open a merge request.

Run the tests with `python -m pytest`.

## Binary search tree

`bst.BinarySearchTree` is a generic, iterative BST. Duplicates are ignored
(`insert` returns `False`). `height()` is -1 for an empty tree.

```python
from bst import BinarySearchTree

t = BinarySearchTree([8, 3, 10, 1, 6])
t.insert(14)
3 in t              # True
t.min(), t.max()    # (1, 14)
t.delete(3)
list(t.in_order())  # [1, 6, 8, 10, 14]
list(t.pre_order()), list(t.post_order()), list(t.level_order())
t.size, t.height()
```
