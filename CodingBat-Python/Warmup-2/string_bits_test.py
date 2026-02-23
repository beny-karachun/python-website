"""
Tester for stringBits - CodingBat Python
10 test cases
"""

from string_bits import string_bits


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_bits(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"Hello\") expected \, got {result}")
        failed += 1

    # Test 2
    result = string_bits(\"Hi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"Hi\") expected \, got {result}")
        failed += 1

    # Test 3
    result = string_bits(\"Heeololeo\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"Heeololeo\") expected \, got {result}")
        failed += 1

    # Test 4
    result = string_bits(\"HiHiHi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"HiHiHi\") expected \, got {result}")
        failed += 1

    # Test 5
    result = string_bits(\"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"\") expected \, got {result}")
        failed += 1

    # Test 6
    result = string_bits(\"Greetings\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"Greetings\") expected \, got {result}")
        failed += 1

    # Test 7
    result = string_bits(\"Chocoate\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"Chocoate\") expected \, got {result}")
        failed += 1

    # Test 8
    result = string_bits(\"pi\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"pi\") expected \, got {result}")
        failed += 1

    # Test 9
    result = string_bits(\"Hello Kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"Hello Kitten\") expected \, got {result}")
        failed += 1

    # Test 10
    result = string_bits(\"hxaxpxpxy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_bits(\"hxaxpxpxy\") expected \, got {result}")
        failed += 1

    print(f"string_bits: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
