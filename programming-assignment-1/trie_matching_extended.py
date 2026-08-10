# python3
import sys


class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_end = False


def build_trie(patterns):
  root = TrieNode()
  for pattern in patterns:
    current = root
    for char in pattern:
      if char not in current.children:
        current.children[char] = TrieNode()
      current = current.children[char]
    current.is_end = True
  return root


def solve(text, patterns):
  root = build_trie(patterns)
  results = []
  text_len = len(text)

  for i in range(text_len):
    current = root
    for j in range(i, text_len):
      char = text[j]
      if char in current.children:
        current = current.children[char]
        if current.is_end:
          results.append(i)
          break
      else:
        break

  return results


if __name__ == "__main__":
  input_data = sys.stdin.read().split()
  if input_data:
    text = input_data[0]
    n = int(input_data[1])
    patterns = input_data[2 : 2 + n]
    ans = solve(text, patterns)
    print(" ".join(map(str, ans)))