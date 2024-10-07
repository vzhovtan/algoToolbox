# Input: first line is n which is number of compounds and w which is capacity
# next lines contains cost and weight of the compound
# Output: max values of compounds which fits into the capacity
def costforunit(c, w):
  if w == 0:
    return 0
  else:
    return c/w

def maxvalue(capacity, cost, weight):
  totalmax = 0
  if capacity == 0:
    return f'{totalmax:.4f}'
  if len(cost) == 0:
    return f'{totalmax:.4f}'
  if len(weight) == 1 and weight[0] < capacity:
    return f'{cost[0] * weight[0]:.4f}'
  while capacity > 0:
    currcost = max(cost)
    currind = cost.index(currcost)
    if weight[currind] >= capacity:
      totalmax += capacity * currcost
      break
    else:
      totalmax += weight[currind] * currcost
      capacity -= weight[currind]
      weight.pop(currind)
      cost.pop(currind)
  return f'{totalmax:.4f}'

def main():
  num, capacity = map(int, input().split(" "))
  i, cost, weight = 0, [], []
  while i < num:
    c, w = map(int, input().split(" "))
    weight.append(w)
    cost.append(costforunit(c, w))
    i += 1
  print(maxvalue(capacity, cost, weight))

if __name__ == "__main__":
  main()