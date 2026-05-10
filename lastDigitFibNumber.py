# Input: An integer n.
# Output: Last digit of N-th Fibonacchi number

def fib(n):
  f = [0] * 61
  f[0] = 0
  f[1] = 1
  for i in range(2, n + 1):
    f[i] = (f[i - 1] + f[i - 2]) % 10
  return f

def lastdigit(n):
  f = fib(60)
  return f[n % 60]

def main():
  n = int(input())
  print(lastdigit(n))

if __name__ == "__main__":
  main()