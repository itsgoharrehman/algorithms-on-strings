# python3
import sys


def build_trie(patterns):
  tree = {0: {}}
  node_count = 1

  for pattern in patterns:
    current_node = 0
    for char in pattern:
      if char in tree[current_node]:
        current_node = tree[current_node][char]
      else:
        tree[current_node][char] = node_count
        tree[node_count] = {}
        current_node = node_count
        node_count += 1
  return tree


def solve(text, patterns):
  tree = build_trie(patterns)
  results = []
  text_len = len(text)

  for i in range(text_len):
    current_node = 0
    for j in range(i, text_len):
      char = text[j]
      if char in tree[current_node]:
        current_node = tree[current_node][char]
        if not tree[current_node]:  # Leaf node reached
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