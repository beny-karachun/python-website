/**
 * Tester for More20 - CodingBat Java
 * 21 test cases
 */
public class More20Tester {

    public static void main(String[] args) {
        More20 obj = new More20();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.more20(20) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(20) expected false");
            failed++;
        }

        // Test 2
        if (obj.more20(21) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(21) expected true");
            failed++;
        }

        // Test 3
        if (obj.more20(22) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(22) expected true");
            failed++;
        }

        // Test 4
        if (obj.more20(23) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(23) expected false");
            failed++;
        }

        // Test 5
        if (obj.more20(25) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(25) expected false");
            failed++;
        }

        // Test 6
        if (obj.more20(30) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(30) expected false");
            failed++;
        }

        // Test 7
        if (obj.more20(31) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(31) expected false");
            failed++;
        }

        // Test 8
        if (obj.more20(59) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(59) expected false");
            failed++;
        }

        // Test 9
        if (obj.more20(60) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(60) expected false");
            failed++;
        }

        // Test 10
        if (obj.more20(61) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(61) expected true");
            failed++;
        }

        // Test 11
        if (obj.more20(62) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(62) expected true");
            failed++;
        }

        // Test 12
        if (obj.more20(1020) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(1020) expected false");
            failed++;
        }

        // Test 13
        if (obj.more20(1021) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(1021) expected true");
            failed++;
        }

        // Test 14
        if (obj.more20(1000) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(1000) expected false");
            failed++;
        }

        // Test 15
        if (obj.more20(1001) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(1001) expected true");
            failed++;
        }

        // Test 16
        if (obj.more20(50) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(50) expected false");
            failed++;
        }

        // Test 17
        if (obj.more20(55) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(55) expected false");
            failed++;
        }

        // Test 18
        if (obj.more20(40) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(40) expected false");
            failed++;
        }

        // Test 19
        if (obj.more20(41) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(41) expected true");
            failed++;
        }

        // Test 20
        if (obj.more20(39) == false) {
            passed++;
        } else {
            System.out.println("FAIL: more20(39) expected false");
            failed++;
        }

        // Test 21
        if (obj.more20(42) == true) {
            passed++;
        } else {
            System.out.println("FAIL: more20(42) expected true");
            failed++;
        }

        System.out.println("more20: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}