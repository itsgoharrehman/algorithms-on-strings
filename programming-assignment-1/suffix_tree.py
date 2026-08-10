# python3
import sys


class Node:

  def __init__(self):
    self.edges = {}


def build_suffix_tree(text):
  root = Node()
  n = len(text)

  for i in range(n):
    curr = root
    j = i
    while j < n:
      char = text[j]
      if char in curr.edges:
        child, start, length = curr.edges[char]
        k = 0
        while k < length and j + k < n and text[j + k] == text[start + k]:
          k += 1

        if k == length:
          curr = child
          j += length
        else:
          mid_node = Node()
          mid_node.edges[text[start + k]] = (child, start + k, length - k)
          curr.edges[char] = (mid_node, start, k)

          leaf_node = Node()
          mid_node.edges[text[j + k]] = (leaf_node, j + k, n - (j + k))
          break
      else:
        leaf_node = Node()
        curr.edges[char] = (leaf_node, j, n - j)
        break

  return root


def get_edge_labels(root, text):
  labels = []
  stack = [root]
  while stack:
    node = stack.pop()
    for child, start, length in node.edges.values():
      labels.append(text[start : start + length])
      stack.append(child)
  return labels


if __name__ == "__main__":
  input_data = sys.stdin.read().split()
  if input_data:
    text = input_data[0]
    root = build_suffix_tree(text)
    labels = get_edge_labels(root, text)
    print("\n".join(labels))