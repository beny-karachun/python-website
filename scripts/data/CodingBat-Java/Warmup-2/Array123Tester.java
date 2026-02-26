/**
 * Tester for Array123 - CodingBat Java
 * 3 test cases
 */
public class Array123Tester {

    public static void main(String[] args) {
        Array123 obj = new Array123();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.array123({1, 1, 2, 3, 1]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: array123([1, 1, 2, 3, 1]) expected true");
            failed++;
        }

        // Test 2
        if (obj.array123({1, 1, 2, 4, 1]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: array123([1, 1, 2, 4, 1]) expected false");
            failed++;
        }

        // Test 3
        if (obj.array123({1, 1, 2, 1, 2, 3]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: array123([1, 1, 2, 1, 2, 3]) expected true");
            failed++;
        }

        System.out.println("array123: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}