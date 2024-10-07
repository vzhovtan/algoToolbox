# Input: An integer n.
# Output: Last digit of sum of squares of Fib numbers
# num mod 60 gives 60 repeatations in Pisano Series
def pisanonummod60(n):
  previous, current = 0, 1
  n = n % 60
  if (n == 0):
    return 0
  elif (n == 1):
    return 1
  else:
    for _ in range(2, n + 1):
      previous, current = current, (previous + current) % 60
  return current

def main():
  n = int(input())
  summ = pisanonummod60(n) * pisanonummod60(n+1)
  print(summ % 10)

if __name__ == "__main__":
  main()