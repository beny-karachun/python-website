/**
 * Tester for Love6 - CodingBat Java
 * 20 test cases
 */
public class Love6Tester {

    public static void main(String[] args) {
        Love6 obj = new Love6();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.love6(6, 4) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(6, 4) expected true");
            failed++;
        }

        // Test 2
        if (obj.love6(4, 5) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(4, 5) expected false");
            failed++;
        }

        // Test 3
        if (obj.love6(1, 5) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(1, 5) expected true");
            failed++;
        }

        // Test 4
        if (obj.love6(1, 6) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(1, 6) expected true");
            failed++;
        }

        // Test 5
        if (obj.love6(1, 8) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(1, 8) expected false");
            failed++;
        }

        // Test 6
        if (obj.love6(1, 7) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(1, 7) expected true");
            failed++;
        }

        // Test 7
        if (obj.love6(7, 5) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(7, 5) expected false");
            failed++;
        }

        // Test 8
        if (obj.love6(8, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(8, 2) expected true");
            failed++;
        }

        // Test 9
        if (obj.love6(6, 6) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(6, 6) expected true");
            failed++;
        }

        // Test 10
        if (obj.love6(-6, 2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(-6, 2) expected false");
            failed++;
        }

        // Test 11
        if (obj.love6(-4, -10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(-4, -10) expected true");
            failed++;
        }

        // Test 12
        if (obj.love6(-7, 1) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(-7, 1) expected false");
            failed++;
        }

        // Test 13
        if (obj.love6(7, -1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(7, -1) expected true");
            failed++;
        }

        // Test 14
        if (obj.love6(-6, 12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(-6, 12) expected true");
            failed++;
        }

        // Test 15
        if (obj.love6(-2, -4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(-2, -4) expected false");
            failed++;
        }

        // Test 16
        if (obj.love6(7, 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(7, 1) expected true");
            failed++;
        }

        // Test 17
        if (obj.love6(0, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(0, 9) expected false");
            failed++;
        }

        // Test 18
        if (obj.love6(8, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(8, 3) expected false");
            failed++;
        }

        // Test 19
        if (obj.love6(3, 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: love6(3, 3) expected true");
            failed++;
        }

        // Test 20
        if (obj.love6(3, 4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: love6(3, 4) expected false");
            failed++;
        }

        System.out.println("love6: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}