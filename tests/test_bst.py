import pytest

from bst import BinarySearchTree, Node


def make() -> BinarySearchTree[int]:
    #        8
    #      /   \
    #     3     10
    #    / \      \
    #   1   6      14
    #      / \    /
    #     4   7  13
    return BinarySearchTree([8, 3, 10, 1, 6, 14, 4, 7, 13])


def test_empty():
    t: BinarySearchTree[int] = BinarySearchTree()
    assert len(t) == 0 and t.size == 0
    assert t.height() == -1
    assert t.search(1) is None and not t.contains(1) and 1 not in t
    assert list(t.in_order()) == list(t.pre_order()) == []
    assert list(t.post_order()) == list(t.level_order()) == []
    assert t.delete(1) is False
    with pytest.raises(ValueError):
        t.min()
    with pytest.raises(ValueError):
        t.max()


def test_single_node():
    t = BinarySearchTree[int]()
    assert t.insert(5) is True
    assert t.size == 1 and t.height() == 0
    assert t.min() == t.max() == 5
    assert isinstance(t.search(5), Node)
    assert list(t) == [5]
    assert t.delete(5) is True
    assert t.root is None and t.size == 0 and t.height() == -1


def test_duplicates_ignored():
    t = BinarySearchTree[int]()
    assert t.insert(2) is True
    assert t.insert(2) is False
    assert t.size == 1 and list(t) == [2]


def test_traversals():
    t = make()
    assert list(t.in_order()) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert list(t.pre_order()) == [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert list(t.post_order()) == [1, 4, 7, 6, 3, 13, 14, 10, 8]
    assert list(t.level_order()) == [8, 3, 10, 1, 6, 14, 4, 7, 13]


def test_search_min_max_height_size():
    t = make()
    assert t.size == 9 and t.height() == 3
    assert t.min() == 1 and t.max() == 14
    assert t.contains(13) and 7 in t and 5 not in t
    assert t.search(6).value == 6


def test_delete_missing():
    t = make()
    assert t.delete(99) is False
    assert t.size == 9


def test_delete_leaf():
    t = make()
    assert t.delete(4) is True
    assert list(t.in_order()) == [1, 3, 6, 7, 8, 10, 13, 14]
    assert t.size == 8 and 4 not in t


def test_delete_one_child():
    t = make()
    assert t.delete(14) is True  # only left child (13)
    assert list(t.pre_order()) == [8, 3, 1, 6, 4, 7, 10, 13]
    assert t.size == 8
    assert t.delete(10) is True  # only right child (13)
    assert list(t.level_order()) == [8, 3, 13, 1, 6, 4, 7]


def test_delete_two_children():
    t = make()
    assert t.delete(3) is True
    assert list(t.in_order()) == [1, 4, 6, 7, 8, 10, 13, 14]
    assert t.root.left.value == 4
    assert t.size == 8


def test_delete_root_two_children():
    t = make()
    assert t.delete(8) is True
    assert t.root.value == 10
    assert list(t.in_order()) == [1, 3, 4, 6, 7, 10, 13, 14]
    assert t.size == 8


def test_delete_root_one_child():
    t = BinarySearchTree([5, 7, 9])
    assert t.delete(5) is True
    assert t.root.value == 7
    assert list(t) == [7, 9]
    assert t.height() == 1


def test_delete_everything_height_size():
    t = make()
    for i, v in enumerate([8, 3, 10, 1, 6, 14, 4, 7, 13], 1):
        assert t.delete(v)
        assert t.size == 9 - i
        assert list(t) == sorted(list(t))
    assert t.root is None and t.height() == -1


def test_height_after_ops():
    t = BinarySearchTree([2, 1, 3])
    assert t.height() == 1
    t.insert(4)
    assert t.height() == 2
    t.delete(4)
    assert t.height() == 1


def test_strings():
    t = BinarySearchTree(["m", "c", "x"])
    assert list(t) == ["c", "m", "x"]
    assert t.min() == "c" and t.max() == "x"


def test_degenerate_large_tree():
    n = 3000  # well beyond the default recursion limit (1000)
    t = BinarySearchTree[int]()
    for i in range(n):
        t.insert(i)
    assert t.size == n and t.height() == n - 1
    assert t.min() == 0 and t.max() == n - 1
    assert list(t.in_order()) == list(range(n))
    assert list(t.pre_order()) == list(range(n))
    assert list(t.post_order()) == list(range(n - 1, -1, -1))
    assert list(t.level_order()) == list(range(n))
    assert t.contains(n - 1)
    assert t.delete(0) and t.delete(n - 1)
    assert t.size == n - 2 and t.height() == n - 3
