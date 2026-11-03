<div align="center">
  <h1>algorithms-on-strings</h1>
  <p>Pattern matching, suffix trees, suffix arrays, and Burrows-Wheeler transform algorithms for UC San Diego.</p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"></a>
    <img src="https://img.shields.io/badge/Institution-UC_San_Diego-182B49?style=flat-square&logo=coursera&logoColor=white" alt="UC San Diego">
    <img src="https://img.shields.io/badge/Language-Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Focus-String_Algorithms_&_Indexing-E34F26?style=flat-square&logo=thealgorithms&logoColor=white" alt="String Algorithms">
    <a href="https://github.com/itsgoharrehman/algorithms-on-strings/stargazers"><img src="https://img.shields.io/github/stars/itsgoharrehman/algorithms-on-strings?style=flat-square&logo=github&logoColor=white" alt="Stars"></a>
    <a href="https://github.com/itsgoharrehman/algorithms-on-strings/issues"><img src="https://img.shields.io/github/issues/itsgoharrehman/algorithms-on-strings?style=flat-square&logo=github&logoColor=white" alt="Issues"></a>
  </p>
</div>

---

> [!IMPORTANT]
> **Academic Honesty and Institutional Integrity**:
> This repository contains completed algorithmic coursework for the University of California San Diego's **Algorithms on Strings** course (part of the Computer Science Data Structures & Algorithms Specialization). In accordance with UCSD's Policy on Integrity of Scholarship and the Coursera Honor Code, students currently enrolled in the course are strictly prohibited from copying, plagiarizing, or submitting any part of these solutions. This repository exists solely for code review, pedagogical reference, and portfolio demonstration.

---

## Core String Algorithms & Asymptotic Complexity Matrix

The repository implements essential computational biology, string indexing, and compression algorithms:

| Module | Problem / Algorithm | Description & Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Assignment 1** | Trie Construction (`trie.py`) | Multi-pattern prefix dictionary tree | `O(TotalLength)` | `O(TotalLength)` |
| **Assignment 1** | Trie Pattern Matching (`trie_matching.py`) | Exact multi-pattern search in text | `O(|Text| * |Pattern|_max)` | `O(TrieSize)` |
| **Assignment 1** | Extended Trie Matching (`trie_matching_extended.py`) | Multi-pattern matching with pattern prefixes | `O(|Text| * |Pattern|_max)` | `O(TrieSize)` |
| **Assignment 1** | Suffix Tree (`suffix_tree.py`) | Compact edge-compressed suffix tree | `O(|Text|^2)` | `O(|Text|)` |
| **Assignment 1** | Non-Shared Substring (`non_shared_substring.py`) | Shortest distinct substring via generalized suffix tree | `O(|T_1| + |T_2|)` | `O(|T_1| + |T_2|)` |
| **Assignment 2** | Burrows-Wheeler Transform (`bwt.py`) | Text permutation for compression preprocessing | `O(|Text| log |Text|)` | `O(|Text|)` |
| **Assignment 2** | Inverse BWT (`bwtinverse.py`) | Reconstruction via First-Last (LF) mapping | `O(|Text|)` | `O(|Text|)` |
| **Assignment 2** | Better BWMatching (`bwmatching.py`) | Pattern count lookup via FirstOccurrence & Count tables | `O(|Pattern|)` | `O(|Text| * |Alphabet|)` |
| **Assignment 2** | Suffix Array (`suffix_array.py`) | Lexicographical suffix order sorting | `O(|Text| log |Text|)` | `O(|Text|)` |
| **Assignment 3** | Knuth-Morris-Pratt (`kmp.py`) | Linear-time exact matching via prefix function | `O(|Pattern| + |Text|)` | `O(|Pattern|)` |
| **Assignment 3** | Suffix Array for Large Text (`suffix_array_long.py`) | Cyclic shift doubling sort algorithm | `O(|Text| log |Text|)` | `O(|Text|)` |
| **Assignment 3** | Suffix Tree from Array (`suffix_tree_from_array.py`) | Linear reconstruction from Suffix and LCP arrays | `O(|Text|)` | `O(|Text|)` |

---

## Directory Structure

```
algorithms-on-strings/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml              # Defect reporting form
│   │   └── question.yml                # Conceptual algorithm question form
│   ├── PULL_REQUEST_TEMPLATE.md        # Academic integrity verification checklist
│   └── dependabot.yml                  # Weekly automated pip dependency scanner
├── programming-assignment-1/           # From Tries to Suffix Trees (prefix trees, non-shared substrings)
├── programming-assignment-2/           # Burrows-Wheeler Transform & Suffix Arrays (BWT, BWMatching)
├── programming-assignment-3/           # Advanced Pattern Matching (KMP algorithm, large suffix arrays)
├── requirements.txt                    # Testing dependencies
├── LICENSE                             # MIT License
├── SECURITY.md                         # Security policy and disclosure protocol
├── CONTRIBUTING.md                     # Academic archive contribution guidelines
└── CODE_OF_CONDUCT.md                 # Contributor Covenant v2.1
```

---

## Running and Testing Locally

### Prerequisites

* Python 3.10 or higher
* `pytest` for automated test execution

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/itsgoharrehman/algorithms-on-strings.git
   cd algorithms-on-strings
   ```

2. Install test dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run an algorithm script against input fixtures:
   ```bash
   python programming-assignment-2/bwt.py
   python programming-assignment-3/kmp.py
   python programming-assignment-3/suffix_array_long.py
   ```

---

## Academic Governance and Licensing

* **License**: Licensed under the terms of the [MIT License](LICENSE).
* **Security Policy**: See [SECURITY.md](SECURITY.md) for vulnerability disclosure.
* **Academic Guidelines**: See [CONTRIBUTING.md](CONTRIBUTING.md) regarding preservation of completed coursework.
