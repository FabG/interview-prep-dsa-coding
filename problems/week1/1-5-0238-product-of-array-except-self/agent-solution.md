# 1.5 Product of Array Except Self — Agent solution

- Problem: [description](problem-description.md)
- Author: Codex; original explanation and Python code
- Created: November 1, 2026
- Basis: local problem description; personal solution not consulted for this implementation
- Validation: local examples, edge cases and exhaustive small inputs; not submitted to LeetCode

## Approach

For each index, multiply two quantities: the product of everything to its left
and the product of everything to its right. Neither includes the current element.

1. Walk left to right, storing the product of earlier elements in the output.
2. Walk right to left, multiplying each output entry by the product of later elements.

Use running products initialized to `1`: the product of an empty side is 1.
Update each running product **after** using it, so the current element stays excluded.

## Python solution

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
```

The input list is unchanged, and no division is used.

## Walkthrough

For `nums = [1, 2, 3, 4]`:

| Index | Current value | Product to its left | Product to its right | Result |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 24 | 24 |
| 1 | 2 | 1 | 12 | 12 |
| 2 | 3 | 2 | 4 | 8 |
| 3 | 4 | 6 | 1 | 6 |

After the first pass, `answer` is `[1, 1, 2, 6]`. The second pass transforms
it into `[24, 12, 8, 6]`. The right-product column is explanatory; the code
uses one scalar rather than storing another list.

## Why it works

Before index i in the first pass, `left_product` contains precisely the product
of indices less than i. Storing it before multiplying by nums[i] preserves that
invariant for the next iteration.

Before index i in the reverse pass, `right_product` contains precisely the
product of indices greater than i. Multiplying these two products includes
every input position exactly once except i.

Zeros require no special branching: with one zero, only its own output can be
nonzero; with two or more zeros, every output is zero. Negative values also work
through ordinary multiplication.

## Complexity

- **Time: O(n).** Output initialization and both passes are linear. Two sequential
  passes give O(n + n), not O(n²).
- **Auxiliary space: O(1), excluding output.** Only a fixed number of scalars
  is needed beyond the result list.
- **Space including output: O(n).** The result contains n values.

These bounds use constant-time arithmetic under the problem's bounded-product
constraints. Python integers can otherwise grow, making arithmetic cost depend
on integer size.

## Local validation

Both LeetCode examples and local cases for two elements, multiple zeros,
negative values and all ones passed. Also checked zero at either end, 100,000
ones, and every length-2-through-6 list over `[-2, -1, 0, 1, 2]` against a
straightforward multiplication oracle. The oracle is for testing only and is
not part of this O(n) implementation. Input preservation was checked as well.
