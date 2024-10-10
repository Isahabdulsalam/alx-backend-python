#!/usr/bin/env python3

from typing import Any, Mapping, Optional, Union

def safely_get_value(dct: Mapping, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
  """
  Safely retrieves the value from a dictionary for a given key.
  Returns the default value if the key is not found.

  Args:
    dct: The dictionary from which to retrieve the value.
    key: The key whose corresponding value is to be retrieved.
    default: The value to return if the key is not found.

  Returns:
    The value associated with the key if found, otherwise the default value.
  """
  if key in dct:
    return dct[key]
  else:
    return default
