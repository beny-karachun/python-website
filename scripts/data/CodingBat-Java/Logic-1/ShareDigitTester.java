/**
 * Tester for ShareDigit - CodingBat Java
 * 10 test cases
 */
public class ShareDigitTester {

    public static void main(String[] args) {
        ShareDigit obj = new ShareDigit();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.shareDigit(12, 23) == true) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(12, 23) expected true");
            failed++;
        }

        // Test 2
        if (obj.shareDigit(12, 43) == false) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(12, 43) expected false");
            failed++;
        }

        // Test 3
        if (obj.shareDigit(12, 44) == false) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(12, 44) expected false");
            failed++;
        }

        // Test 4
        if (obj.shareDigit(23, 12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(23, 12) expected true");
            failed++;
        }

        // Test 5
        if (obj.shareDigit(23, 39) == true) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(23, 39) expected true");
            failed++;
        }

        // Test 6
        if (obj.shareDigit(23, 19) == false) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(23, 19) expected false");
            failed++;
        }

        // Test 7
        if (obj.shareDigit(30, 90) == true) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(30, 90) expected true");
            failed++;
        }

        // Test 8
        if (obj.shareDigit(30, 91) == false) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(30, 91) expected false");
            failed++;
        }

        // Test 9
        if (obj.shareDigit(55, 55) == true) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(55, 55) expected true");
            failed++;
        }

        // Test 10
        if (obj.shareDigit(55, 44) == false) {
            passed++;
        } else {
            System.out.println("FAIL: shareDigit(55, 44) expected false");
            failed++;
        }

        System.out.println("shareDigit: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}