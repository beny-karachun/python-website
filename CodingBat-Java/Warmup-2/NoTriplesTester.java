/**
 * Tester for NoTriples - CodingBat Java
 * 3 test cases
 */
public class NoTriplesTester {

    public static void main(String[] args) {
        NoTriples obj = new NoTriples();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.noTriples({1, 1, 2, 2, 1]) == true) {
            passed++;
        } else {
            System.out.println("FAIL: noTriples([1, 1, 2, 2, 1]) expected true");
            failed++;
        }

        // Test 2
        if (obj.noTriples({1, 1, 2, 2, 2, 1]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: noTriples([1, 1, 2, 2, 2, 1]) expected false");
            failed++;
        }

        // Test 3
        if (obj.noTriples({1, 1, 1, 2, 2, 2, 1]) == false) {
            passed++;
        } else {
            System.out.println("FAIL: noTriples([1, 1, 1, 2, 2, 2, 1]) expected false");
            failed++;
        }

        System.out.println("noTriples: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}