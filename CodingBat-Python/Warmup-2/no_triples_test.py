"""
Tester for noTriples - CodingBat Python
3 test cases
"""

from no_triples import no_triples


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = no_triples([1, 1, 2, 2, 1])
    if result == True:
        passed += 1
    else:
        print(f"FAIL: no_triples([1, 1, 2, 2, 1]) expected True, got {result}")
        failed += 1

    # Test 2
    result = no_triples([1, 1, 2, 2, 2, 1])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: no_triples([1, 1, 2, 2, 2, 1]) expected False, got {result}")
        failed += 1

    # Test 3
    result = no_triples([1, 1, 1, 2, 2, 2, 1])
    if result == False:
        passed += 1
    else:
        print(f"FAIL: no_triples([1, 1, 1, 2, 2, 2, 1]) expected False, got {result}")
        failed += 1

    print(f"no_triples: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
