/**
 * Tester for MaxMod5 - CodingBat Java
 * 11 test cases
 */
public class MaxMod5Tester {

    public static void main(String[] args) {
        MaxMod5 obj = new MaxMod5();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.maxMod5(2, 3) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(2, 3) expected 3");
            failed++;
        }

        // Test 2
        if (obj.maxMod5(6, 2) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(6, 2) expected 6");
            failed++;
        }

        // Test 3
        if (obj.maxMod5(3, 2) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(3, 2) expected 3");
            failed++;
        }

        // Test 4
        if (obj.maxMod5(8, 12) == 12) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(8, 12) expected 12");
            failed++;
        }

        // Test 5
        if (obj.maxMod5(7, 12) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(7, 12) expected 7");
            failed++;
        }

        // Test 6
        if (obj.maxMod5(11, 6) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(11, 6) expected 6");
            failed++;
        }

        // Test 7
        if (obj.maxMod5(2, 7) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(2, 7) expected 2");
            failed++;
        }

        // Test 8
        if (obj.maxMod5(7, 7) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(7, 7) expected 0");
            failed++;
        }

        // Test 9
        if (obj.maxMod5(9, 1) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(9, 1) expected 9");
            failed++;
        }

        // Test 10
        if (obj.maxMod5(9, 14) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(9, 14) expected 9");
            failed++;
        }

        // Test 11
        if (obj.maxMod5(1, 2) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: maxMod5(1, 2) expected 2");
            failed++;
        }

        System.out.println("maxMod5: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}