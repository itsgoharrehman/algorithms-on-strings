# python3
import sys

def build_bwt(text: str) -> str:
    n = len(text)
    # Generate all cyclic rotations and sort them lexicographically
    rotations = sorted(text[i:] + text[:i] for i in range(n))
    # Return the last column of the matrix
    return "".join(r[-1] for r in rotations)

if __name__ == '__main__':
    text = sys.stdin.read().strip()
    if text:
        print(build_bwt(text))