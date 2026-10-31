# 1.4 Group Anagrams — Agent solution

- Problem: [description](problem-description.md)
- Author: Codex; original explanation and Python code
- Created: October 31, 2026
- Basis: the local problem description; personal solution not consulted for this implementation
- Validation: local examples and edge cases; not submitted to LeetCode

## Approach: group by character counts

Two words are anagrams exactly when they contain the same number of each letter.
Use a 26-element count vector as a signature. Convert it to a tuple so it can be
a dictionary key, and append each original word to the group for that signature.

For example, `eat`, `tea` and `ate` all have one `a`, one `e` and one `t`, so
their signatures match. `tan` and `nat` share a different signature.

## Python solution

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = {}
        first_letter = ord("a")

        for word in strs:
            counts = [0] * 26
            for character in word:
                counts[ord(character) - first_letter] += 1

            signature = tuple(counts)
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(word)

        return list(groups.values())
```

`ord(character) - ord("a")` maps lowercase letters to indices 0 through 25.
A tuple is hashable when its elements are hashable; a mutable list cannot be a
dictionary key. This solution relies on the lowercase-English input constraint.

Empty strings have an all-zero signature. Each occurrence is appended, so
repeated words and repeated empty strings are preserved. The input is unchanged.

## Why it works

After processing any prefix of the input, each dictionary entry contains exactly
the processed words with its signature. Equal signatures mean equal counts for
every letter, so all words in a group are anagrams. Conversely, anagrams have
equal signatures and therefore enter the same group. Every word is appended
once, ensuring no occurrence is lost or added.

## Complexity

Let n be the number of words, T the total number of characters, g the number of
groups, and A = 26 the alphabet size.

- Average time: O(T + nA). Each character is counted once; creating, hashing
  and comparing signatures costs O(A) per word, with average dictionary lookup
  behavior. For the fixed alphabet this is O(T + n).
- If k is the maximum word length, the bound is O(n(k + 1)). It is commonly
  shortened to O(nk) for nonempty words, but the +1 accounts for empty strings.
- Extra storage including returned groups: O(gA + n), or O(n) for fixed A.
  The lists store references to existing strings rather than copying characters.
- Excluding the returned group lists, auxiliary storage is O(gA + g + A),
  which is O(g) for fixed A: dictionary keys and entries plus temporary counts.

The average-time bound assumes ordinary hash-table behavior; pathological hash
collisions can make dictionary operations slower.

## Simpler alternative: sorted-word keys

Use `"".join(sorted(word))` as the dictionary key. It is concise and naturally
supports a wider character set, but sorting each word costs O(k log k) in the
worst case. Counting avoids sorting and takes advantage of the fixed alphabet.
For Unicode, define whether equality should account for normalization or case
before adapting either approach.

## Local validation

All three source examples passed. Additional checks covered:

- Repeated words and repeated empty strings in the same input.
- Same letters with different multiplicities (`aab`, `abb`, `aba`).
- All words in one group and all words in distinct groups.
- Alphabet boundary letters (`a` and `z`).

Comparisons ignore both group order and order within groups while retaining
multiplicity. Input preservation was also checked.
