/**
 * Tester for Less20 - CodingBat Java
 * 22 test cases
 */
public class Less20Tester {

    public static void main(String[] args) {
        Less20 obj = new Less20();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.less20(18) == true) {
            passed++;
        } else {
            System.out.println("FAIL: less20(18) expected true");
            failed++;
        }

        // Test 2
        if (obj.less20(19) == true) {
            passed++;
        } else {
            System.out.println("FAIL: less20(19) expected true");
            failed++;
        }

        // Test 3
        if (obj.less20(20) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(20) expected false");
            failed++;
        }

        // Test 4
        if (obj.less20(8) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(8) expected false");
            failed++;
        }

        // Test 5
        if (obj.less20(17) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(17) expected false");
            failed++;
        }

        // Test 6
        if (obj.less20(23) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(23) expected false");
            failed++;
        }

        // Test 7
        if (obj.less20(25) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(25) expected false");
            failed++;
        }

        // Test 8
        if (obj.less20(30) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(30) expected false");
            failed++;
        }

        // Test 9
        if (obj.less20(31) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(31) expected false");
            failed++;
        }

        // Test 10
        if (obj.less20(58) == true) {
            passed++;
        } else {
            System.out.println("FAIL: less20(58) expected true");
            failed++;
        }

        // Test 11
        if (obj.less20(59) == true) {
            passed++;
        } else {
            System.out.println("FAIL: less20(59) expected true");
            failed++;
        }

        // Test 12
        if (obj.less20(60) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(60) expected false");
            failed++;
        }

        // Test 13
        if (obj.less20(61) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(61) expected false");
            failed++;
        }

        // Test 14
        if (obj.less20(62) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(62) expected false");
            failed++;
        }

        // Test 15
        if (obj.less20(1017) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1017) expected false");
            failed++;
        }

        // Test 16
        if (obj.less20(1018) == true) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1018) expected true");
            failed++;
        }

        // Test 17
        if (obj.less20(1019) == true) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1019) expected true");
            failed++;
        }

        // Test 18
        if (obj.less20(1020) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1020) expected false");
            failed++;
        }

        // Test 19
        if (obj.less20(1021) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1021) expected false");
            failed++;
        }

        // Test 20
        if (obj.less20(1022) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1022) expected false");
            failed++;
        }

        // Test 21
        if (obj.less20(1023) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(1023) expected false");
            failed++;
        }

        // Test 22
        if (obj.less20(37) == false) {
            passed++;
        } else {
            System.out.println("FAIL: less20(37) expected false");
            failed++;
        }

        System.out.println("less20: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}