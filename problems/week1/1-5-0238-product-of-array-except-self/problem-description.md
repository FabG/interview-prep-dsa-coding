# 1.5 Product of Array Except Self

- LeetCode problem: 238
- Difficulty: Medium
- Source: [Product of Array Except Self on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)
- Captured: November 1, 2026
- Language: Python

## Task

Return a list where the value at each index is the product of every input
value except the value at that index. Preserve index order.

Your algorithm must run in **O(n) time** and **must not use division**.

This description summarizes the linked LeetCode problem.

## Examples from LeetCode

| nums | Expected result |
| --- | --- |
| `[1, 2, 3, 4]` | `[24, 12, 8, 6]` |
| `[-1, 1, 0, -3, 3]` | `[0, 0, 9, 0, 0]` |

## Input limits

- Between 2 and 100,000 integers.
- Each integer is between -30 and 30, inclusive.
- Every prefix product, suffix product and output value fits in a signed 32-bit integer.

## Follow-up

Can you use **O(1) extra space**, excluding the output list?

## Workspace

- [My solution](my-solution.py)
- [Agent solution](agent-solution.md)
- [Progress tracker](../../../TRACKER.md)

Run from the repository root:

```bash
python3 problems/week1/1-5-0238-product-of-array-except-self/my-solution.py
```
