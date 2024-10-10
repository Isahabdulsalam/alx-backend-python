#!/usr/bin/env python3

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
  """
  This function takes a list of strings and returns a list of tuples, 
  where each tuple contains a string and its length.

  Args:
    lst: A list of strings.

  Returns:
    A list of tuples, where each tuple contains a string and its length.
  """
  return [(i, len(i)) for i in lst]
