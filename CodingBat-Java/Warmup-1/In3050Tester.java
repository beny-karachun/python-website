/**
 * Tester for In3050 - CodingBat Java
 * 12 test cases
 */
public class In3050Tester {

    public static void main(String[] args) {
        In3050 obj = new In3050();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.in3050(30, 31) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(30, 31) expected true");
            failed++;
        }

        // Test 2
        if (obj.in3050(30, 41) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(30, 41) expected false");
            failed++;
        }

        // Test 3
        if (obj.in3050(40, 50) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(40, 50) expected true");
            failed++;
        }

        // Test 4
        if (obj.in3050(40, 51) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(40, 51) expected false");
            failed++;
        }

        // Test 5
        if (obj.in3050(39, 50) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(39, 50) expected false");
            failed++;
        }

        // Test 6
        if (obj.in3050(50, 39) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(50, 39) expected false");
            failed++;
        }

        // Test 7
        if (obj.in3050(40, 39) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(40, 39) expected true");
            failed++;
        }

        // Test 8
        if (obj.in3050(49, 48) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(49, 48) expected true");
            failed++;
        }

        // Test 9
        if (obj.in3050(50, 40) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(50, 40) expected true");
            failed++;
        }

        // Test 10
        if (obj.in3050(50, 51) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(50, 51) expected false");
            failed++;
        }

        // Test 11
        if (obj.in3050(35, 36) == true) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(35, 36) expected true");
            failed++;
        }

        // Test 12
        if (obj.in3050(35, 45) == false) {
            passed++;
        } else {
            System.out.println("FAIL: in3050(35, 45) expected false");
            failed++;
        }

        System.out.println("in3050: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}