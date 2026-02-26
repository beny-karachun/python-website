/**
 * Tester for PowerN - CodingBat Java
 * 11 test cases
 */
public class PowerNTester {

    public static void main(String[] args) {
        PowerN obj = new PowerN();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.powerN(3, 1) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(3, 1) expected 3");
            failed++;
        }

        // Test 2
        if (obj.powerN(3, 2) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(3, 2) expected 9");
            failed++;
        }

        // Test 3
        if (obj.powerN(3, 3) == 27) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(3, 3) expected 27");
            failed++;
        }

        // Test 4
        if (obj.powerN(2, 1) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(2, 1) expected 2");
            failed++;
        }

        // Test 5
        if (obj.powerN(2, 2) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(2, 2) expected 4");
            failed++;
        }

        // Test 6
        if (obj.powerN(2, 3) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(2, 3) expected 8");
            failed++;
        }

        // Test 7
        if (obj.powerN(2, 4) == 16) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(2, 4) expected 16");
            failed++;
        }

        // Test 8
        if (obj.powerN(2, 5) == 32) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(2, 5) expected 32");
            failed++;
        }

        // Test 9
        if (obj.powerN(10, 1) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(10, 1) expected 10");
            failed++;
        }

        // Test 10
        if (obj.powerN(10, 2) == 100) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(10, 2) expected 100");
            failed++;
        }

        // Test 11
        if (obj.powerN(10, 3) == 1000) {
            passed++;
        } else {
            System.out.println("FAIL: powerN(10, 3) expected 1000");
            failed++;
        }

        System.out.println("powerN: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}