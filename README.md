# Algorithms on Strings

This repository contains solutions to programming assignments for the **Algorithms on Strings** course (part of the Coursera Data Structures and Algorithms Specialization).

All implementations are in **Python 3**.

---

## 📁 Repository Structure

```text
algorithms-on-strings/
├── programming-assignment-1/
│   ├── trie.py
│   ├── trie_matching.py
│   ├── trie_matching_extended.py
│   ├── suffix_tree.py
│   └── non_shared_substring.py
└── programming-assignment-2/
    ├── bwt.py
    ├── bwtinverse.py
    ├── bwmatching.py
    └── suffix_array.py
```

---

## 💡 Assignments Overview

### 🔹 Programming Assignment 1: Trie & Suffix Tree Construction

| File | Description |
| :--- | :--- |
| [`trie.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-1/trie.py) | Builds a Trie data structure from a list of input patterns. |
| [`trie_matching.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-1/trie_matching.py) | Implements multiple pattern matching using a Trie. |
| [`trie_matching_extended.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-1/trie_matching_extended.py) | Extends Trie matching to handle cases where one pattern is a prefix of another. |
| [`suffix_tree.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-1/suffix_tree.py) | Builds a Suffix Tree for a given string and outputs edge labels. |
| [`non_shared_substring.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-1/non_shared_substring.py) | Finds the shortest substring of string `Text1` that does not appear in string `Text2`. |

---

### 🔹 Programming Assignment 2: Burrows-Wheeler Transform & Suffix Array

| File | Description |
| :--- | :--- |
| [`bwt.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-2/bwt.py) | Computes the Burrows-Wheeler Transform (BWT) of a string. |
| [`bwtinverse.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-2/bwtinverse.py) | Reconstructs the original string from its Burrows-Wheeler Transform using Last-to-First (LF) mapping. |
| [`bwmatching.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-2/bwmatching.py) | Efficiently counts pattern occurrences in a text using BWT and count tables. |
| [`suffix_array.py`](file:///c:/Users/Gohar%20Rehman/Desktop/algorithms-on-strings/programming-assignment-2/suffix_array.py) | Constructs the Suffix Array of a string by sorting suffix indices lexicographically. |

---

## 🚀 Usage

Run any script using Python 3 and provide input via standard input (`stdin`):

### Example: Running `trie.py`
```bash
python programming-assignment-1/trie.py < input.txt
```

### Example: Running `bwt.py`
```bash
python programming-assignment-2/bwt.py
# Input: AAAB$
# Output: TEX_BWT_OUTPUT
```

---

## 📜 Requirements

- Python `3.x`
