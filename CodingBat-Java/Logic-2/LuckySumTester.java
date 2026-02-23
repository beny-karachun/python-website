/**
 * Tester for LuckySum - CodingBat Java
 * 12 test cases
 */
public class LuckySumTester {

    public static void main(String[] args) {
        LuckySum obj = new LuckySum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.luckySum(1, 2, 3) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(1, 2, 3) expected 6");
            failed++;
        }

        // Test 2
        if (obj.luckySum(1, 2, 13) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(1, 2, 13) expected 3");
            failed++;
        }

        // Test 3
        if (obj.luckySum(1, 13, 3) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(1, 13, 3) expected 1");
            failed++;
        }

        // Test 4
        if (obj.luckySum(1, 13, 13) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(1, 13, 13) expected 1");
            failed++;
        }

        // Test 5
        if (obj.luckySum(6, 5, 2) == 13) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(6, 5, 2) expected 13");
            failed++;
        }

        // Test 6
        if (obj.luckySum(13, 2, 3) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(13, 2, 3) expected 0");
            failed++;
        }

        // Test 7
        if (obj.luckySum(13, 2, 13) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(13, 2, 13) expected 0");
            failed++;
        }

        // Test 8
        if (obj.luckySum(13, 13, 2) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(13, 13, 2) expected 0");
            failed++;
        }

        // Test 9
        if (obj.luckySum(9, 4, 13) == 13) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(9, 4, 13) expected 13");
            failed++;
        }

        // Test 10
        if (obj.luckySum(8, 13, 2) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(8, 13, 2) expected 8");
            failed++;
        }

        // Test 11
        if (obj.luckySum(7, 2, 1) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(7, 2, 1) expected 10");
            failed++;
        }

        // Test 12
        if (obj.luckySum(3, 3, 13) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: luckySum(3, 3, 13) expected 6");
            failed++;
        }

        System.out.println("luckySum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}