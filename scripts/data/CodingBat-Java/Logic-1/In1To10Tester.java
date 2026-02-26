/**
 * Tester for In1To10 - CodingBat Java
 * 15 test cases
 */
public class In1To10Tester {

    public static void main(String[] args) {
        In1To10 obj = new In1To10();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.in1To10(5, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(5, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.in1To10(11, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(11, false) expected false");
            failed++;
        }

        // Test 3
        if (obj.in1To10(11, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(11, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.in1To10(10, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(10, false) expected true");
            failed++;
        }

        // Test 5
        if (obj.in1To10(10, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(10, true) expected true");
            failed++;
        }

        // Test 6
        if (obj.in1To10(9, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(9, false) expected true");
            failed++;
        }

        // Test 7
        if (obj.in1To10(9, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(9, true) expected false");
            failed++;
        }

        // Test 8
        if (obj.in1To10(1, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(1, false) expected true");
            failed++;
        }

        // Test 9
        if (obj.in1To10(1, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(1, true) expected true");
            failed++;
        }

        // Test 10
        if (obj.in1To10(0, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(0, false) expected false");
            failed++;
        }

        // Test 11
        if (obj.in1To10(0, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(0, true) expected true");
            failed++;
        }

        // Test 12
        if (obj.in1To10(-1, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(-1, false) expected false");
            failed++;
        }

        // Test 13
        if (obj.in1To10(-1, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(-1, true) expected true");
            failed++;
        }

        // Test 14
        if (obj.in1To10(99, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(99, false) expected false");
            failed++;
        }

        // Test 15
        if (obj.in1To10(-99, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1To10(-99, true) expected true");
            failed++;
        }

        System.out.println("in1To10: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}