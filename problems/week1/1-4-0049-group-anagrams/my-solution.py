"""Problem 1.4: Group Anagrams — my solution.

Source: https://leetcode.com/problems/group-anagrams/
Status: N — not attempted; scaffold only
Submission link:
Submission date:
Submission result: not submitted
Time spent:
Assistance used: problem description and local test scaffold only
To review again?: No — update after the attempt

Approach and reasoning: fill in after your attempt.
Time complexity: to be determined.
Auxiliary space: to be determined.
Mistakes and lessons:
Comparison with the agent solution: pending.
Review history:

Run from the repository root:
    python3 problems/week1/1-4-0049-group-anagrams/my-solution.py

The harness ignores ordering but preserves duplicate occurrences. Each example
runs even if an earlier example fails. Run without -O, which disables assertions.
Submit only the Solution class and required imports to LeetCode.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # convert each string from the list to sorted list of characters and use it as the key in the dictionary
        anagram_map: dict[str, str] = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in anagram_map:
                anagram_map[s_sorted] = []
            anagram_map[s_sorted].append(s)
        return list(anagram_map.values())

        raise NotImplementedError("Add your groupAnagrams implementation, then run this file again.")


def normalize_groups(groups: list[list[str]]) -> list[list[str]]:
    """Normalize output ordering for comparison without removing duplicates."""
    return sorted(sorted(group) for group in groups)


def run_examples() -> None:
    """Check the three problem examples and one additional duplicate case."""
    cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        # Additional local case, not a quoted LeetCode example.
        (["ab", "ba", "ab", "", ""], [["ab", "ba", "ab"], ["", ""]]),
    ]
    passed = 0
    failed = 0
    for number, (strs, expected) in enumerate(cases, start=1):
        try:
            actual = Solution().groupAnagrams(strs.copy())
            assert isinstance(actual, list), f"expected a list, got {actual!r}"
            assert all(isinstance(group, list) for group in actual), (
                f"expected a list of lists, got {actual!r}"
            )
            assert all(isinstance(word, str) for group in actual for word in group), (
                f"expected strings in every group, got {actual!r}"
            )
            assert normalize_groups(actual) == normalize_groups(expected), (
                f"expected {expected!r} (any order), got {actual!r}"
            )
        except AssertionError as error:
            failed += 1
            print(f"Case {number} FAILED: {error}")
            print(f"  strs={strs!r}")
        except Exception as error:
            failed += 1
            print(f"Case {number} ERROR: {type(error).__name__}: {error}")
            print(f"  strs={strs!r}, expected={expected!r}")
        else:
            passed += 1
            print(f"Case {number} PASSED: {actual!r}")
    print(f"\nResults: {passed} passed, {failed} failed, {len(cases)} total.")


if __name__ == "__main__":
    run_examples()
