"""
Tester for strCount - CodingBat Python
14 test cases
"""

from str_count import str_count


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = str_count(\"catcowcat\", \"cat\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: str_count(\"catcowcat\", \"cat\") expected 2, got {result}")
        failed += 1

    # Test 2
    result = str_count(\"catcowcat\", \"cow\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_count(\"catcowcat\", \"cow\") expected 1, got {result}")
        failed += 1

    # Test 3
    result = str_count(\"catcowcat\", \"dog\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: str_count(\"catcowcat\", \"dog\") expected 0, got {result}")
        failed += 1

    # Test 4
    result = str_count(\"cacatcowcat\", \"cat\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: str_count(\"cacatcowcat\", \"cat\") expected 2, got {result}")
        failed += 1

    # Test 5
    result = str_count(\"xyx\", \"x\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: str_count(\"xyx\", \"x\") expected 2, got {result}")
        failed += 1

    # Test 6
    result = str_count(\"iiiijj\", \"i\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: str_count(\"iiiijj\", \"i\") expected 4, got {result}")
        failed += 1

    # Test 7
    result = str_count(\"iiiijj\", \"ii\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: str_count(\"iiiijj\", \"ii\") expected 2, got {result}")
        failed += 1

    # Test 8
    result = str_count(\"iiiijj\", \"iii\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_count(\"iiiijj\", \"iii\") expected 1, got {result}")
        failed += 1

    # Test 9
    result = str_count(\"iiiijj\", \"j\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: str_count(\"iiiijj\", \"j\") expected 2, got {result}")
        failed += 1

    # Test 10
    result = str_count(\"iiiijj\", \"jj\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_count(\"iiiijj\", \"jj\") expected 1, got {result}")
        failed += 1

    # Test 11
    result = str_count(\"aaabababab\", \"ab\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: str_count(\"aaabababab\", \"ab\") expected 4, got {result}")
        failed += 1

    # Test 12
    result = str_count(\"aaabababab\", \"aa\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_count(\"aaabababab\", \"aa\") expected 1, got {result}")
        failed += 1

    # Test 13
    result = str_count(\"aaabababab\", \"a\")
    if result == 6:
        passed += 1
    else:
        print(f"FAIL: str_count(\"aaabababab\", \"a\") expected 6, got {result}")
        failed += 1

    # Test 14
    result = str_count(\"aaabababab\", \"b\")
    if result == 4:
        passed += 1
    else:
        print(f"FAIL: str_count(\"aaabababab\", \"b\") expected 4, got {result}")
        failed += 1

    print(f"str_count: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
