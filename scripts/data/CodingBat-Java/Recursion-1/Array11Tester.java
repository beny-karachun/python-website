/**
 * Tester for Array11 - CodingBat Java
 * 3 test cases
 */
public class Array11Tester {

    public static void main(String[] args) {
        Array11 obj = new Array11();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.array11({1, 2, 11], 0) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: array11([1, 2, 11], 0) expected 1");
            failed++;
        }

        // Test 2
        if (obj.array11({11, 11], 0) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: array11([11, 11], 0) expected 2");
            failed++;
        }

        // Test 3
        if (obj.array11({1, 2, 3, 4], 0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: array11([1, 2, 3, 4], 0) expected 0");
            failed++;
        }

        System.out.println("array11: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}