#Input: An integer n and a sequence of n non-negative integers.
#Output: The maximum value that can be obtained by multiplying two different
# elements from the sequence.
def maxpairwise(arrint):
  arrint.sort()
  maxpw = arrint[-1] * arrint[-2]
  return maxpw

def main():
  n = int(input())
  arr = map(int, input().split(" "))
  print(maxpairwise(list(arr)))

if __name__ == "__main__":
  main()