"""
Tester for countYZ - CodingBat Python
11 test cases
"""

from count_yz import count_yz


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = count_yz(\"fez day\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"fez day\") expected 2, got {result}")
        failed += 1

    # Test 2
    result = count_yz(\"day fez\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"day fez\") expected 2, got {result}")
        failed += 1

    # Test 3
    result = count_yz(\"day fyyyz\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"day fyyyz\") expected 2, got {result}")
        failed += 1

    # Test 4
    result = count_yz(\"day yak\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"day yak\") expected 1, got {result}")
        failed += 1

    # Test 5
    result = count_yz(\"day:yak\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"day:yak\") expected 1, got {result}")
        failed += 1

    # Test 6
    result = count_yz(\"!!day--yaz!!\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"!!day--yaz!!\") expected 2, got {result}")
        failed += 1

    # Test 7
    result = count_yz(\"yak zak\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"yak zak\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = count_yz(\"DAY abc XYZ\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"DAY abc XYZ\") expected 2, got {result}")
        failed += 1

    # Test 9
    result = count_yz(\"aaz yyz my\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"aaz yyz my\") expected 3, got {result}")
        failed += 1

    # Test 10
    result = count_yz(\"y2bz\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"y2bz\") expected 2, got {result}")
        failed += 1

    # Test 11
    result = count_yz(\"zxyx\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: count_yz(\"zxyx\") expected 0, got {result}")
        failed += 1

    print(f"count_yz: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
