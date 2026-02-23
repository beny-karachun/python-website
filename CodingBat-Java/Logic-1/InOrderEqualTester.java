/**
 * Tester for InOrderEqual - CodingBat Java
 * 14 test cases
 */
public class InOrderEqualTester {

    public static void main(String[] args) {
        InOrderEqual obj = new InOrderEqual();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.inOrderEqual(2, 5, 11, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(2, 5, 11, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.inOrderEqual(5, 7, 6, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(5, 7, 6, false) expected false");
            failed++;
        }

        // Test 3
        if (obj.inOrderEqual(5, 5, 7, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(5, 5, 7, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.inOrderEqual(5, 5, 7, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(5, 5, 7, false) expected false");
            failed++;
        }

        // Test 5
        if (obj.inOrderEqual(2, 5, 4, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(2, 5, 4, false) expected false");
            failed++;
        }

        // Test 6
        if (obj.inOrderEqual(3, 4, 3, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(3, 4, 3, false) expected false");
            failed++;
        }

        // Test 7
        if (obj.inOrderEqual(3, 4, 4, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(3, 4, 4, false) expected false");
            failed++;
        }

        // Test 8
        if (obj.inOrderEqual(3, 4, 3, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(3, 4, 3, true) expected false");
            failed++;
        }

        // Test 9
        if (obj.inOrderEqual(3, 4, 4, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(3, 4, 4, true) expected true");
            failed++;
        }

        // Test 10
        if (obj.inOrderEqual(1, 5, 5, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(1, 5, 5, true) expected true");
            failed++;
        }

        // Test 11
        if (obj.inOrderEqual(5, 5, 5, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(5, 5, 5, true) expected true");
            failed++;
        }

        // Test 12
        if (obj.inOrderEqual(2, 2, 1, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(2, 2, 1, true) expected false");
            failed++;
        }

        // Test 13
        if (obj.inOrderEqual(9, 2, 2, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(9, 2, 2, true) expected false");
            failed++;
        }

        // Test 14
        if (obj.inOrderEqual(0, 1, 0, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: inOrderEqual(0, 1, 0, true) expected false");
            failed++;
        }

        System.out.println("inOrderEqual: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}