#!/usr/bin/env python3
from typing import Any, Optional, Sequence

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
  """
  This function safely returns the first element of a list,
  returning None if the list is empty.

  Args:
    lst: A sequence of elements of any type.

  Returns:
    The first element of the list, or None if the list is empty.
  """
  if lst:
    return lst[0]
  else:
    return None
