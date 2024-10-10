#!/usr/bin/env python3

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
  """
  This function takes a tuple and a factor as input and returns a new list
  where each element of the tuple is repeated 'factor' times.

  Args:
    lst: The input tuple.
    factor: The number of times to repeat each element.

  Returns:
    A new list with the zoomed-in elements.
  """
  zoomed_in: List = [
    item for item in lst
    for i in range(factor)
  ]
  return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
