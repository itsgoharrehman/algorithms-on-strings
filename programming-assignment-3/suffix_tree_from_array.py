# python3
import sys

# Increase recursion depth if traversing deep trees recursively
sys.setrecursionlimit(200000)

class SuffixTreeNode:
    def __init__(self, parent, depth, start, end):
        self.parent = parent
        self.children = {}
        self.depth = depth
        self.start = start
        self.end = end

def build_suffix_tree(text, order, lcp):
    root = SuffixTreeNode(None, 0, -1, -1)
    lcp_val = 0
    cur_node = root

    for i in range(len(text)):
        suffix = order[i]
        while cur_node.depth > lcp_val:
            cur_node = cur_node.parent

        if cur_node.depth == lcp_val:
            leaf = SuffixTreeNode(cur_node, len(text) - suffix, suffix + cur_node.depth, len(text))
            cur_node.children[text[suffix + cur_node.depth]] = leaf
            cur_node = leaf
        else:
            edge_start = order[i - 1] + cur_node.depth
            offset = lcp_val - cur_node.depth
            mid_char = text[edge_start]
            child_node = cur_node.children[mid_char]

            mid_node = SuffixTreeNode(cur_node, lcp_val, child_node.start, child_node.start + offset)
            child_node.start += offset
            child_node.parent = mid_node
            mid_node.children[text[child_node.start]] = child_node

            cur_node.children[mid_char] = mid_node

            leaf = SuffixTreeNode(mid_node, len(text) - suffix, suffix + lcp_val, len(text))
            mid_node.children[text[suffix + lcp_val]] = leaf
            cur_node = leaf

        if i < len(text) - 1:
            lcp_val = lcp[i]

    return root

def print_edges(text, node):
    for char, child in node.children.items():
        print("{0} {1}".format(child.start, child.end))
        print_edges(text, child)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    order = list(map(int, sys.stdin.readline().split()))
    lcp = list(map(int, sys.stdin.readline().split()))
    
    root = build_suffix_tree(text, order, lcp)
    print(text)
    print_edges(text, root)