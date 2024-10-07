# Input: Two single digit numbers.
# Output: The sum of these numbers.

def twosum(n, m):
  summ = n + m
  return summ

def main():
  n, m = map(int, input().split())
  print(twosum(n, m))

if __name__ == "__main__":
  main()
