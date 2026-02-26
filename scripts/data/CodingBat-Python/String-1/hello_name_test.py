"""
Tester for helloName - CodingBat Python
10 test cases
"""

from hello_name import hello_name


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = hello_name(\"Bob\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Bob\") expected \, got {result}")
        failed += 1

    # Test 2
    result = hello_name(\"Alice\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Alice\") expected \, got {result}")
        failed += 1

    # Test 3
    result = hello_name(\"X\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"X\") expected \, got {result}")
        failed += 1

    # Test 4
    result = hello_name(\"Dolly\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Dolly\") expected \, got {result}")
        failed += 1

    # Test 5
    result = hello_name(\"Alpha\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Alpha\") expected \, got {result}")
        failed += 1

    # Test 6
    result = hello_name(\"Omega\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Omega\") expected \, got {result}")
        failed += 1

    # Test 7
    result = hello_name(\"Goodbye\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Goodbye\") expected \, got {result}")
        failed += 1

    # Test 8
    result = hello_name(\"ho ho ho\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"ho ho ho\") expected \, got {result}")
        failed += 1

    # Test 9
    result = hello_name(\"xyz!\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"xyz!\") expected \, got {result}")
        failed += 1

    # Test 10
    result = hello_name(\"Hello\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: hello_name(\"Hello\") expected \, got {result}")
        failed += 1

    print(f"hello_name: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
