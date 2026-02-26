/**
 * Tester for NearTen - CodingBat Java
 * 15 test cases
 */
public class NearTenTester {

    public static void main(String[] args) {
        NearTen obj = new NearTen();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.nearTen(12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(12) expected true");
            failed++;
        }

        // Test 2
        if (obj.nearTen(17) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(17) expected false");
            failed++;
        }

        // Test 3
        if (obj.nearTen(19) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(19) expected true");
            failed++;
        }

        // Test 4
        if (obj.nearTen(31) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(31) expected true");
            failed++;
        }

        // Test 5
        if (obj.nearTen(6) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(6) expected false");
            failed++;
        }

        // Test 6
        if (obj.nearTen(10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(10) expected true");
            failed++;
        }

        // Test 7
        if (obj.nearTen(11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(11) expected true");
            failed++;
        }

        // Test 8
        if (obj.nearTen(21) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(21) expected true");
            failed++;
        }

        // Test 9
        if (obj.nearTen(22) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(22) expected true");
            failed++;
        }

        // Test 10
        if (obj.nearTen(23) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(23) expected false");
            failed++;
        }

        // Test 11
        if (obj.nearTen(54) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(54) expected false");
            failed++;
        }

        // Test 12
        if (obj.nearTen(155) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(155) expected false");
            failed++;
        }

        // Test 13
        if (obj.nearTen(158) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(158) expected true");
            failed++;
        }

        // Test 14
        if (obj.nearTen(3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(3) expected false");
            failed++;
        }

        // Test 15
        if (obj.nearTen(1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearTen(1) expected true");
            failed++;
        }

        System.out.println("nearTen: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}