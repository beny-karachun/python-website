"""
Tester for stringSplosion - CodingBat Python
10 test cases
"""

from string_splosion import string_splosion


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = string_splosion(\"Code\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"Code\") expected \, got {result}")
        failed += 1

    # Test 2
    result = string_splosion(\"abc\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"abc\") expected \, got {result}")
        failed += 1

    # Test 3
    result = string_splosion(\"ab\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"ab\") expected \, got {result}")
        failed += 1

    # Test 4
    result = string_splosion(\"x\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"x\") expected \, got {result}")
        failed += 1

    # Test 5
    result = string_splosion(\"fade\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"fade\") expected \, got {result}")
        failed += 1

    # Test 6
    result = string_splosion(\"There\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"There\") expected \, got {result}")
        failed += 1

    # Test 7
    result = string_splosion(\"Kitten\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"Kitten\") expected \, got {result}")
        failed += 1

    # Test 8
    result = string_splosion(\"Bye\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"Bye\") expected \, got {result}")
        failed += 1

    # Test 9
    result = string_splosion(\"Good\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"Good\") expected \, got {result}")
        failed += 1

    # Test 10
    result = string_splosion(\"Bad\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: string_splosion(\"Bad\") expected \, got {result}")
        failed += 1

    print(f"string_splosion: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
