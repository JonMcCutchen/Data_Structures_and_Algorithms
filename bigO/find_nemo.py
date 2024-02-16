nemo = ['nemo']


def find_nemo(array):
  for i in range(len(array)):
    if array[i] == 'nemo':
      print('Found NEMO!')
      break


find_nemo(nemo)