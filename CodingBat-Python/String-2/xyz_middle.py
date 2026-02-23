"""
CodingBat > Python > String-2 > xyzMiddle

Given a string, does "xyz" appear in the middle of the string? To define
middle, we'll say that the number of chars to the left and right of the "xyz"
must differ by at most one. This problem is harder than it looks.

Examples:
  xyzMiddle("AAxyzBB") → True
  xyzMiddle("AxyzBB") → True
  xyzMiddle("AxyzBBB") → False
  xyzMiddle("AxyzBBBB") → False
  xyzMiddle("AAAxyzB") → False
  xyzMiddle("AAAxyzBB") → True
  xyzMiddle("AAAAxyzBB") → False
  xyzMiddle("AAAAAxyzBBB") → False
  xyzMiddle("1x345xyz12x4") → True
  xyzMiddle("xyzAxyzBBB") → True
  xyzMiddle("xyzAxyzBxyz") → True
  xyzMiddle("xyzxyzAxyzBxyzxyz") → True
  xyzMiddle("xyzxyzxyzBxyzxyz") → True
  xyzMiddle("xyzxyzAxyzxyzxyz") → True
  xyzMiddle("xyzxyzAxyzxyzxy") → False
  xyzMiddle("AxyzxyzBB") → False
  xyzMiddle("") → False
  xyzMiddle("x") → False
  xyzMiddle("xy") → False
  xyzMiddle("xyz") → True
  xyzMiddle("xyzz") → True
"""


def xyz_middle(str):
    # TODO: implement
    return False
