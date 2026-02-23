"""
Tester for strDist - CodingBat Python
14 test cases
"""

from str_dist import str_dist


def run_tests():
    passed = 0
    failed = 0

    # Test 1
    result = str_dist(\"catcowcat\", \"cat\")
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"catcowcat\", \"cat\") expected 9, got {result}")
        failed += 1

    # Test 2
    result = str_dist(\"catcowcat\", \"cow\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"catcowcat\", \"cow\") expected 3, got {result}")
        failed += 1

    # Test 3
    result = str_dist(\"cccatcowcatxx\", \"cat\")
    if result == 9:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"cccatcowcatxx\", \"cat\") expected 9, got {result}")
        failed += 1

    # Test 4
    result = str_dist(\"abccatcowcatcatxyz\", \"cat\")
    if result == 12:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"abccatcowcatcatxyz\", \"cat\") expected 12, got {result}")
        failed += 1

    # Test 5
    result = str_dist(\"xyx\", \"x\")
    if result == 3:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"xyx\", \"x\") expected 3, got {result}")
        failed += 1

    # Test 6
    result = str_dist(\"xyx\", \"y\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"xyx\", \"y\") expected 1, got {result}")
        failed += 1

    # Test 7
    result = str_dist(\"xyx\", \"z\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"xyx\", \"z\") expected 0, got {result}")
        failed += 1

    # Test 8
    result = str_dist(\"z\", \"z\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"z\", \"z\") expected 1, got {result}")
        failed += 1

    # Test 9
    result = str_dist(\"x\", \"z\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"x\", \"z\") expected 0, got {result}")
        failed += 1

    # Test 10
    result = str_dist(\"\", \"z\")
    if result == 0:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"\", \"z\") expected 0, got {result}")
        failed += 1

    # Test 11
    result = str_dist(\"hiHellohihihi\", \"hi\")
    if result == 13:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"hiHellohihihi\", \"hi\") expected 13, got {result}")
        failed += 1

    # Test 12
    result = str_dist(\"hiHellohihihi\", \"hih\")
    if result == 5:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"hiHellohihihi\", \"hih\") expected 5, got {result}")
        failed += 1

    # Test 13
    result = str_dist(\"hiHellohihihi\", \"o\")
    if result == 1:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"hiHellohihihi\", \"o\") expected 1, got {result}")
        failed += 1

    # Test 14
    result = str_dist(\"hiHellohihihi\", \"ll\")
    if result == 2:
        passed += 1
    else:
        print(f"FAIL: str_dist(\"hiHellohihihi\", \"ll\") expected 2, got {result}")
        failed += 1

    print(f"str_dist: {passed}/{passed + failed} tests passed.")
    if failed == 0:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()
