# LeetCode Practice — Claude Instructions

## Project Purpose
Roger is practicing Python interview questions by solving LeetCode problems.
For every solution submitted, Claude should:
1. Review correctness and identify any bugs
2. Analyze time and space complexity
3. Suggest improvements (more Pythonic style, better algorithm, edge cases)
4. Place the solution file in the correct topic folder
5. Update the README.md progress table

## Folder Structure
Solutions go in topic subfolders:
- `arrays/` — array manipulation, prefix sums, intervals
- `strings/` — string parsing, anagrams, palindromes
- `linked_lists/` — singly/doubly linked list operations
- `trees/` — BST, DFS, BFS, tries
- `graphs/` — DFS, BFS, topological sort, union-find
- `dynamic_programming/` — memoization, tabulation, knapsack
- `two_pointers/` — two-pointer and fast/slow pointer patterns
- `sliding_window/` — fixed and variable-size window problems
- `binary_search/` — binary search on arrays and answer space
- `stack_queue/` — monotonic stack, queue patterns
- `hash_maps/` — frequency counting, grouping
- `backtracking/` — permutations, combinations, subsets
- `sorting_searching/` — custom sort, merge sort patterns
- `math/` — number theory, bit manipulation

## File Naming
`<topic>/<leetcode_number>_<snake_case_title>.py`
Example: `arrays/001_two_sum.py`

## Solution File Format
Use `_template.py` as the base for every new solution.

## README Updates
After adding a solution, update the progress table in README.md:
- Add a row with: problem number, title (linked to LeetCode), difficulty, topic, solution file link
- Increment the stats counters (Total, Easy/Medium/Hard)

## Git Workflow
- Commit each solution individually with message: `Add #<number> <Title> (<Difficulty>)`
- Push to `git@github.com:roger894351/leetcode-practice.git` after each commit

## User Profile
- Language: Python
- Goal: Interview preparation
- Feedback style: Direct — show improved code, explain the why
