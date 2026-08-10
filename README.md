# Algorithms on Strings

This repository contains solutions to programming assignments for the **Algorithms on Strings** course (part of the Coursera Data Structures and Algorithms Specialization).

All implementations are written in **Python 3**.

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
├── programming-assignment-2/
│   ├── bwt.py
│   ├── bwtinverse.py
│   ├── bwmatching.py
│   └── suffix_array.py
└── programming-assignment-3/
    ├── kmp.py
    ├── suffix_array_long.py
    ├── suffix_array_matching.py
    └── suffix_tree_from_array.py
```

---

## 💡 Assignments Overview

### 🔹 Programming Assignment 1: Trie & Suffix Tree Construction

| File | Description |
| :--- | :--- |
| [`trie.py`](./programming-assignment-1/trie.py) | Builds a Trie data structure from a list of input patterns. |
| [`trie_matching.py`](./programming-assignment-1/trie_matching.py) | Implements multiple pattern matching using a Trie. |
| [`trie_matching_extended.py`](./programming-assignment-1/trie_matching_extended.py) | Extends Trie matching to handle cases where one pattern is a prefix of another. |
| [`suffix_tree.py`](./programming-assignment-1/suffix_tree.py) | Builds a Suffix Tree for a given string and outputs edge labels. |
| [`non_shared_substring.py`](./programming-assignment-1/non_shared_substring.py) | Finds the shortest substring of string `Text1` that does not appear in string `Text2`. |

---

## 🔹 Programming Assignment 2: Burrows-Wheeler Transform & Suffix Array

| File | Description |
| :--- | :--- |
| [`bwt.py`](./programming-assignment-2/bwt.py) | Computes the Burrows-Wheeler Transform (BWT) of a string. |
| [`bwtinverse.py`](./programming-assignment-2/bwtinverse.py) | Reconstructs the original string from its Burrows-Wheeler Transform using Last-to-First (LF) mapping. |
| [`bwmatching.py`](./programming-assignment-2/bwmatching.py) | Efficiently counts pattern occurrences in a text using BWT and count tables. |
| [`suffix_array.py`](./programming-assignment-2/suffix_array.py) | Constructs the Suffix Array of a string by sorting suffix indices lexicographically. |

---

## 🔹 Programming Assignment 3: Knuth-Morris-Pratt & Advanced Suffix Arrays

| File | Description |
| :--- | :--- |
| [`kmp.py`](./programming-assignment-3/kmp.py) | Implements the Knuth-Morris-Pratt (KMP) pattern matching algorithm. |
| [`suffix_array_long.py`](./programming-assignment-3/suffix_array_long.py) | Builds a Suffix Array for long strings in $O(|S| \log |S|)$ time using prefix doubling. |
| [`suffix_array_matching.py`](./programming-assignment-3/suffix_array_matching.py) | Performs fast pattern matching using a Suffix Array and binary search. |
| [`suffix_tree_from_array.py`](./programming-assignment-3/suffix_tree_from_array.py) | Constructs a Suffix Tree directly from a Suffix Array and LCP array in linear time. |

---

## 🚀 Usage

Run any script using Python 3 and provide input via standard input (`stdin`):

```bash
python programming-assignment-3/kmp.py < input.txt
```

---

## 📜 Requirements

- Python `3.x`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

