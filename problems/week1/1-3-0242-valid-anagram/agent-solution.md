# 1.3 Valid Anagram — Agent solution

- Problem: [description](problem-description.md)
- Author: Codex (agent-written explanation and code)
- Basis: the local problem description; no external solution consulted
- Created: October 25, 2026
- Context: the agent previously saw the user's sorting solution; this is not a blind attempt.
- Validation: local examples and edge cases; not submitted to LeetCode

## Approach

Anagrams have identical character frequencies. First reject unequal lengths.
Then use 26 counters, one for each lowercase English letter. Increment a
letter's counter for each occurrence in `s` and decrement it for each
occurrence in `t`. Return `True` exactly when every counter is zero.

## Python solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        first_letter = ord("a")

        for character in s:
            counts[ord(character) - first_letter] += 1
        for character in t:
            counts[ord(character) - first_letter] -= 1

        return all(count == 0 for count in counts)
```

`ord(character) - ord("a")` maps `a` to index 0, `b` to index 1, and so on.
This indexing relies on the problem's lowercase-English-letter constraint.
The input strings are not modified.

## Why it works

After both loops, each counter equals that letter's frequency in `s` minus
its frequency in `t`. All counters are zero if and only if the strings have
the same letters with the same multiplicities, which is exactly the anagram
condition. Unequal lengths cannot be anagrams.

## Complexity

Let n = len(s) and m = len(t).

- Time: O(n + m) for the scans plus a fixed 26-counter check. Unequal lengths
  return in O(1). For equal lengths, the scan is O(n).
- Auxiliary space: O(1), since the counter list always has 26 entries,
  regardless of input length, under the usual bounded-integer model.

## Unicode follow-up

For arbitrary Unicode characters, replace the fixed array with a dictionary
of character counts, or compare `collections.Counter(s)` and
`collections.Counter(t)`. This takes O(n + m) average time and O(k) space for
k distinct characters. Clarify whether characters mean Unicode code points
or user-perceived characters, and whether normalization is required, before
choosing how to count them.

## Comparison with my solution

The [personal solution](my-solution.py) sorts both strings and compares them:
O(n log n + m log m) worst-case time and O(n + m) auxiliary space.
The agent solution uses the fixed alphabet to count characters in linear time
with constant auxiliary space. Both approaches preserve repeated characters.

## Local validation

Both examples from the description pass. Additional checks cover:

| s | t | Expected |
| --- | --- | --- |
| `"a"` | `"a"` | `True` |
| `"a"` | `"b"` | `False` |
| `"ab"` | `"a"` | `False` |
| `"aab"` | `"abb"` | `False` |
| `"aab"` | `"aba"` | `True` |
| `"az"` | `"za"` | `True` |

Also checked matching and mismatching inputs at the 50,000-character limit.
