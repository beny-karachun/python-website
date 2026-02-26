/**
 * Tester for Array6 - CodingBat Java
 * 3 test cases
 */
public class Array6Tester {

    public static void main(String[] args) {
        Array6 obj = new Array6();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.array6({1, 6, 4], 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: array6([1, 6, 4], 0) expected true");
            failed++;
        }

        // Test 2
        if (obj.array6({1, 4], 0) == false) {
            passed++;
        } else {
            System.out.println("FAIL: array6([1, 4], 0) expected false");
            failed++;
        }

        // Test 3
        if (obj.array6({6}, 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: array6([6], 0) expected true");
            failed++;
        }

        System.out.println("array6: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}