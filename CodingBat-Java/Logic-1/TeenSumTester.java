/**
 * Tester for TeenSum - CodingBat Java
 * 16 test cases
 */
public class TeenSumTester {

    public static void main(String[] args) {
        TeenSum obj = new TeenSum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.teenSum(3, 4) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(3, 4) expected 7");
            failed++;
        }

        // Test 2
        if (obj.teenSum(10, 13) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(10, 13) expected 19");
            failed++;
        }

        // Test 3
        if (obj.teenSum(13, 2) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(13, 2) expected 19");
            failed++;
        }

        // Test 4
        if (obj.teenSum(3, 19) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(3, 19) expected 19");
            failed++;
        }

        // Test 5
        if (obj.teenSum(13, 13) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(13, 13) expected 19");
            failed++;
        }

        // Test 6
        if (obj.teenSum(10, 10) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(10, 10) expected 20");
            failed++;
        }

        // Test 7
        if (obj.teenSum(6, 14) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(6, 14) expected 19");
            failed++;
        }

        // Test 8
        if (obj.teenSum(15, 2) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(15, 2) expected 19");
            failed++;
        }

        // Test 9
        if (obj.teenSum(19, 19) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(19, 19) expected 19");
            failed++;
        }

        // Test 10
        if (obj.teenSum(19, 20) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(19, 20) expected 19");
            failed++;
        }

        // Test 11
        if (obj.teenSum(2, 18) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(2, 18) expected 19");
            failed++;
        }

        // Test 12
        if (obj.teenSum(12, 4) == 16) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(12, 4) expected 16");
            failed++;
        }

        // Test 13
        if (obj.teenSum(2, 20) == 22) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(2, 20) expected 22");
            failed++;
        }

        // Test 14
        if (obj.teenSum(2, 17) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(2, 17) expected 19");
            failed++;
        }

        // Test 15
        if (obj.teenSum(2, 16) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(2, 16) expected 19");
            failed++;
        }

        // Test 16
        if (obj.teenSum(6, 7) == 13) {
            passed++;
        } else {
            System.out.println("FAIL: teenSum(6, 7) expected 13");
            failed++;
        }

        System.out.println("teenSum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}