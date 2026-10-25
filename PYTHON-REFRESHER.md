# Python refresher for coding interviews

A practical reference for an experienced developer who is rusty with Python. Read enough to regain fluency, then type the examples from memory. The goal is to express and debug your reasoning without fighting the language.

Examples target **Python 3.9+** and use only the standard library. Check the selected interview runtime before using newer features. This refresher does not include the solution to problem 1.1.

## A one hour refresh

| Minutes | Focus |
| --- | --- |
| 0–10 | Syntax, iteration, indexing and functions |
| 10–25 | Lists, dictionaries, sets and strings |
| 25–35 | Mutation, copying and common traps |
| 35–45 | Sorting, queues, heaps and binary search |
| 45–60 | Complete three drills near the end without looking back |

Save recursion and memoization for a second session if they need more attention. All Python code blocks below are independent, executable examples with assertions; copy one into a scratch file and run it with `python3`.

## Syntax you should be able to write without searching

Indentation defines blocks. Use four spaces. Conditions use `and`, `or`, `not`; branches use `if`, `elif`, `else`. Python has no `++` operator: use `i += 1`.

```python
values = [6, -2, 0, 9]
positive = []
for value in values:
    if value > 0:
        positive.append(value)
assert positive == [6, 9]

left, right = 0, len(values) - 1
left, right = right, left  # RHS is evaluated before assignment
assert (left, right) == (3, 0)

label = "empty" if not values else "nonempty"
assert label == "nonempty"
```

