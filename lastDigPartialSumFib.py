# Input: An integer m and n, m < n
# Output: the last digit of sum Fm + ... + Fn
def lastdigpartsum(n, m):
  a = [0, 1]
  for i in range(2, 60):
    a.append(a[i - 1] + a[i - 2])
  summ = 0
  n, m = n % 60, m % 60
  if m < n:
    m += 60
  for i in range(n, m + 1):
    summ += a[i % 60]
  return summ % 10

def main():
  n, m = map(int, input().split(" "))
  print(lastdigpartsum(n, m))

if __name__ == "__main__":
  main()