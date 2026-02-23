/**
 * Tester for Has271 - CodingBat Java
 * 3 test cases
 */
public class Has271Tester {

    public static void main(String[] args) {
        Has271 obj = new Has271();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.has271({1, 2, 7, 1]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: has271([1, 2, 7, 1]) expected true");
            failed++;
        }

        // Test 2
        if (obj.has271({1, 2, 8, 1]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: has271([1, 2, 8, 1]) expected false");
            failed++;
        }

        // Test 3
        if (obj.has271({2, 7, 1]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: has271([2, 7, 1]) expected true");
            failed++;
        }

        System.out.println("has271: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}