`None`, zero and empty collections are false in a condition. Use `value is None` when zero or an empty collection is a meaningful result. `==` compares values; `is` compares object identity. [Types and truth values](https://docs.python.org/3/library/stdtypes.html).

```python
position = 0
assert not position                 # Zero is false
assert position is not None        # But it is a valid index
assert 9 / 4 == 2.25                # True division
assert 9 // 4 == 2                  # Floor division
assert -9 // 4 == -3                # Floors toward negative infinity
assert -9 % 4 == 3
assert 2 ** 4 == 16                 # Exponentiation; ^ means XOR
assert divmod(9, 4) == (2, 1)
```

Integers can grow beyond fixed machine widths. That prevents ordinary fixed-width overflow, but arithmetic on very large integers is not constant-time.

## Iteration and indexing

`range(start, stop, step)` excludes `stop`. Prefer `enumerate` when both index and value matter. `zip` stops at the shortest input. [Built-in functions](https://docs.python.org/3/library/functions.html).

```python
items = [8, 3, 5]
assert list(range(3)) == [0, 1, 2]
assert list(range(2, -1, -1)) == [2, 1, 0]
assert list(enumerate(items)) == [(0, 8), (1, 3), (2, 5)]
assert list(zip(["a", "b"], [10])) == [("a", 10)]
assert items[-1] == 5
assert items[1:3] == [3, 5]          # Stop excluded
assert items[::-1] == [5, 3, 8]      # Reversed copy
```

A negative index wraps from the end; it does not indicate “outside the array.” Validate grid coordinates before indexing. List slices allocate a new list; an index outside the list raises `IndexError`, while slice boundaries are clipped.

## Lists, tuples and comprehensions

Use a list for an ordered, mutable sequence or a stack. Use a tuple for a fixed record such as a coordinate. `{}` creates an empty dictionary; `set()` creates an empty set.

```python
stack = [4, 7]
stack.append(11)
assert stack[-1] == 11              # Peek
assert stack.pop() == 11            # Remove from the end
stack.extend([2, 6])
assert stack == [4, 7, 2, 6]

squares = [x * x for x in range(6) if x % 2 == 0]
assert squares == [0, 4, 16]
coordinate = (2, 5)
row, col = coordinate
assert row == 2 and col == 5
single_item_tuple = (4,)            # The comma matters
```

Keep comprehensions simple enough to explain aloud. `append` adds one object; `extend` adds the items from an iterable. `remove(x)` removes a value, while `pop(i)` removes an index. [Data structures tutorial](https://docs.python.org/3/tutorial/datastructures.html).

## Dictionaries and sets

A dictionary maps keys to values; a set tracks membership. Keys and set members must be hashable: integers, strings and tuples of hashable values work; lists do not. Membership in a dictionary checks keys.

```python
ages = {"Mia": 31, "Noah": 28}
assert "Mia" in ages
assert ages.get("Ava", 0) == 0       # Default without inserting
ages["Ava"] = 26
assert set(ages.items()) == {("Mia", 31), ("Noah", 28), ("Ava", 26)}

seen = set()
seen.add((2, 5))
assert (2, 5) in seen
seen.discard((9, 9))                # Missing item is fine
assert {1, 2} & {2, 3} == {2}       # Intersection
assert {1, 2} | {2, 3} == {1, 2, 3} # Union
```

Dictionaries preserve insertion order; sets do not promise a useful iteration order. Avoid adding or removing keys while iterating over the same dictionary. Use a snapshot or collect changes first. [Mappings and sets](https://docs.python.org/3/library/stdtypes.html).

## Strings and small built-ins

Strings are immutable. Build a list of pieces and join it when producing a longer result. Repeated concatenation can create repeated copying.

```python
text = "  Python makes sense  "
assert text.strip().split() == ["Python", "makes", "sense"]
assert "-".join(["fast", "clear"]) == "fast-clear"
assert "AbC".lower() == "abc"
assert "A7".isalnum()
assert ord("d") - ord("a") == 3     # Only assume a-z when allowed
assert chr(ord("a") + 3) == "d"
assert f"items={3}" == "items=3"

assert sum([3, 6, 9]) == 18
assert any(x < 0 for x in [3, -6])
assert all(x >= 0 for x in [3, 6])
assert min([], default=0) == 0
```

`any` and `all` can stop early. The expressions above pass generators rather than building intermediate lists. A generator is consumed as it is traversed; it is not a reusable list. [Built-ins](https://docs.python.org/3/library/functions.html), [string operations](https://docs.python.org/3/library/stdtypes.html).

## Functions, scope and type hints

Arguments refer to objects: mutating a passed list affects the caller, while rebinding the local parameter does not. Type hints document intent; they do not enforce types at runtime. A function that reaches its end without returning produces `None`.

```python
def keep_at_least(values: list[int], minimum: int = 0) -> list[int]:
    return [value for value in values if value >= minimum]

assert keep_at_least([-3, 0, 4]) == [0, 4]
assert keep_at_least([-3, 0, 4], minimum=2) == [4]

# Never use a mutable default such as bucket=[] for per-call state.
def collect(value: int, bucket=None) -> list[int]:
    if bucket is None:
        bucket = []
    bucket.append(value)
    return bucket

assert collect(4) == [4]
assert collect(9) == [9]
```

Default values are evaluated when the function is defined. A shared default list can retain data between calls. Inside nested functions, `nonlocal` permits rebinding a variable from the enclosing function; mutating an enclosing list does not require it. [Functions and parameters](https://docs.python.org/3/tutorial/controlflow.html).

## Mutation and copying traps

Assignment binds another name to the same object. A shallow copy duplicates the outer container but retains references to nested objects. [Copy semantics](https://docs.python.org/3/library/copy.html).

```python
original = [[1], [2]]
alias = original
shallow = original.copy()
assert alias is original
assert shallow is not original
shallow[0].append(9)
assert original == [[1, 9], [2]]     # Inner list is still shared

rows, cols = 3, 2
bad_grid = [[0] * cols] * rows       # Repeats the same row object
bad_grid[0][0] = 7
assert bad_grid[1][0] == 7

grid = [[0] * cols for _ in range(rows)]
grid[0][0] = 7
assert grid[1][0] == 0

path = [1, 2]
answers = [path.copy()]             # Snapshot for backtracking
path.append(3)
assert answers == [[1, 2]]
```

For deeper nested state, decide which objects need copying rather than reaching automatically for `deepcopy`. When modifying a collection in a loop, be explicit about whether iteration sees the original or a snapshot.

## Sorting

`sorted(values)` returns a new list. `values.sort()` changes the list and returns `None`. Both are stable: equal keys retain their original relative order. [Sorting guide](https://docs.python.org/3/howto/sorting.html).

```python
values = [7, 2, 5]
ordered = sorted(values)
assert values == [7, 2, 5]
assert ordered == [2, 5, 7]
result = values.sort(reverse=True)
assert result is None
assert values == [7, 5, 2]

records = [("a", 4), ("b", 2), ("c", 4)]
assert sorted(records, key=lambda record: record[1]) == [
    ("b", 2), ("a", 4), ("c", 4)
]
# Ascending second field, then descending first field for numeric pairs.
pairs = [(2, 4), (3, 4), (1, 2)]
assert sorted(pairs, key=lambda pair: (pair[1], -pair[0])) == [
    (1, 2), (3, 4), (2, 4)
]
```

Do not assign `values = values.sort()`. Sorting in place still uses temporary memory internally; it is not automatically an O(1)-space operation.

## The collections toolkit

Use `Counter` for frequencies, `defaultdict` for grouped values, and `deque` for a FIFO queue. Accessing a missing `defaultdict` key with brackets inserts the factory result; `.get()` does not. [Collections reference](https://docs.python.org/3/library/collections.html).

```python
from collections import Counter, defaultdict, deque

counts = Counter("balloon")
assert counts["l"] == 2
assert counts["z"] == 0

groups = defaultdict(list)
for name, team in [("Mia", "red"), ("Noah", "blue"), ("Ava", "red")]:
    groups[team].append(name)
assert groups["red"] == ["Mia", "Ava"]
assert groups.get("green") is None
assert "green" not in groups

queue = deque(["first"])
queue.append("second")
assert queue.popleft() == "first"
assert queue[0] == "second"
```

Repeated `list.pop(0)` shifts the remaining elements. Use `deque.popleft()` for breadth-first traversal. When traversing a graph, marking nodes visited when enqueuing avoids duplicate queue entries.

## Heaps and binary search

A `heapq` heap is a list organized so its minimum is at position zero; the rest of the list is not sorted. `heapify` builds it in O(n); push and pop take O(log n). Negating numeric priorities provides a portable max-heap technique. With equal priorities and unorderable objects, add a unique numeric tie-breaker to the tuple. [Heap reference](https://docs.python.org/3/library/heapq.html).

```python
import heapq

heap = [8, 2, 6]
heapq.heapify(heap)
heapq.heappush(heap, 4)
assert heap[0] == 2
assert heapq.heappop(heap) == 2

max_heap = [-value for value in [8, 2, 6]]
heapq.heapify(max_heap)
assert -heapq.heappop(max_heap) == 8
```

`bisect_left` returns the first suitable insertion position; `bisect_right` returns the position after existing equal values. Neither guarantees that the searched value exists. Search is O(log n); inserting into the list remains O(n). [Bisect reference](https://docs.python.org/3/library/bisect.html).

```python
from bisect import bisect_left, bisect_right

values = [2, 4, 4, 9]
assert bisect_left(values, 4) == 1
assert bisect_right(values, 4) == 3
assert bisect_left(values, 7) == 3
index = bisect_left(values, 7)
found = index < len(values) and values[index] == 7
assert not found
```

## Recursion and memoization

Every recursive function needs a base case and progress toward it. Python limits recursion depth; long chains may need an explicit stack. Raising the limit is not a general fix. [Recursion limit](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit).

`lru_cache(maxsize=None)` caches results by hashable arguments. `cache` is another unbounded option on Python 3.9+. Cache a function whose result is determined by its arguments; changes to hidden mutable inputs can make cached results stale. Caching also uses memory. [Memoization reference](https://docs.python.org/3/library/functools.html).

```python
from functools import lru_cache

# A syntax demonstration, not a recommended replacement for n * (n + 1) // 2.
@lru_cache(maxsize=None)
def triangular(n: int) -> int:
    if n == 0:
        return 0
    return n + triangular(n - 1)

assert triangular(5) == 15
triangular.cache_clear()
```

## Classes and the LeetCode wrapper

`self` is the current instance, passed automatically when you call its method. Put per-object mutable state in `__init__`, not in a shared class attribute. Adapt to the exact signature provided by the problem. [Classes tutorial](https://docs.python.org/3/tutorial/classes.html).

```python
class Solution:
    # A small example unrelated to the pending Two Sum exercise.
    def countPositive(self, nums: list[int]) -> int:
        return sum(value > 0 for value in nums)

solver = Solution()
assert solver.countPositive([-2, 0, 5, 8]) == 2
assert solver.countPositive([]) == 0
```

For older signatures, `List[int]` needs `from typing import List`; `list[int]` works on Python 3.9+. Include required imports when saving code locally. A local call uses `Solution().method(arguments)`; printing the answer is different from returning it.

## Costs worth remembering

Typical CPython interview cost model; n is container size and k is output length. Hash operations assume ordinary hashes and constant-size keys; dictionary/set lookup is average O(1), with O(n) worst cases. Comparing or hashing long values adds their own cost.

| Operation | Typical cost |
| --- | --- |
| List indexing or `len(list)` | O(1) |
| List append | Amortized O(1) |
| List pop from end | O(1) |
| List front insertion/removal or membership search | O(n) |
| List slice of k elements | O(k) time and extra space |
| Dict/set lookup, insertion or deletion | Average O(1) |
| Deque append or pop at either end | O(1) |
| Sort a list | O(n log n) worst-case time |
| Heap build / push or pop / peek | O(n) / O(log n) / O(1) |
| Binary search in a sorted list | O(log n) |
| String join | O(total output length), plus processing the pieces |

A short expression can conceal a loop: `x in values`, `values.index(x)`, `sum(values)` and slicing all deserve attention inside another loop. Include recursion frames, copies, visited sets and caches in auxiliary-space analysis.

## Debugging when you are rusty

Read the final line of a traceback first, then the relevant call above it. `KeyError` usually means a missing dictionary key; `IndexError` means an invalid sequence position; `TypeError` often means an unexpected type or call signature. Catch specific exceptions only when recovery is intended. Broadly swallowing exceptions hides bugs. [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html).

Use a tiny input you can trace by hand. Inspect changing state with `print(f"{index=}, {value=}")` when those variables exist, then remove debugging output. Assertions are useful for local checks, but can be disabled with optimized execution; do not use them as production input validation.

## Practice drills

Spend 15–20 minutes on three drills. Type the code without copying an earlier example.

1. **Index fluency:** produce `(index, value)` pairs for every negative item. For `[4, -2, 0, -7]`, expect `[(1, -2), (3, -7)]`.
2. **Safe matrix:** create a 3-by-4 grid of independent zero-filled rows. Set one cell to 9 and verify only that cell changes.
3. **Frequency map:** count letters in `"cocoa"`. Expect `{"c": 2, "o": 2, "a": 1}`. First use a plain dictionary, then `Counter`.
4. **Stable sort:** sort `[("a", 3), ("b", 1), ("c", 3)]` by the number. Expect `[("b", 1), ("a", 3), ("c", 3)]`.
5. **Queue:** enqueue three strings, dequeue two, then assert which string remains.
6. **Function defaults:** call a collecting function twice without supplying a list. Prove the calls do not share state.
7. **Search boundaries:** find insertion positions on either side of 5 in `[1, 5, 5, 5, 8]`. Expect 1 and 4.
8. **Heap:** remove the two smallest values from `[7, 1, 4, 2]`. Expect 1 followed by 2.

When these feel comfortable, return to [problem 1.1](problems/0001-two-sum/problem-description.md). Keep your submitted code in [my-solution.py](problems/0001-two-sum/my-solution.py) and record any syntax mistake you had to look up. Revisit only those sections before the next session.

## Before you submit

- Does the function return the requested type and use the given signature?
- Are zero, empty input where allowed, duplicates and boundary indices handled?
- Did you accidentally alias mutable state or overwrite a list with `.sort()`'s return value?
- Are membership checks and slices adding hidden work inside loops?
- Can you explain both time and auxiliary-space complexity?

Reference links point to official Python documentation, checked October 25, 2026. Examples are original and deliberately use a conservative language baseline rather than assuming the newest runtime.
