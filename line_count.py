
def line_count():
  """
  Reference the "Reading Files in Python" lesson to open the `file.txt` file, count the number of words in the file, and return the count.
  """
  file = open('file.txt', 'r')
  count = 0
  for line in file.readlines():
    count+=1
  file.close()
  return count
  
