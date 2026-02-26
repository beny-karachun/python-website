/**
 * Tester for SortaSum - CodingBat Java
 * 9 test cases
 */
public class SortaSumTester {

    public static void main(String[] args) {
        SortaSum obj = new SortaSum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sortaSum(3, 4) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(3, 4) expected 7");
            failed++;
        }

        // Test 2
        if (obj.sortaSum(9, 4) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(9, 4) expected 20");
            failed++;
        }

        // Test 3
        if (obj.sortaSum(10, 11) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(10, 11) expected 21");
            failed++;
        }

        // Test 4
        if (obj.sortaSum(12, -3) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(12, -3) expected 9");
            failed++;
        }

        // Test 5
        if (obj.sortaSum(-3, 12) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(-3, 12) expected 9");
            failed++;
        }

        // Test 6
        if (obj.sortaSum(4, 5) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(4, 5) expected 9");
            failed++;
        }

        // Test 7
        if (obj.sortaSum(4, 6) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(4, 6) expected 20");
            failed++;
        }

        // Test 8
        if (obj.sortaSum(14, 7) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(14, 7) expected 21");
            failed++;
        }

        // Test 9
        if (obj.sortaSum(14, 6) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: sortaSum(14, 6) expected 20");
            failed++;
        }

        System.out.println("sortaSum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}