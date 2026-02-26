/**
 * Tester for LessBy10 - CodingBat Java
 * 14 test cases
 */
public class LessBy10Tester {

    public static void main(String[] args) {
        LessBy10 obj = new LessBy10();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.lessBy10(1, 7, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(1, 7, 11) expected true");
            failed++;
        }

        // Test 2
        if (obj.lessBy10(1, 7, 10) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(1, 7, 10) expected false");
            failed++;
        }

        // Test 3
        if (obj.lessBy10(11, 1, 7) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(11, 1, 7) expected true");
            failed++;
        }

        // Test 4
        if (obj.lessBy10(10, 7, 1) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(10, 7, 1) expected false");
            failed++;
        }

        // Test 5
        if (obj.lessBy10(-10, 2, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(-10, 2, 2) expected true");
            failed++;
        }

        // Test 6
        if (obj.lessBy10(2, 11, 11) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(2, 11, 11) expected false");
            failed++;
        }

        // Test 7
        if (obj.lessBy10(3, 3, 30) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(3, 3, 30) expected true");
            failed++;
        }

        // Test 8
        if (obj.lessBy10(3, 3, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(3, 3, 3) expected false");
            failed++;
        }

        // Test 9
        if (obj.lessBy10(10, 1, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(10, 1, 11) expected true");
            failed++;
        }

        // Test 10
        if (obj.lessBy10(10, 11, 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(10, 11, 1) expected true");
            failed++;
        }

        // Test 11
        if (obj.lessBy10(10, 11, 2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(10, 11, 2) expected false");
            failed++;
        }

        // Test 12
        if (obj.lessBy10(3, 30, 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(3, 30, 3) expected true");
            failed++;
        }

        // Test 13
        if (obj.lessBy10(2, 2, -8) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(2, 2, -8) expected true");
            failed++;
        }

        // Test 14
        if (obj.lessBy10(2, 8, 12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: lessBy10(2, 8, 12) expected true");
            failed++;
        }

        System.out.println("lessBy10: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}