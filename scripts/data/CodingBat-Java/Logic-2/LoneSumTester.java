/**
 * Tester for LoneSum - CodingBat Java
 * 9 test cases
 */
public class LoneSumTester {

    public static void main(String[] args) {
        LoneSum obj = new LoneSum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.loneSum(1, 2, 3) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(1, 2, 3) expected 6");
            failed++;
        }

        // Test 2
        if (obj.loneSum(3, 2, 3) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(3, 2, 3) expected 2");
            failed++;
        }

        // Test 3
        if (obj.loneSum(3, 3, 3) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(3, 3, 3) expected 0");
            failed++;
        }

        // Test 4
        if (obj.loneSum(9, 2, 2) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(9, 2, 2) expected 9");
            failed++;
        }

        // Test 5
        if (obj.loneSum(2, 2, 9) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(2, 2, 9) expected 9");
            failed++;
        }

        // Test 6
        if (obj.loneSum(2, 9, 2) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(2, 9, 2) expected 9");
            failed++;
        }

        // Test 7
        if (obj.loneSum(2, 9, 3) == 14) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(2, 9, 3) expected 14");
            failed++;
        }

        // Test 8
        if (obj.loneSum(4, 2, 3) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(4, 2, 3) expected 9");
            failed++;
        }

        // Test 9
        if (obj.loneSum(1, 3, 1) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: loneSum(1, 3, 1) expected 3");
            failed++;
        }

        System.out.println("loneSum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}