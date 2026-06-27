<div align="center">

<img src="https://leetcode.com/static/images/LeetCode_logo_rvs.png" alt="LeetCode Logo" width="80"/>

# 🚀 LeetCode Solutions — Ayush Vaidya

**A curated, optimized collection of LeetCode problem solutions tracking my DSA mastery journey.**

[![LeetCode](https://img.shields.io/badge/LeetCode-Ayush--2703-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/Ayush-2703/)
[![GitHub](https://img.shields.io/badge/GitHub-Ayush--2703-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayush-2703)
[![Language](https://img.shields.io/badge/Language-Java%20%7C%20C%2B%2B%20%7C%20Python-blue?style=for-the-badge)](https://github.com/Ayush-2703/LeetCode_Problems)
[![Repo Stars](https://img.shields.io/github/stars/Ayush-2703/LeetCode_Problems?style=for-the-badge&color=yellow)](https://github.com/Ayush-2703/LeetCode_Problems/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Ayush-2703/LeetCode_Problems?style=for-the-badge&color=brightgreen)](https://github.com/Ayush-2703/LeetCode_Problems/commits/main)

---

> *"The journey of 1,000 problems begins with a single Array."*

</div>

---

## 📊 Live LeetCode Stats

<div align="center">

<img src="https://leetcard.jacoblin.cool/Ayush-2703?theme=dark&font=source_code_pro&ext=heatmap&border=1&radius=10" alt="LeetCode Stats Card" width="500"/>

</div>

---

## 📋 Table of Contents

- [About This Repository](#-about-this-repository)
- [Progress Tracker](#-progress-tracker)
- [Repository Structure](#-repository-structure)
- [Topics Covered](#-topics-covered)
- [Solutions Index](#-solutions-index)
- [How to Use](#-how-to-use)
- [Optimization Philosophy](#-optimization-philosophy)
- [Resources & Roadmap](#-resources--roadmap)
- [Connect With Me](#-connect-with-me)

---

## 🎯 About This Repository

This repository is my **living DSA notebook** — a continuously updated log of optimized solutions to LeetCode problems. Every solution here is:

- ✅ **Accepted** on LeetCode (verified submission)
- ⚡ **Optimized** for both time and space complexity
- 📝 **Documented** with approach explanation and complexity analysis
- 🏷️ **Tagged** by topic, difficulty, and pattern

**Target:** Top tech companies (FAANG / MAANG) interview preparation.

---

## 📈 Progress Tracker

<div align="center">

| Difficulty | Solved | Target | Progress |
|:---:|:---:|:---:|:---|
| 🟢 Easy | 80+ | 200 | `████████████░░░░░░░░` 60% |
| 🟡 Medium | 60+ | 300 | `████████░░░░░░░░░░░░` 40% |
| 🔴 Hard | 15+ | 100 | `███░░░░░░░░░░░░░░░░░` 15% |
| **Total** | **155+** | **600** | **`████████░░░░░░░░░░░░` 26%** |

> 📌 *Update this table as you solve more problems.*

</div>

---

## 🗂️ Repository Structure

```
LeetCode_Problems/
│
├── 📁 Arrays/
│   ├── Easy/
│   │   ├── 0001_Two_Sum.java
│   │   └── ...
│   ├── Medium/
│   └── Hard/
│
├── 📁 Strings/
├── 📁 LinkedList/
├── 📁 Trees/
├── 📁 Graphs/
├── 📁 Dynamic_Programming/
├── 📁 Backtracking/
├── 📁 Binary_Search/
├── 📁 Heap_Priority_Queue/
├── 📁 Stacks_Queues/
├── 📁 Sliding_Window/
├── 📁 Two_Pointers/
├── 📁 Greedy/
├── 📁 Math/
│
└── README.md
```

### 📄 Per-File Convention

Each solution file follows this template:

```java
/**
 * Problem: 1. Two Sum
 * Link: https://leetcode.com/problems/two-sum/
 * Difficulty: Easy
 * Topics: Array, Hash Map
 *
 * Approach:
 *   Use a HashMap to store value → index mappings.
 *   For each element, check if its complement exists in the map.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement))
                return new int[]{map.get(complement), i};
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

---

## 🧩 Topics Covered

<div align="center">

| # | Topic | Problems Solved | Key Patterns |
|:---:|:---|:---:|:---|
| 1 | 📦 Arrays | 30+ | Prefix Sum, Kadane's, Sorting |
| 2 | 🔤 Strings | 20+ | Sliding Window, Two Pointers, KMP |
| 3 | 🔗 Linked Lists | 15+ | Fast & Slow Pointers, Reversal |
| 4 | 🌳 Trees & BST | 20+ | BFS, DFS, In/Pre/Post-order |
| 5 | 🕸️ Graphs | 15+ | DFS, BFS, Union-Find, Dijkstra |
| 6 | 💡 Dynamic Programming | 20+ | Top-Down, Bottom-Up, Memoization |
| 7 | 🔙 Backtracking | 8+ | Permutations, Subsets, N-Queens |
| 8 | 🔍 Binary Search | 12+ | Search Space Reduction, Rotated Arrays |
| 9 | 📊 Heaps & Priority Queues | 8+ | Top-K, Merge K Sorted |
| 10 | 📚 Stacks & Queues | 10+ | Monotonic Stack, BFS Queue |
| 11 | 🪟 Sliding Window | 8+ | Fixed & Variable Window |
| 12 | 👆 Two Pointers | 10+ | Opposite Ends, Same Direction |
| 13 | 💰 Greedy | 8+ | Interval Scheduling, Huffman |
| 14 | 🔢 Math & Bit Manipulation | 8+ | XOR, Bit Counting, Modular |

</div>

---

## 📚 Solutions Index

> Click any problem title to navigate directly to the LeetCode problem page.

### 🟢 Easy

| # | Problem | Topic | Time | Space | Solution |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Array, Hash Map | O(n) | O(n) | [Java](Arrays/Easy/0001_Two_Sum.java) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Math | O(log n) | O(1) | [Java](Math/Easy/0009_Palindrome_Number.java) |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | String | O(n·m) | O(1) | [Java](Strings/Easy/0014_Longest_Common_Prefix.java) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | O(n) | O(n) | [Java](Stacks_Queues/Easy/0020_Valid_Parentheses.java) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List | O(n+m) | O(1) | [Java](LinkedList/Easy/0021_Merge_Two_Sorted_Lists.java) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | DP | O(n) | O(1) | [Java](Dynamic_Programming/Easy/0070_Climbing_Stairs.java) |
| 104 | [Max Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Tree, DFS | O(n) | O(h) | [Java](Trees/Easy/0104_Max_Depth_Binary_Tree.java) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Array, Greedy | O(n) | O(1) | [Java](Arrays/Easy/0121_Best_Time_Buy_Sell_Stock.java) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List | O(n) | O(1) | [Java](LinkedList/Easy/0141_Linked_List_Cycle.java) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List | O(n) | O(1) | [Java](LinkedList/Easy/0206_Reverse_Linked_List.java) |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Tree, BFS | O(n) | O(n) | [Java](Trees/Easy/0226_Invert_Binary_Tree.java) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | String, Hash | O(n) | O(1) | [Java](Strings/Easy/0242_Valid_Anagram.java) |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Array, Math | O(n) | O(1) | [Java](Arrays/Easy/0268_Missing_Number.java) |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Two Pointers | O(n) | O(1) | [Java](Two_Pointers/Easy/0344_Reverse_String.java) |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Binary Search | O(log n) | O(1) | [Java](Binary_Search/Easy/0704_Binary_Search.java) |

---

### 🟡 Medium

| # | Problem | Topic | Time | Space | Solution |
|:---:|:---|:---:|:---:|:---:|:---:|
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | O(n) | O(k) | [Java](Sliding_Window/Medium/0003_Longest_Substring_No_Repeat.java) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Array, Two Ptr | O(n²) | O(1) | [Java](Arrays/Medium/0015_3Sum.java) |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Binary Search | O(log n) | O(1) | [Java](Binary_Search/Medium/0033_Search_Rotated_Sorted_Array.java) |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Backtracking | O(n·n!) | O(n) | [Java](Backtracking/Medium/0046_Permutations.java) |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Array, Sorting | O(n log n) | O(n) | [Java](Arrays/Medium/0056_Merge_Intervals.java) |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Backtracking | O(n·2ⁿ) | O(n) | [Java](Backtracking/Medium/0078_Subsets.java) |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Tree, BFS | O(n) | O(n) | [Java](Trees/Medium/0102_Level_Order_Traversal.java) |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Array, HashSet | O(n) | O(n) | [Java](Arrays/Medium/0128_Longest_Consecutive_Sequence.java) |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Binary Search | O(log n) | O(1) | [Java](Binary_Search/Medium/0153_Min_Rotated_Sorted_Array.java) |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Graph, DFS | O(m·n) | O(m·n) | [Java](Graphs/Medium/0200_Number_Of_Islands.java) |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Graph, Topological | O(V+E) | O(V+E) | [Java](Graphs/Medium/0207_Course_Schedule.java) |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Array | O(n) | O(1) | [Java](Arrays/Medium/0238_Product_Array_Except_Self.java) |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | DP, Binary Search | O(n log n) | O(n) | [Java](Dynamic_Programming/Medium/0300_Longest_Increasing_Subsequence.java) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | DP | O(amount·n) | O(amount) | [Java](Dynamic_Programming/Medium/0322_Coin_Change.java) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Heap, Bucket Sort | O(n) | O(n) | [Java](Heap_Priority_Queue/Medium/0347_Top_K_Frequent_Elements.java) |
| 437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Tree, Prefix Sum | O(n) | O(n) | [Java](Trees/Medium/0437_Path_Sum_III.java) |

---

### 🔴 Hard

| # | Problem | Topic | Time | Space | Solution |
|:---:|:---|:---:|:---:|:---:|:---:|
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary Search | O(log(m+n)) | O(1) | [Java](Binary_Search/Hard/0004_Median_Two_Sorted_Arrays.java) |
| 23 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap, Linked List | O(n log k) | O(k) | [Java](Heap_Priority_Queue/Hard/0023_Merge_K_Sorted_Lists.java) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | O(n) | O(1) | [Java](Two_Pointers/Hard/0042_Trapping_Rain_Water.java) |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding Window | O(n) | O(k) | [Java](Sliding_Window/Hard/0076_Min_Window_Substring.java) |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Stack | O(n) | O(n) | [Java](Stacks_Queues/Hard/0084_Largest_Rectangle_Histogram.java) |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Tree, DFS | O(n) | O(h) | [Java](Trees/Hard/0124_BT_Max_Path_Sum.java) |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Tree, BFS | O(n) | O(n) | [Java](Trees/Hard/0297_Serialize_Deserialize_BT.java) |

> 📌 *This is a curated index. See individual topic folders for all files.*

---

## 🛠️ How to Use

### Clone the Repository

```bash
git clone https://github.com/Ayush-2703/LeetCode_Problems.git
cd LeetCode_Problems
```

### Run a Solution Locally (Java example)

```bash
# Compile
javac Arrays/Easy/0001_Two_Sum.java

# Run
java -cp Arrays/Easy Solution
```

### Adding a New Solution

1. Navigate to the correct topic folder and difficulty subfolder
2. Create file: `XXXX_Problem_Name.java` (using the LeetCode number)
3. Paste the solution with the header comment template (see above)
4. Add a row to the Solutions Index table in this README
5. Commit with a descriptive message:

```bash
git add .
git commit -m "✅ Add #1234 - Problem Name [Medium] [Graph/BFS]"
git push origin main
```

---

## ⚡ Optimization Philosophy

Every solution in this repo is evaluated against three tiers before being committed:

```
Tier 1 — Correctness     → Does it pass all LeetCode test cases?
Tier 2 — Complexity      → Is Big-O time and space optimal or near-optimal?
Tier 3 — Readability     → Is it clean enough to explain in a 45-minute interview?
```

### Common Patterns I Use

<details>
<summary><b>📌 Click to expand — Pattern Cheatsheet</b></summary>

| Pattern | When to Use | Example Problems |
|:---|:---|:---|
| **Two Pointers** | Sorted arrays, palindromes, pair sums | 3Sum, Container With Most Water |
| **Sliding Window** | Contiguous subarray/substring problems | Longest Substring, Min Window Substring |
| **Fast & Slow Pointers** | Cycle detection, middle of linked list | Linked List Cycle, Happy Number |
| **Merge Intervals** | Overlapping ranges | Merge Intervals, Insert Interval |
| **Cyclic Sort** | Problems involving 1→N range arrays | Missing Number, Find All Duplicates |
| **In-place Reversal (LL)** | Reversing without extra space | Reverse LL, Reverse Sublist |
| **Tree BFS** | Level-order traversal, shortest path | Level Order Traversal, Right Side View |
| **Tree DFS** | Path sums, max depth, subtree checks | Path Sum, Lowest Common Ancestor |
| **Two Heaps** | Median of stream, task scheduling | Find Median from Data Stream |
| **Subsets / Backtracking** | Generating combinations/permutations | Subsets, Permutations, Combination Sum |
| **Binary Search** | Sorted arrays, search space reduction | Search in Rotated Array, Koko Eating Bananas |
| **Top K Elements** | Kth largest/smallest, frequent elements | Top K Frequent, Kth Largest in Stream |
| **K-way Merge** | Merging K sorted arrays/lists | Merge K Sorted Lists, Smallest Range |
| **Monotonic Stack** | Next greater/smaller element | Daily Temperatures, Largest Rectangle |
| **DP — Knapsack** | Subset sums, capacity constraints | 0/1 Knapsack, Coin Change |
| **DP — LCS/LIS** | Subsequence problems | LCS, LIS, Edit Distance |
| **Graph — Union Find** | Connectivity, cycle detection | Number of Provinces, Redundant Connection |
| **Graph — Topological Sort** | Dependencies, ordering | Course Schedule, Alien Dictionary |

</details>

---

## 📚 Resources & Roadmap

### 🗺️ Recommended Study Order

```
Phase 1 — Foundations (2–3 weeks)
  Arrays → Strings → Linked Lists → Stacks & Queues

Phase 2 — Core DSA (4–6 weeks)
  Trees → Graphs → Binary Search → Two Pointers → Sliding Window

Phase 3 — Advanced (4–6 weeks)
  Dynamic Programming → Backtracking → Heaps → Tries → Greedy

Phase 4 — Interview Prep (2–4 weeks)
  Blind 75 → NeetCode 150 → Company-specific lists
```

### 📖 Top Study Resources

| Resource | Link | Type |
|:---|:---|:---:|
| NeetCode Roadmap | [neetcode.io/roadmap](https://neetcode.io/roadmap) | Free |
| Striver's A2Z DSA Sheet | [takeuforward.org](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) | Free |
| Grokking Patterns | [designgurus.io](https://www.designgurus.io/) | Paid |
| CLRS — Introduction to Algorithms | Book | Paid |
| LeetCode 75 Study Plan | [leetcode.com/studyplan/leetcode-75](https://leetcode.com/studyplan/leetcode-75/) | Free |

### 🏷️ Must-Solve Lists

- 🔥 **[Blind 75](https://leetcode.com/list/xi4ci4ig/)** — Classic FAANG interview set
- 💯 **[NeetCode 150](https://neetcode.io/practice)** — Extended curated list
- 🏢 **Company-Wise Lists** — Google, Amazon, Meta, Microsoft, Apple

---

## 🤝 Connect With Me

<div align="center">

[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/Ayush-2703/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayush-2703)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/)

**If this repo helped you, please ⭐ star it — it keeps me motivated to keep solving!**

</div>

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE).

Solutions are for **learning and reference purposes only.**
Please attempt problems independently before viewing solutions.

---

<div align="center">

*Last updated: June 2026 · Maintained by [Ayush-2703](https://github.com/Ayush-2703)*

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=Ayush-2703.LeetCode_Problems&color=blue&style=flat-square)

</div>
