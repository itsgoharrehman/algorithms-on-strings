# python3
import sys

def sort_characters(s):
    order = [0] * len(s)
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    chars = sorted(count.keys())
    prev = 0
    for char in chars:
        count[char], prev = prev, prev + count[char]
        
    for i, char in enumerate(s):
        order[count[char]] = i
        count[char] += 1
    return order

def compute_char_classes(s, order):
    eq_class = [0] * len(s)
    eq_class[order[0]] = 0
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i - 1]]:
            eq_class[order[i]] = eq_class[order[i - 1]] + 1
        else:
            eq_class[order[i]] = eq_class[order[i - 1]]
    return eq_class

def sort_doubled(s, l, order, eq_class):
    count = [0] * len(s)
    new_order = [0] * len(s)
    for i in range(len(s)):
        count[eq_class[i]] += 1
    for i in range(1, len(s)):
        count[i] += count[i - 1]
    for i in range(len(s) - 1, -1, -1):
        start = (order[i] - l + len(s)) % len(s)
        cl = eq_class[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def update_classes(new_order, eq_class, l):
    n = len(new_order)
    new_class = [0] * n
    new_class[new_order[0]] = 0
    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i - 1]
        mid_cur = (cur + l) % n
        mid_prev = (prev + l) % n
        if eq_class[cur] != eq_class[prev] or eq_class[mid_cur] != eq_class[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class

def build_suffix_array(text):
    order = sort_characters(text)
    eq_class = compute_char_classes(text, order)
    l = 1
    while l < len(text):
        order = sort_doubled(text, l, order, eq_class)
        eq_class = update_classes(order, eq_class, l)
        l *= 2
    return order

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))