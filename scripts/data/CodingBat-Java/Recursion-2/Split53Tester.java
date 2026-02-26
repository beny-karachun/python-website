/**
 * Tester for Split53 - CodingBat Java
 * 3 test cases
 */
public class Split53Tester {

    public static void main(String[] args) {
        Split53 obj = new Split53();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.split53({1, 1]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: split53([1, 1]) expected true");
            failed++;
        }

        // Test 2
        if (obj.split53({1, 1, 1]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: split53([1, 1, 1]) expected false");
            failed++;
        }

        // Test 3
        if (obj.split53({2, 4, 2]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: split53([2, 4, 2]) expected true");
            failed++;
        }

        System.out.println("split53: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}