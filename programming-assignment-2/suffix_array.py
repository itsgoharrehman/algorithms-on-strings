# python3
import sys

def build_suffix_array(text: str) -> list:
    # Sort starting indices based on suffix lexicographical order
    return sorted(range(len(text)), key=lambda i: text[i:])

if __name__ == '__main__':
    text = sys.stdin.read().strip()
    if text:
        print(*build_suffix_array(text))