/**
 * Tester for In1020 - CodingBat Java
 * 7 test cases
 */
public class In1020Tester {

    public static void main(String[] args) {
        In1020 obj = new In1020();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.in1020(12, 99) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(12, 99) expected true");
            failed++;
        }

        // Test 2
        if (obj.in1020(21, 12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(21, 12) expected true");
            failed++;
        }

        // Test 3
        if (obj.in1020(8, 99) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(8, 99) expected false");
            failed++;
        }

        // Test 4
        if (obj.in1020(99, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(99, 10) expected true");
            failed++;
        }

        // Test 5
        if (obj.in1020(20, 20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(20, 20) expected true");
            failed++;
        }

        // Test 6
        if (obj.in1020(21, 21) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(21, 21) expected false");
            failed++;
        }

        // Test 7
        if (obj.in1020(9, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in1020(9, 9) expected false");
            failed++;
        }

        System.out.println("in1020: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}