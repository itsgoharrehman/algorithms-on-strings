# python3
import sys

def compute_prefix_function(p):
    s = [0] * len(p)
    border = 0
    for i in range(1, len(p)):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def find_pattern(pattern, text):
    concat = pattern + '$' + text
    s = compute_prefix_function(concat)
    result = []
    p_len = len(pattern)
    
    for i in range(p_len + 1, len(concat)):
        if s[i] == p_len:
            result.append(i - 2 * p_len)
    return result

if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))