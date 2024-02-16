def print_numbers_then_pairs(numbers):
  print("these are the numbers:")
  for number in numbers:
    print(number)
  print("and these are their sums:");
  for firstNumber in numbers:
    for secondNumber in numbers:
      print(firstNumber + secondNumber)

print_numbers_then_pairs([1, 2, 3, 4, 5])

# O(n + n^2) or O(n^2)