# python3
import sys

def preprocess_bwt(bwt: str):
    alphabet = ['$', 'A', 'C', 'G', 'T']
    n = len(bwt)
    
    # FirstOccurrence[char]: 0-based index of first occurrence in sorted BWT
    first_occurrence = {}
    sorted_bwt = sorted(bwt)
    for i, char in enumerate(sorted_bwt):
        if char not in first_occurrence:
            first_occurrence[char] = i

    # Count[char][i]: number of occurrences of char in BWT[0...i-1]
    count = {char: [0] * (n + 1) for char in alphabet}
    for i, char in enumerate(bwt):
        for c in alphabet:
            count[c][i + 1] = count[c][i]
        if char in count:
            count[char][i + 1] += 1
            
    return first_occurrence, count

def count_occurrences(pattern: str, bwt_len: int, first_occ: dict, count: dict) -> int:
    top = 0
    bottom = bwt_len - 1
    pattern_chars = list(pattern)
    
    while top <= bottom and pattern_chars:
        symbol = pattern_chars.pop()
        if symbol in count and (count[symbol][bottom + 1] - count[symbol][top]) > 0:
            top = first_occ[symbol] + count[symbol][top]
            bottom = first_occ[symbol] + count[symbol][bottom + 1] - 1
        else:
            return 0
            
    return bottom - top + 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    bwt = input_data[0]
    patterns = input_data[2:]
    
    first_occ, count = preprocess_bwt(bwt)
    bwt_len = len(bwt)
    
    results = [
        count_occurrences(p, bwt_len, first_occ, count) 
        for p in patterns
    ]
    print(*(results))

if __name__ == '__main__':
    main()