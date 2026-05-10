#Input: A sequence of n non-negative integers.
#Output: The maximum value and second maximum value

def twomax(arrint):
  max = 0
  secmax = 0
  for i in range(len(arrint)):
    if arrint[i] > max:
      max = arrint[i]
  arrint.remove(max)
  for i in range(len(arrint)):
    if arrint[i] > secmax:
      secmax = arrint[i]
  return max, secmax

def main():
  arr = map(int, input().split(" "))
  print(twomax(list(arr)))

if __name__ == "__main__":
  main()