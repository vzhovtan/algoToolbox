# Input: Integer n and m.
# Output: N-th Fibonacchi number modulo m
# aka Pisano period

def hugefibnumber(n, m):
  if n <= 1:
    return n

  arr = [0, 1]
  previousMod = 0
  currentMod = 1

  for i in range(n - 1):
    tempMod = previousMod
    previousMod = currentMod % m
    currentMod = (tempMod + currentMod) % m
    arr.append(currentMod)
    if currentMod == 1 and previousMod == 0:
      index = (n % (i + 1))
      return arr[index]
  return currentMod

def main():
  n, m  = map(int, input().split(" "))
  print(hugefibnumber(n, m))

if __name__ == "__main__":
  main()