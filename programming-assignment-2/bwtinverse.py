# python3
import sys

def inverse_bwt(bwt: str) -> str:
    n = len(bwt)
    # Pair characters with their original 0-based position in BWT
    first_col = sorted((char, i) for i, char in enumerate(bwt))
    
    # LF mapping: maps BWT index i -> row index in first_col
    lf = [0] * n
    for row_idx, (_, orig_idx) in enumerate(first_col):
        lf[orig_idx] = row_idx
        
    # Start from '$' in BWT
    curr = bwt.find('$')
    res = []
    for _ in range(n):
        res.append(bwt[curr])
        curr = lf[curr]
        
    return "".join(reversed(res))

if __name__ == '__main__':
    bwt = sys.stdin.read().strip()
    if bwt:
        print(inverse_bwt(bwt))