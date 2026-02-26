/**
 * Tester for ArrayCount9 - CodingBat Java
 * 3 test cases
 */
public class ArrayCount9Tester {

    public static void main(String[] args) {
        ArrayCount9 obj = new ArrayCount9();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.arrayCount9({1, 2, 9]) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: arrayCount9([1, 2, 9]) expected 1");
            failed++;
        }

        // Test 2
        if (obj.arrayCount9({1, 9, 9]) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: arrayCount9([1, 9, 9]) expected 2");
            failed++;
        }

        // Test 3
        if (obj.arrayCount9({1, 9, 9, 3, 9]) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: arrayCount9([1, 9, 9, 3, 9]) expected 3");
            failed++;
        }

        System.out.println("arrayCount9: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}