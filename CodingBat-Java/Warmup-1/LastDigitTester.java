/**
 * Tester for LastDigit - CodingBat Java
 * 7 test cases
 */
public class LastDigitTester {

    public static void main(String[] args) {
        LastDigit obj = new LastDigit();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.lastDigit(7, 17) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(7, 17) expected true");
            failed++;
        }

        // Test 2
        if (obj.lastDigit(6, 17) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(6, 17) expected false");
            failed++;
        }

        // Test 3
        if (obj.lastDigit(3, 113) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(3, 113) expected true");
            failed++;
        }

        // Test 4
        if (obj.lastDigit(114, 113) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(114, 113) expected false");
            failed++;
        }

        // Test 5
        if (obj.lastDigit(114, 4) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(114, 4) expected true");
            failed++;
        }

        // Test 6
        if (obj.lastDigit(10, 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(10, 0) expected true");
            failed++;
        }

        // Test 7
        if (obj.lastDigit(11, 0) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lastDigit(11, 0) expected false");
            failed++;
        }

        System.out.println("lastDigit: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}