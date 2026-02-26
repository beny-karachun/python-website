/**
 * Tester for Array220 - CodingBat Java
 * 3 test cases
 */
public class Array220Tester {

    public static void main(String[] args) {
        Array220 obj = new Array220();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.array220({1, 2, 20], 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: array220([1, 2, 20], 0) expected true");
            failed++;
        }

        // Test 2
        if (obj.array220({3, 30], 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: array220([3, 30], 0) expected true");
            failed++;
        }

        // Test 3
        if (obj.array220({3}, 0) == false) {
            passed++;
        } else {
            System.out.println("FAIL: array220([3], 0) expected false");
            failed++;
        }

        System.out.println("array220: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}