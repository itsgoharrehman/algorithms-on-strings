# python3
import sys


def solve(text1, text2):
  len1 = len(text1)
  len2 = len(text2)

  for length in range(1, len1 + 1):
    text2_substrings = {
        text2[i : i + length] for i in range(len2 - length + 1)
    }

    for i in range(len1 - length + 1):
      sub = text1[i : i + length]
      if sub not in text2_substrings:
        return sub

  return ""


if __name__ == "__main__":
  input_data = sys.stdin.read().split()
  if len(input_data) >= 2:
    text1 = input_data[0]
    text2 = input_data[1]
    print(solve(text1, text2))