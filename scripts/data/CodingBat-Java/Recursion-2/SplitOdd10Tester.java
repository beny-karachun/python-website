/**
 * Tester for SplitOdd10 - CodingBat Java
 * 3 test cases
 */
public class SplitOdd10Tester {

    public static void main(String[] args) {
        SplitOdd10 obj = new SplitOdd10();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.splitOdd10({5, 5, 5]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: splitOdd10([5, 5, 5]) expected true");
            failed++;
        }

        // Test 2
        if (obj.splitOdd10({5, 5, 6]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: splitOdd10([5, 5, 6]) expected false");
            failed++;
        }

        // Test 3
        if (obj.splitOdd10({5, 5, 6, 1]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: splitOdd10([5, 5, 6, 1]) expected true");
            failed++;
        }

        System.out.println("splitOdd10: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}