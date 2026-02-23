/**
 * Tester for SplitArray - CodingBat Java
 * 3 test cases
 */
public class SplitArrayTester {

    public static void main(String[] args) {
        SplitArray obj = new SplitArray();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.splitArray({2, 2]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: splitArray([2, 2]) expected true");
            failed++;
        }

        // Test 2
        if (obj.splitArray({2, 3]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: splitArray([2, 3]) expected false");
            failed++;
        }

        // Test 3
        if (obj.splitArray({5, 2, 3]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: splitArray([5, 2, 3]) expected true");
            failed++;
        }

        System.out.println("splitArray: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}