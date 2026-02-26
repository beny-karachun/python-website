"""
Tester for endX - CodingBat Python
12 test cases
"""

from end_x import end_x


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = end_x(\"xxre\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"xxre\") expected \, got {result}")
        failed += 1

    # Test 2
    result = end_x(\"xxhixx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"xxhixx\") expected \, got {result}")
        failed += 1

    # Test 3
    result = end_x(\"xhixhix\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"xhixhix\") expected \, got {result}")
        failed += 1

    # Test 4
    result = end_x(\"hiy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"hiy\") expected \, got {result}")
        failed += 1

    # Test 5
    result = end_x(\"h\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"h\") expected \, got {result}")
        failed += 1

    # Test 6
    result = end_x(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"x\") expected \, got {result}")
        failed += 1

    # Test 7
    result = end_x(\"xx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"xx\") expected \, got {result}")
        failed += 1

    # Test 8
    result = end_x(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = end_x(\"bxx\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"bxx\") expected \, got {result}")
        failed += 1

    # Test 10
    result = end_x(\"bxax\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"bxax\") expected \, got {result}")
        failed += 1

    # Test 11
    result = end_x(\"axaxax\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"axaxax\") expected \, got {result}")
        failed += 1

    # Test 12
    result = end_x(\"xxhxi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: end_x(\"xxhxi\") expected \, got {result}")
        failed += 1

    print(f"end_x: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
