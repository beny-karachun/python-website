/**
 * Tester for RoundSum - CodingBat Java
 * 19 test cases
 */
public class RoundSumTester {

    public static void main(String[] args) {
        RoundSum obj = new RoundSum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.roundSum(16, 17, 18) == 60) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(16, 17, 18) expected 60");
            failed++;
        }

        // Test 2
        if (obj.roundSum(12, 13, 14) == 30) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(12, 13, 14) expected 30");
            failed++;
        }

        // Test 3
        if (obj.roundSum(6, 4, 4) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(6, 4, 4) expected 10");
            failed++;
        }

        // Test 4
        if (obj.roundSum(4, 6, 5) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(4, 6, 5) expected 20");
            failed++;
        }

        // Test 5
        if (obj.roundSum(4, 4, 6) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(4, 4, 6) expected 10");
            failed++;
        }

        // Test 6
        if (obj.roundSum(9, 4, 4) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(9, 4, 4) expected 10");
            failed++;
        }

        // Test 7
        if (obj.roundSum(0, 0, 1) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(0, 0, 1) expected 0");
            failed++;
        }

        // Test 8
        if (obj.roundSum(0, 9, 0) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(0, 9, 0) expected 10");
            failed++;
        }

        // Test 9
        if (obj.roundSum(10, 10, 19) == 40) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(10, 10, 19) expected 40");
            failed++;
        }

        // Test 10
        if (obj.roundSum(20, 30, 40) == 90) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(20, 30, 40) expected 90");
            failed++;
        }

        // Test 11
        if (obj.roundSum(45, 21, 30) == 100) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(45, 21, 30) expected 100");
            failed++;
        }

        // Test 12
        if (obj.roundSum(23, 11, 26) == 60) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(23, 11, 26) expected 60");
            failed++;
        }

        // Test 13
        if (obj.roundSum(23, 24, 25) == 70) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(23, 24, 25) expected 70");
            failed++;
        }

        // Test 14
        if (obj.roundSum(25, 24, 25) == 80) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(25, 24, 25) expected 80");
            failed++;
        }

        // Test 15
        if (obj.roundSum(23, 24, 29) == 70) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(23, 24, 29) expected 70");
            failed++;
        }

        // Test 16
        if (obj.roundSum(11, 24, 36) == 70) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(11, 24, 36) expected 70");
            failed++;
        }

        // Test 17
        if (obj.roundSum(24, 36, 32) == 90) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(24, 36, 32) expected 90");
            failed++;
        }

        // Test 18
        if (obj.roundSum(14, 12, 26) == 50) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(14, 12, 26) expected 50");
            failed++;
        }

        // Test 19
        if (obj.roundSum(12, 10, 24) == 40) {
            passed++;
        } else {
            System.out.println("FAIL: roundSum(12, 10, 24) expected 40");
            failed++;
        }

        System.out.println("roundSum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}