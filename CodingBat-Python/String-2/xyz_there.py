"""
CodingBat > Python > String-2 > xyzThere

Return true if the given string contains an appearance of "xyz" where the xyz
is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does
not.

Examples:
  xyzThere("abcxyz") → True
  xyzThere("abc.xyz") → False
  xyzThere("xyz.abc") → True
  xyzThere("abcxy") → False
  xyzThere("xyz") → True
  xyzThere("xy") → False
  xyzThere("x") → False
  xyzThere("") → False
  xyzThere("abc.xyzxyz") → True
  xyzThere("abc.xxyz") → True
  xyzThere(".xyz") → False
  xyzThere("12.xyz") → False
  xyzThere("12xyz") → True
  xyzThere("1.xyz.xyz2.xyz") → False
"""


def xyz_there(str):
    # TODO: implement
    return False
