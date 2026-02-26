/**
 * Tester for PosNeg - CodingBat Java
 * 19 test cases
 */
public class PosNegTester {

    public static void main(String[] args) {
        PosNeg obj = new PosNeg();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.posNeg(1, -1, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(1, -1, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.posNeg(-1, 1, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-1, 1, false) expected true");
            failed++;
        }

        // Test 3
        if (obj.posNeg(-4, -5, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-4, -5, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.posNeg(-4, -5, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-4, -5, false) expected false");
            failed++;
        }

        // Test 5
        if (obj.posNeg(-4, 5, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-4, 5, false) expected true");
            failed++;
        }

        // Test 6
        if (obj.posNeg(-4, 5, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-4, 5, true) expected false");
            failed++;
        }

        // Test 7
        if (obj.posNeg(1, 1, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(1, 1, false) expected false");
            failed++;
        }

        // Test 8
        if (obj.posNeg(-1, -1, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-1, -1, false) expected false");
            failed++;
        }

        // Test 9
        if (obj.posNeg(1, -1, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(1, -1, true) expected false");
            failed++;
        }

        // Test 10
        if (obj.posNeg(-1, 1, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-1, 1, true) expected false");
            failed++;
        }

        // Test 11
        if (obj.posNeg(1, 1, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(1, 1, true) expected false");
            failed++;
        }

        // Test 12
        if (obj.posNeg(-1, -1, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-1, -1, true) expected true");
            failed++;
        }

        // Test 13
        if (obj.posNeg(5, -5, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(5, -5, false) expected true");
            failed++;
        }

        // Test 14
        if (obj.posNeg(-6, 6, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-6, 6, false) expected true");
            failed++;
        }

        // Test 15
        if (obj.posNeg(-5, -6, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-5, -6, false) expected false");
            failed++;
        }

        // Test 16
        if (obj.posNeg(-2, -1, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-2, -1, false) expected false");
            failed++;
        }

        // Test 17
        if (obj.posNeg(1, 2, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(1, 2, false) expected false");
            failed++;
        }

        // Test 18
        if (obj.posNeg(-5, 6, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-5, 6, true) expected false");
            failed++;
        }

        // Test 19
        if (obj.posNeg(-5, -5, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: posNeg(-5, -5, true) expected true");
            failed++;
        }

        System.out.println("posNeg: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}