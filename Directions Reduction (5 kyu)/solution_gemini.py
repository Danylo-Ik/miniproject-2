def dir_reduc(arr):
  """
  Reduces a list of directions by removing opposing directions.

  Args:
      arr: A list of directions (North, South, East, West)

  Returns:
      A list containing only the remaining non-canceling directions.
  """
  stack = []
  for direction in arr:
    if stack and is_opposite(stack[-1], direction):
      stack.pop()
    else:
      stack.append(direction)
  return stack

def is_opposite(dir1, dir2):
  """
  Checks if two directions are opposing.

  Args:
      dir1: The first direction (North, South, East, West)
      dir2: The second direction (North, South, East, West)

  Returns:
      True if the directions are opposing, False otherwise.
  """
  return (dir1 == "NORTH" and dir2 == "SOUTH") or \
         (dir1 == "SOUTH" and dir2 == "NORTH") or \
         (dir1 == "EAST" and dir2 == "WEST") or \
         (dir1 == "WEST" and dir2 == "EAST")
