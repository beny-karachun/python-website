"""
Tester for zipZap - CodingBat Python
12 test cases
"""

from zip_zap import zip_zap


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = zip_zap(\"zipXzap\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zipXzap\") expected \, got {result}")
        failed += 1

    # Test 2
    result = zip_zap(\"zopzop\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zopzop\") expected \, got {result}")
        failed += 1

    # Test 3
    result = zip_zap(\"zzzopzop\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zzzopzop\") expected \, got {result}")
        failed += 1

    # Test 4
    result = zip_zap(\"zibzap\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zibzap\") expected \, got {result}")
        failed += 1

    # Test 5
    result = zip_zap(\"zip\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zip\") expected \, got {result}")
        failed += 1

    # Test 6
    result = zip_zap(\"zi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zi\") expected \, got {result}")
        failed += 1

    # Test 7
    result = zip_zap(\"z\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"z\") expected \, got {result}")
        failed += 1

    # Test 8
    result = zip_zap(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"\") expected \, got {result}")
        failed += 1

    # Test 9
    result = zip_zap(\"zzp\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"zzp\") expected \, got {result}")
        failed += 1

    # Test 10
    result = zip_zap(\"abcppp\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"abcppp\") expected \, got {result}")
        failed += 1

    # Test 11
    result = zip_zap(\"azbcppp\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"azbcppp\") expected \, got {result}")
        failed += 1

    # Test 12
    result = zip_zap(\"azbcpzpp\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: zip_zap(\"azbcpzpp\") expected \, got {result}")
        failed += 1

    print(f"zip_zap: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
