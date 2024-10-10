#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
  """
  This function takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

  Args:
    multiplier: The multiplier to use.

  Returns:
    A function that multiplies a float by multiplier.
  """
  def multiply(number: float) -> float:
    return multiplier * number
  return multiply
