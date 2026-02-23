/**
 * Tester for InOrder - CodingBat Java
 * 12 test cases
 */
public class InOrderTester {

    public static void main(String[] args) {
        InOrder obj = new InOrder();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.inOrder(1, 2, 4, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(1, 2, 4, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.inOrder(1, 2, 1, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(1, 2, 1, false) expected false");
            failed++;
        }

        // Test 3
        if (obj.inOrder(1, 1, 2, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(1, 1, 2, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.inOrder(3, 2, 4, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(3, 2, 4, false) expected false");
            failed++;
        }

        // Test 5
        if (obj.inOrder(2, 3, 4, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(2, 3, 4, false) expected true");
            failed++;
        }

        // Test 6
        if (obj.inOrder(3, 2, 4, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(3, 2, 4, true) expected true");
            failed++;
        }

        // Test 7
        if (obj.inOrder(4, 2, 2, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(4, 2, 2, true) expected false");
            failed++;
        }

        // Test 8
        if (obj.inOrder(4, 5, 2, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(4, 5, 2, true) expected false");
            failed++;
        }

        // Test 9
        if (obj.inOrder(2, 4, 6, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(2, 4, 6, true) expected true");
            failed++;
        }

        // Test 10
        if (obj.inOrder(7, 9, 10, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(7, 9, 10, false) expected true");
            failed++;
        }

        // Test 11
        if (obj.inOrder(7, 5, 6, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(7, 5, 6, true) expected true");
            failed++;
        }

        // Test 12
        if (obj.inOrder(7, 5, 4, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrder(7, 5, 4, true) expected false");
            failed++;
        }

        System.out.println("inOrder: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}