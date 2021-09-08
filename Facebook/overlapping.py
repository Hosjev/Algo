class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(v):
  if v == None or len(v) == 0 :
    return None

  result = []
  result.append(Pair(v[0].first, v[0].second))

  for i in range(1, len(v)):
    x1 = v[i].first
    y1 = v[i].second
    y2 = result[len(result) - 1].second

    if y2 >= x1:
      result[len(result) - 1].second = max(y1, y2)
    else:
      result.append(Pair(x1, y1))

  return result;

v = [Pair(1, 5), Pair(3, 1), Pair(4, 6), 
     Pair(6, 8), Pair(10, 12), Pair(11, 15)]

result = merge_intervals(v)

for i in range(len(result)):
  print("[" + str(result[i].first) + ", " + str(result[i].second) + "]", end =" ")


# R 1, 8
# for i in 1-6
#   x1 = 3 4 6 10
#   y1 = 1 6 8 12
#   y2 = R[1-1].s = 5 5 6 8
#   
#   if my last second number is larger or equal to current starting number
#   take max of second/end time, else, my ranges don't overlap
#   this only works if the pairs are in order of v[0] to end
#   if y2 >= x1:
#       res[lR-1].s = max(y1, y2)
#   else:
#       res.app(P(x1, y1))
