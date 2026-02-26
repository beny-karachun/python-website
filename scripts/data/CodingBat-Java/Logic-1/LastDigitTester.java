/**
 * Tester for LastDigit - CodingBat Java
 * 13 test cases
 */
public class LastDigitTester {

    public static void main(String[] args) {
        LastDigit obj = new LastDigit();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.lastDigit(23, 19, 13) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(23, 19, 13) expected true");
            failed++;
        }

        // Test 2
        if (obj.lastDigit(23, 19, 12) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(23, 19, 12) expected false");
            failed++;
        }

        // Test 3
        if (obj.lastDigit(23, 19, 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(23, 19, 3) expected true");
            failed++;
        }

        // Test 4
        if (obj.lastDigit(23, 19, 39) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(23, 19, 39) expected true");
            failed++;
        }

        // Test 5
        if (obj.lastDigit(1, 2, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(1, 2, 3) expected false");
            failed++;
        }

        // Test 6
        if (obj.lastDigit(1, 1, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(1, 1, 2) expected true");
            failed++;
        }

        // Test 7
        if (obj.lastDigit(1, 2, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(1, 2, 2) expected true");
            failed++;
        }

        // Test 8
        if (obj.lastDigit(14, 25, 43) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(14, 25, 43) expected false");
            failed++;
        }

        // Test 9
        if (obj.lastDigit(14, 25, 45) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(14, 25, 45) expected true");
            failed++;
        }

        // Test 10
        if (obj.lastDigit(248, 106, 1002) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(248, 106, 1002) expected false");
            failed++;
        }

        // Test 11
        if (obj.lastDigit(248, 106, 1008) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(248, 106, 1008) expected true");
            failed++;
        }

        // Test 12
        if (obj.lastDigit(10, 11, 20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(10, 11, 20) expected true");
            failed++;
        }

        // Test 13
        if (obj.lastDigit(0, 11, 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(0, 11, 0) expected true");
            failed++;
        }

        System.out.println("lastDigit: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}