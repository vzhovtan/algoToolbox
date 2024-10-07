# Input: intergers d (distance between cities) and m (car can travle on one tank) plus sequense of integers stop1 < stop2 < stopN
# Output The monimum number of refills to go from one city to another, fueling at stop1, stop2, etc
def countHop(dist, miles, ns, stations):
  if dist == 0:
    return 0
  if miles == 0:
    return -1
  if dist <= miles:
    return 0

  num_refill, curr_refill, limit = 0, 0, miles

  while limit < dist:
    if curr_refill >= ns or stations[curr_refill] > limit:
      return -1

    while curr_refill < ns - 1 and stations[curr_refill + 1] <= limit:
      curr_refill += 1

    num_refill += 1
    limit = stations[curr_refill] + miles
    curr_refill += 1

  return num_refill

def main():
  dist = int(input())
  miles = int(input())
  ns = int(input())
  ls = map(int, input().split(" "))
  stations = list(ls)
  print(countHop(dist, miles, ns, stations))

if __name__ == "__main__":
  main()