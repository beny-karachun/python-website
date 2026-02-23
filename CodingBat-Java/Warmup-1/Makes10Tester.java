/**
 * Tester for Makes10 - CodingBat Java
 * 9 test cases
 */
public class Makes10Tester {

    public static void main(String[] args) {
        Makes10 obj = new Makes10();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.makes10(9, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(9, 10) expected true");
            failed++;
        }

        // Test 2
        if (obj.makes10(9, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(9, 9) expected false");
            failed++;
        }

        // Test 3
        if (obj.makes10(1, 9) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(1, 9) expected true");
            failed++;
        }

        // Test 4
        if (obj.makes10(10, 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(10, 1) expected true");
            failed++;
        }

        // Test 5
        if (obj.makes10(10, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(10, 10) expected true");
            failed++;
        }

        // Test 6
        if (obj.makes10(8, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(8, 2) expected true");
            failed++;
        }

        // Test 7
        if (obj.makes10(8, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(8, 3) expected false");
            failed++;
        }

        // Test 8
        if (obj.makes10(10, 42) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(10, 42) expected true");
            failed++;
        }

        // Test 9
        if (obj.makes10(12, -2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makes10(12, -2) expected true");
            failed++;
        }

        System.out.println("makes10: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}