"""A generic binary search tree with iterative algorithms."""

from __future__ import annotations

from collections import deque
from typing import Generic, Iterator, Optional, Protocol, TypeVar


class _Comparable(Protocol):
    def __lt__(self, other: "_Comparable", /) -> bool: ...


T = TypeVar("T", bound=_Comparable)


class Node(Generic[T]):
    """A tree node holding a value and optional left/right children."""

    __slots__ = ("value", "left", "right")

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class BinarySearchTree(Generic[T]):
    """Binary search tree. Duplicates policy: duplicates are ignored.

    All operations are iterative, so degenerate trees never hit the
    recursion limit. Values must support ``<`` and ``==``.
    """

    def __init__(self, values: Optional[Iterator[T] | list[T]] = None) -> None:
        self.root: Optional[Node[T]] = None
        self._size = 0
        for v in values or ():
            self.insert(v)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, value: object) -> bool:
        return self.search(value) is not None  # type: ignore[arg-type]

    def __iter__(self) -> Iterator[T]:
        return self.in_order()

    @property
    def size(self) -> int:
        """Number of values in the tree."""
        return self._size

    def insert(self, value: T) -> bool:
        """Insert value. Return True if added, False if it was a duplicate."""
        if self.root is None:
            self.root = Node(value)
            self._size = 1
            return True
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    break
                cur = cur.left
            elif cur.value < value:
                if cur.right is None:
                    cur.right = Node(value)
                    break
                cur = cur.right
            else:
                return False
        self._size += 1
        return True

    def search(self, value: T) -> Optional[Node[T]]:
        """Return the node holding value, or None."""
        cur = self.root
        while cur is not None:
            if value < cur.value:
                cur = cur.left
            elif cur.value < value:
                cur = cur.right
            else:
                return cur
        return None

    def contains(self, value: T) -> bool:
        """Return True if value is in the tree."""
        return self.search(value) is not None

    def delete(self, value: T) -> bool:
        """Delete value (leaf, one-child or two-child). Return True if removed."""
        parent: Optional[Node[T]] = None
        cur = self.root
        while cur is not None and (value < cur.value or cur.value < value):
            parent = cur
            cur = cur.left if value < cur.value else cur.right
        if cur is None:
            return False

        if cur.left is not None and cur.right is not None:
            # Two children: replace with in-order successor's value.
            succ_parent = cur
            succ = cur.right
            while succ.left is not None:
                succ_parent = succ
                succ = succ.left
            cur.value = succ.value
            parent, cur = succ_parent, succ

        child = cur.left if cur.left is not None else cur.right
        if parent is None:
            self.root = child
        elif parent.left is cur:
            parent.left = child
        else:
            parent.right = child
        self._size -= 1
        return True

    def min(self) -> T:
        """Smallest value. Raises ValueError if empty."""
        if self.root is None:
            raise ValueError("tree is empty")
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.value

    def max(self) -> T:
        """Largest value. Raises ValueError if empty."""
        if self.root is None:
            raise ValueError("tree is empty")
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.value

    def height(self) -> int:
        """Number of edges on the longest root-to-leaf path (-1 if empty)."""
        if self.root is None:
            return -1
        h = -1
        level = [self.root]
        while level:
            h += 1
            level = [c for n in level for c in (n.left, n.right) if c is not None]
        return h

    def in_order(self) -> Iterator[T]:
        """Yield values left, node, right (sorted order)."""
        stack: list[Node[T]] = []
        cur = self.root
        while stack or cur is not None:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            yield cur.value
            cur = cur.right

    def pre_order(self) -> Iterator[T]:
        """Yield values node, left, right."""
        stack = [self.root] if self.root else []
        while stack:
            node = stack.pop()
            yield node.value
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def post_order(self) -> Iterator[T]:
        """Yield values left, right, node."""
        stack: list[Node[T]] = []
        cur = self.root
        last: Optional[Node[T]] = None
        while stack or cur is not None:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                top = stack[-1]
                if top.right is not None and last is not top.right:
                    cur = top.right
                else:
                    yield top.value
                    last = stack.pop()

    def level_order(self) -> Iterator[T]:
        """Yield values breadth-first, level by level."""
        queue: deque[Node[T]] = deque([self.root] if self.root else [])
        while queue:
            node = queue.popleft()
            yield node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
