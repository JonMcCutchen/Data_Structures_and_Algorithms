boxes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def log_all_pairs(array):
  counter = 0
  for i in range(len(array)):
    for j in range(len(array)):
      print(array[i], array[j])
      counter += 1
  
  print('number of pairs: ' + str(counter))
      

log_all_pairs(boxes)

# O(n * n) or O(n^2)