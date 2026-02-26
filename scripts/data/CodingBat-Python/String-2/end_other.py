"""
CodingBat > Python > String-2 > endOther

Given two strings, return true if either of the strings appears at the very
end of the other string, ignoring upper/lower case differences (in other
words, the computation should not be "case sensitive"). Note:
str.toLowerCase() returns the lowercase version of a string.

Examples:
  endOther("Hiabc", "abc") → True
  endOther("AbC", "HiaBc") → True
  endOther("abc", "abXabc") → True
  endOther("Hiabc", "abcd") → False
  endOther("Hiabc", "bc") → True
  endOther("Hiabcx", "bc") → False
  endOther("abc", "abc") → True
  endOther("xyz", "12xyz") → True
  endOther("yz", "12xz") → False
  endOther("Z", "12xz") → True
  endOther("12", "12") → True
  endOther("abcXYZ", "abcDEF") → False
  endOther("ab", "ab12") → False
  endOther("ab", "12ab") → True
"""


def end_other(str, str2):
    # TODO: implement
    return False
