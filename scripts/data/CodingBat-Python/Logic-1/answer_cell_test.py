"""
Tester for answerCell - CodingBat Python
6 test cases
"""

from answer_cell import answer_cell


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = answer_cell(False, False, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: answer_cell(False, False, False) expected True, got {result}")
        failed += 1

    # Test 2
    result = answer_cell(False, False, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: answer_cell(False, False, True) expected False, got {result}")
        failed += 1

    # Test 3
    result = answer_cell(True, False, False)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: answer_cell(True, False, False) expected False, got {result}")
        failed += 1

    # Test 4
    result = answer_cell(True, True, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: answer_cell(True, True, False) expected True, got {result}")
        failed += 1

    # Test 5
    result = answer_cell(False, True, False)
    if result == True:
        passed += 1
    else:
        print(f"FAIL: answer_cell(False, True, False) expected True, got {result}")
        failed += 1

    # Test 6
    result = answer_cell(True, True, True)
    if result == False:
        passed += 1
    else:
        print(f"FAIL: answer_cell(True, True, True) expected False, got {result}")
        failed += 1

    print(f"answer_cell: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
