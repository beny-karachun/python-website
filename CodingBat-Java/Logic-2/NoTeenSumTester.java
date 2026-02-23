/**
 * Tester for NoTeenSum - CodingBat Java
 * 16 test cases
 */
public class NoTeenSumTester {

    public static void main(String[] args) {
        NoTeenSum obj = new NoTeenSum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.noTeenSum(1, 2, 3) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(1, 2, 3) expected 6");
            failed++;
        }

        // Test 2
        if (obj.noTeenSum(2, 13, 1) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(2, 13, 1) expected 3");
            failed++;
        }

        // Test 3
        if (obj.noTeenSum(2, 1, 14) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(2, 1, 14) expected 3");
            failed++;
        }

        // Test 4
        if (obj.noTeenSum(2, 1, 15) == 18) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(2, 1, 15) expected 18");
            failed++;
        }

        // Test 5
        if (obj.noTeenSum(2, 1, 16) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(2, 1, 16) expected 19");
            failed++;
        }

        // Test 6
        if (obj.noTeenSum(2, 1, 17) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(2, 1, 17) expected 3");
            failed++;
        }

        // Test 7
        if (obj.noTeenSum(17, 1, 2) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(17, 1, 2) expected 3");
            failed++;
        }

        // Test 8
        if (obj.noTeenSum(2, 15, 2) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(2, 15, 2) expected 19");
            failed++;
        }

        // Test 9
        if (obj.noTeenSum(16, 17, 18) == 16) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(16, 17, 18) expected 16");
            failed++;
        }

        // Test 10
        if (obj.noTeenSum(17, 18, 19) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(17, 18, 19) expected 0");
            failed++;
        }

        // Test 11
        if (obj.noTeenSum(15, 16, 1) == 32) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(15, 16, 1) expected 32");
            failed++;
        }

        // Test 12
        if (obj.noTeenSum(15, 15, 19) == 30) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(15, 15, 19) expected 30");
            failed++;
        }

        // Test 13
        if (obj.noTeenSum(15, 19, 16) == 31) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(15, 19, 16) expected 31");
            failed++;
        }

        // Test 14
        if (obj.noTeenSum(5, 17, 18) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(5, 17, 18) expected 5");
            failed++;
        }

        // Test 15
        if (obj.noTeenSum(17, 18, 16) == 16) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(17, 18, 16) expected 16");
            failed++;
        }

        // Test 16
        if (obj.noTeenSum(17, 19, 18) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: noTeenSum(17, 19, 18) expected 0");
            failed++;
        }

        System.out.println("noTeenSum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}