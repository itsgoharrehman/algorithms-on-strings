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


if __name__ == "__main__":
  input_data = sys.stdin.read().split()
  if input_data:
    n = int(input_data[0])
    patterns = input_data[1 : 1 + n]
    tree = build_trie(patterns)

    for node in tree:
      for char, next_node in tree[node].items():
        print("{0}->{1}:{2}".format(node, next_node, char))