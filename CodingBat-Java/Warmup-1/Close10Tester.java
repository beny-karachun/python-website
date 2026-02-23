/**
 * Tester for Close10 - CodingBat Java
 * 11 test cases
 */
public class Close10Tester {

    public static void main(String[] args) {
        Close10 obj = new Close10();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.close10(8, 13) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: close10(8, 13) expected 8");
            failed++;
        }

        // Test 2
        if (obj.close10(13, 8) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: close10(13, 8) expected 8");
            failed++;
        }

        // Test 3
        if (obj.close10(13, 7) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: close10(13, 7) expected 0");
            failed++;
        }

        // Test 4
        if (obj.close10(7, 13) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: close10(7, 13) expected 0");
            failed++;
        }

        // Test 5
        if (obj.close10(9, 13) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: close10(9, 13) expected 9");
            failed++;
        }

        // Test 6
        if (obj.close10(13, 8) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: close10(13, 8) expected 8");
            failed++;
        }

        // Test 7
        if (obj.close10(10, 12) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: close10(10, 12) expected 10");
            failed++;
        }

        // Test 8
        if (obj.close10(11, 10) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: close10(11, 10) expected 10");
            failed++;
        }

        // Test 9
        if (obj.close10(5, 21) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: close10(5, 21) expected 5");
            failed++;
        }

        // Test 10
        if (obj.close10(0, 20) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: close10(0, 20) expected 0");
            failed++;
        }

        // Test 11
        if (obj.close10(10, 10) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: close10(10, 10) expected 0");
            failed++;
        }

        System.out.println("close10: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}