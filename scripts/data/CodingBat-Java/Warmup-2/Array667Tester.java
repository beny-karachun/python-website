/**
 * Tester for Array667 - CodingBat Java
 * 3 test cases
 */
public class Array667Tester {

    public static void main(String[] args) {
        Array667 obj = new Array667();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.array667({6, 6, 2]) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: array667([6, 6, 2]) expected 1");
            failed++;
        }

        // Test 2
        if (obj.array667({6, 6, 2, 6]) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: array667([6, 6, 2, 6]) expected 1");
            failed++;
        }

        // Test 3
        if (obj.array667({6, 7, 2, 6]) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: array667([6, 7, 2, 6]) expected 1");
            failed++;
        }

        System.out.println("array667: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}