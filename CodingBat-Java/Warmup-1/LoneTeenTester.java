/**
 * Tester for LoneTeen - CodingBat Java
 * 13 test cases
 */
public class LoneTeenTester {

    public static void main(String[] args) {
        LoneTeen obj = new LoneTeen();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.loneTeen(13, 99) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(13, 99) expected true");
            failed++;
        }

        // Test 2
        if (obj.loneTeen(21, 19) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(21, 19) expected true");
            failed++;
        }

        // Test 3
        if (obj.loneTeen(13, 13) == false) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(13, 13) expected false");
            failed++;
        }

        // Test 4
        if (obj.loneTeen(14, 20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(14, 20) expected true");
            failed++;
        }

        // Test 5
        if (obj.loneTeen(20, 15) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(20, 15) expected true");
            failed++;
        }

        // Test 6
        if (obj.loneTeen(16, 17) == false) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(16, 17) expected false");
            failed++;
        }

        // Test 7
        if (obj.loneTeen(16, 9) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(16, 9) expected true");
            failed++;
        }

        // Test 8
        if (obj.loneTeen(16, 18) == false) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(16, 18) expected false");
            failed++;
        }

        // Test 9
        if (obj.loneTeen(13, 19) == false) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(13, 19) expected false");
            failed++;
        }

        // Test 10
        if (obj.loneTeen(13, 20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(13, 20) expected true");
            failed++;
        }

        // Test 11
        if (obj.loneTeen(6, 18) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(6, 18) expected true");
            failed++;
        }

        // Test 12
        if (obj.loneTeen(99, 13) == true) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(99, 13) expected true");
            failed++;
        }

        // Test 13
        if (obj.loneTeen(99, 99) == false) {
            passed++;
        } else {
            System.out.println("FAIL: loneTeen(99, 99) expected false");
            failed++;
        }

        System.out.println("loneTeen: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}