"""
CodingBat > Python > String-2 > xyBalance

We'll say that a String is xy-balanced if for all the 'x' chars in the string,
there exists a 'y' char somewhere later in the string. So "xxy" is balanced,
but "xyx" is not. One 'y' can balance multiple 'x's. Return true if the given
string is xy-balanced.

Examples:
  xyBalance("aaxbby") → True
  xyBalance("aaxbb") → False
  xyBalance("yaaxbb") → False
  xyBalance("yaaxbby") → True
  xyBalance("xaxxbby") → True
  xyBalance("xaxxbbyx") → False
  xyBalance("xxbxy") → True
  xyBalance("xxbx") → False
  xyBalance("bbb") → True
  xyBalance("bxbb") → False
  xyBalance("bxyb") → True
  xyBalance("xy") → True
  xyBalance("y") → True
  xyBalance("x") → False
  xyBalance("") → True
  xyBalance("yxyxyxyx") → False
  xyBalance("yxyxyxyxy") → True
  xyBalance("12xabxxydxyxyzz") → True
"""


def xy_balance(str):
    # TODO: implement
    return False
