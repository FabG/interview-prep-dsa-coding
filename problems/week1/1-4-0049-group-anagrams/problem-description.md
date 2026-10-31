# 1.4 Group Anagrams

- LeetCode problem: 49
- Difficulty: Medium
- Source: [Group Anagrams on LeetCode](https://leetcode.com/problems/group-anagrams/)
- Captured: October 31, 2026
- Language: Python

## Task

Partition the input list `strs` into groups of anagrams. Two strings are anagrams
when their letters can be rearranged to match, using each letter the same number
of times. Return a list of groups containing the original strings.

The order of groups and the order of strings within each group do not matter.
Keep every occurrence of an input string, including duplicates.

This description summarizes the linked LeetCode problem.

## Examples from LeetCode

| strs | Expected groups (one valid ordering) |
| --- | --- |
| `["eat", "tea", "tan", "ate", "nat", "bat"]` | `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]` |
| `[""]` | `[[""]]` |
| `["a"]` | `[["a"]]` |

## Input limits

- Between 1 and 10,000 strings.
- Each string has between 0 and 100 characters.
- Characters are lowercase English letters.

## Workspace

- [My solution](my-solution.py)
- [Agent solution](agent-solution.md)
- [Progress tracker](../../../TRACKER.md)

Run from the repository root:

```bash
python3 problems/week1/1-4-0049-group-anagrams/my-solution.py
```
