"""
Tester for mixStart - CodingBat Python
7 test cases
"""

from mix_start import mix_start


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = mix_start(\"mix snacks\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"mix snacks\") expected True, got {result}")
        failed += 1

    # Test 2
    result = mix_start(\"pix snacks\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"pix snacks\") expected True, got {result}")
        failed += 1

    # Test 3
    result = mix_start(\"piz snacks\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"piz snacks\") expected False, got {result}")
        failed += 1

    # Test 4
    result = mix_start(\"nix\")
    if result == True:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"nix\") expected True, got {result}")
        failed += 1

    # Test 5
    result = mix_start(\"ni\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"ni\") expected False, got {result}")
        failed += 1

    # Test 6
    result = mix_start(\"n\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"n\") expected False, got {result}")
        failed += 1

    # Test 7
    result = mix_start(\"\")
    if result == False:
        passed += 1
    else:
        print(f"FAIL: mix_start(\"\") expected False, got {result}")
        failed += 1

    print(f"mix_start: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
