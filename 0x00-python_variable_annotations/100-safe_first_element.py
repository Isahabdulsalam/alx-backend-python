#!/usr/bin/env python3
from typing import Any, Optional, Sequence
"""Duck typing - first element of a sequence"""


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
  """Augment the following code with the correct duck-typed annotations:"""
  if lst:
    return lst[0]
  else:
    return None
