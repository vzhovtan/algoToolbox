# Input: An integer money
# Output: the minimum number of coins with denomination 1, 5 and 10 that changes money
def change(n):
  if n == 0:
    return 0
  coins = [1,5,10]
  count = 0
  while n > 0:
    if n >= max(coins):
      count +=1
      n -= max(coins)
    else:
      coins.remove(max(coins))

  return count

def main():
  money = int(input())
  print(change(money))

if __name__ == "__main__":
  main()