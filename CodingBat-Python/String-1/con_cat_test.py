"""
Tester for conCat - CodingBat Python
6 test cases
"""

from con_cat import con_cat


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = con_cat(\"abc\", \"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: con_cat(\"abc\", \"cat\") expected \, got {result}")
        failed += 1

    # Test 2
    result = con_cat(\"dog\", \"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: con_cat(\"dog\", \"cat\") expected \, got {result}")
        failed += 1

    # Test 3
    result = con_cat(\"abc\", \"\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: con_cat(\"abc\", \"\") expected \, got {result}")
        failed += 1

    # Test 4
    result = con_cat(\"\", \"cat\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: con_cat(\"\", \"cat\") expected \, got {result}")
        failed += 1

    # Test 5
    result = con_cat(\"pig\", \"g\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: con_cat(\"pig\", \"g\") expected \, got {result}")
        failed += 1

    # Test 6
    result = con_cat(\"pig\", \"doggy\")
    if result == \:
        passed += 1
    else:
        print(f"FAIL: con_cat(\"pig\", \"doggy\") expected \, got {result}")
        failed += 1

    print(f"con_cat: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
