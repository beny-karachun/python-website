"""
Tester for makeTags - CodingBat Python
7 test cases
"""

from make_tags import make_tags


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = make_tags(\"i\", \"Yay\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"i\", \"Yay\") expected \, got {result}")
        failed += 1

    # Test 2
    result = make_tags(\"i\", \"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"i\", \"Hello\") expected \, got {result}")
        failed += 1

    # Test 3
    result = make_tags(\"cite\", \"Yay\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"cite\", \"Yay\") expected \, got {result}")
        failed += 1

    # Test 4
    result = make_tags(\"address\", \"here\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"address\", \"here\") expected \, got {result}")
        failed += 1

    # Test 5
    result = make_tags(\"body\", \"Heart\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"body\", \"Heart\") expected \, got {result}")
        failed += 1

    # Test 6
    result = make_tags(\"i\", \"i\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"i\", \"i\") expected \, got {result}")
        failed += 1

    # Test 7
    result = make_tags(\"i\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: make_tags(\"i\", \"\") expected \, got {result}")
        failed += 1

    print(f"make_tags: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
