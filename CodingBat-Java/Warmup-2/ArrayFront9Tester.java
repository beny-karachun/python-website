/**
 * Tester for ArrayFront9 - CodingBat Java
 * 3 test cases
 */
public class ArrayFront9Tester {

    public static void main(String[] args) {
        ArrayFront9 obj = new ArrayFront9();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.arrayFront9({1, 2, 9, 3, 4]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: arrayFront9([1, 2, 9, 3, 4]) expected true");
            failed++;
        }

        // Test 2
        if (obj.arrayFront9({1, 2, 3, 4, 9]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: arrayFront9([1, 2, 3, 4, 9]) expected false");
            failed++;
        }

        // Test 3
        if (obj.arrayFront9({1, 2, 3, 4, 5]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: arrayFront9([1, 2, 3, 4, 5]) expected false");
            failed++;
        }

        System.out.println("arrayFront9: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}