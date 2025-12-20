# 🎯 LeetCode String Problems - Curated List

> Master these problems to become a String Hero! 🦸

---

## 📊 Progress Tracker

| Difficulty | Total | Completed |
|------------|-------|-----------|
| 🟢 Easy | 15 | ☐/15 |
| 🟡 Medium | 20 | ☐/20 |
| 🔴 Hard | 5 | ☐/5 |

---

## 📺 What Each Problem Actually Asks (+ Videos!)

### 🟢 Easy Problems Explained

| # | What You're Asked To Do | 📺 Video |
|---|-------------------------|----------|
| 125 | Check if string is palindrome (ignore non-alphanumeric, case-insensitive) | [NeetCode](https://youtu.be/jJXJ16kPFWg) |
| 242 | Check if two strings are anagrams | [NeetCode](https://youtu.be/9UtInBqnCgA) |
| 344 | Reverse a string in-place (char array) | [NeetCode](https://youtu.be/P68JPXtFyAg) |
| 387 | Find first character that doesn't repeat | [NeetCode](https://youtu.be/oYZz7f7xpXM) |
| 392 | Is `s` a subsequence of `t`? (chars in order, not necessarily consecutive) | [NeetCode](https://youtu.be/99RVfqklbCE) |
| 409 | What's the longest palindrome you can build from these letters? | [NeetCode](https://youtu.be/aNoJUFwLSis) |
| 14 | Find the longest common prefix among all strings | [NeetCode](https://youtu.be/0sWShKIJoo4) |

### 🟡 Medium Problems Explained

| # | What You're Asked To Do | 📺 Video |
|---|-------------------------|----------|
| 3 | Find length of longest substring with NO repeating characters | [NeetCode](https://youtu.be/wiGpQwVHdE0) |
| 5 | Find the longest palindromic substring | [NeetCode](https://youtu.be/XYQecbcd6_c) |
| 49 | Group strings that are anagrams of each other | [NeetCode](https://youtu.be/vzdNOK2oB2E) |
| 438 | Find all starting indices where anagram of p exists in s | [NeetCode](https://youtu.be/G8xtZy0fDKg) |
| 567 | Check if any permutation of s1 is a substring of s2 | [NeetCode](https://youtu.be/UbyhOgBN834) |
| 647 | Count how many palindromic substrings exist | [NeetCode](https://youtu.be/4RACzI5-du8) |
| 8 | Convert string to integer (handle edge cases!) | [NeetCode](https://youtu.be/zwZw9RKZGJQ) |
| 22 | Generate all valid combinations of n pairs of parentheses | [NeetCode](https://youtu.be/s9fokUqJ76A) |
| 271 | Design encode/decode for list of strings | [NeetCode](https://youtu.be/B1k_sxOSgv8) |

### 🔴 Hard Problems Explained

| # | What You're Asked To Do | 📺 Video |
|---|-------------------------|----------|
| 76 | Find smallest window in S containing all chars of T | [NeetCode](https://youtu.be/jSto0O4AJbM) |
| 10 | Implement regex matching with '.' and '*' | [NeetCode](https://youtu.be/HAA8mgxlov8) |
| 32 | Find length of longest valid parentheses substring | [NeetCode](https://youtu.be/VdQuwtEd10M) |

---

## 🧭 Core Path (Do In This Order)

**Checkpoint:**
- [ ] Basic string operations done
- [ ] Palindrome patterns done
- [ ] Anagram patterns done
- [ ] Sliding window on strings done

---

## 🟢 Easy Problems (Start Here!)

### Foundation (Do These First!)

| # | Problem | Pattern | Status | Notes |
|---|---------|---------|--------|-------|
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Two Pointers | ☐ | In-place, swap ends |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | ☐ | Skip non-alphanumeric |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | HashMap | ☐ | Count frequencies |
| 387 | [First Unique Character](https://leetcode.com/problems/first-unique-character-in-a-string/) | HashMap | ☐ | Two passes |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | String Compare | ☐ | Shrink prefix |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Two Pointers | ☐ | Match in order |

### More Easy Practice

| # | Problem | Pattern | Status | Notes |
|---|---------|---------|--------|-------|
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | HashMap | ☐ | Count pairs |
| 205 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | HashMap | ☐ | Two-way mapping |
| 290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | HashMap | ☐ | Bijection check |
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | String Build | ☐ | Classic |
| 28 | [Find Index of First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | String Search | ☐ | Use find() or implement |
| 541 | [Reverse String II](https://leetcode.com/problems/reverse-string-ii/) | Two Pointers | ☐ | Reverse every 2k chars |
| 557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | Two Pointers | ☐ | Reverse each word |
| 680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Two Pointers | ☐ | Can delete one char |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | String | ☐ | s+s contains rotation |

---

## 🟡 Medium Problems (Level Up!)

### Sliding Window Pattern

| # | Problem | Sub-pattern | Status | Notes |
|---|---------|-------------|--------|-------|
| 3 | [Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Variable Window | ☐ | **MUST KNOW!** |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Variable Window | ☐ | Track max freq |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Fixed Window | ☐ | Anagram in window |
| 438 | [Find All Anagrams](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Fixed Window | ☐ | Similar to #567 |
| 1456 | [Max Vowels in Substring](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Fixed Window | ☐ | Count vowels |

### Palindrome Pattern

| # | Problem | Sub-pattern | Status | Notes |
|---|---------|-------------|--------|-------|
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Expand Center | ☐ | **MUST KNOW!** |
| 647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Expand Center | ☐ | Count all |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Backtracking | ☐ | Find all ways |

### Anagram/HashMap Pattern

| # | Problem | Sub-pattern | Status | Notes |
|---|---------|-------------|--------|-------|
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | HashMap | ☐ | **MUST KNOW!** |
| 451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | HashMap | ☐ | Sort by count |

### Two Pointers Pattern

| # | Problem | Sub-pattern | Status | Notes |
|---|---------|-------------|--------|-------|
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | Two Pointers | ☐ | Handle spaces |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | Two Pointers | ☐ | In-place compress |

### Other Medium

| # | Problem | Pattern | Status | Notes |
|---|---------|---------|--------|-------|
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | Parsing | ☐ | Edge cases! |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Backtracking | ☐ | Track open/close |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Stack | ☐ | Handle ".." |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | DP | ☐ | Can segment? |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Stack | ☐ | +, -, *, / |
| 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Design | ☐ | Length prefix |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Greedy | ☐ | * can be ( ) or empty |

---

## 🔴 Hard Problems (Master Level!)

| # | Problem | Pattern | Status | Notes |
|---|---------|---------|--------|-------|
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding Window | ☐ | **MUST KNOW!** |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | DP | ☐ | . and * |
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | DP | ☐ | ? and * |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Stack/DP | ☐ | Multiple approaches |
| 115 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | DP | ☐ | Count ways |

---

## 📅 Study Plan

### Week 1: Foundation
- Day 1-2: Reverse String, Valid Palindrome, Valid Anagram
- Day 3-4: First Unique Character, Longest Common Prefix
- Day 5-6: Is Subsequence, Valid Palindrome II
- Day 7: Review and practice

### Week 2: Core Patterns
- Day 1-2: Longest Substring Without Repeating (practice until instant)
- Day 3-4: Longest Palindromic Substring, Palindromic Substrings
- Day 5-6: Group Anagrams, Find All Anagrams
- Day 7: Review sliding window pattern

### Week 3: Advanced
- Day 1-2: Permutation in String, Minimum Window Substring
- Day 3-4: Generate Parentheses, Word Break
- Day 5-6: String Compression, Encode/Decode Strings
- Day 7: Hard problems practice

---

## 🎯 Must-Know Problems (Top 10)

These problems appear frequently in interviews:

1. **Valid Palindrome** (#125) - Two Pointers
2. **Valid Anagram** (#242) - HashMap
3. **Longest Substring Without Repeating** (#3) - Sliding Window
4. **Longest Palindromic Substring** (#5) - Expand Center
5. **Group Anagrams** (#49) - HashMap
6. **Minimum Window Substring** (#76) - Sliding Window
7. **Generate Parentheses** (#22) - Backtracking
8. **Longest Common Prefix** (#14) - String Compare
9. **String to Integer** (#8) - Parsing
10. **Encode and Decode Strings** (#271) - Design

---

## 📝 Notes Template

```markdown
## Problem Name (#Number)
**Difficulty:** Easy/Medium/Hard
**Date:** 
**Time:** X minutes

### Approach
- 

### Key Insight
- 

### Mistakes Made
- 

### Time/Space Complexity
- Time: O()
- Space: O()
```

---

## 🏆 Milestones

- [ ] Complete all Easy problems
- [ ] Complete "Must-Know" problems
- [ ] Solve sliding window problems < 15 min
- [ ] Solve palindrome problems < 15 min
- [ ] Can explain all patterns without looking

---

> 💪 **Remember:** Strings are just arrays of characters. Many array techniques apply!
