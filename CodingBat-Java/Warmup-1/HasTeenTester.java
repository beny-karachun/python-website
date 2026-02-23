/**
 * Tester for HasTeen - CodingBat Java
 * 11 test cases
 */
public class HasTeenTester {

    public static void main(String[] args) {
        HasTeen obj = new HasTeen();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.hasTeen(13, 20, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(13, 20, 10) expected true");
            failed++;
        }

        // Test 2
        if (obj.hasTeen(20, 19, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(20, 19, 10) expected true");
            failed++;
        }

        // Test 3
        if (obj.hasTeen(20, 10, 13) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(20, 10, 13) expected true");
            failed++;
        }

        // Test 4
        if (obj.hasTeen(1, 20, 12) == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(1, 20, 12) expected false");
            failed++;
        }

        // Test 5
        if (obj.hasTeen(19, 20, 12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(19, 20, 12) expected true");
            failed++;
        }

        // Test 6
        if (obj.hasTeen(12, 20, 19) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(12, 20, 19) expected true");
            failed++;
        }

        // Test 7
        if (obj.hasTeen(12, 9, 20) == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(12, 9, 20) expected false");
            failed++;
        }

        // Test 8
        if (obj.hasTeen(12, 18, 20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(12, 18, 20) expected true");
            failed++;
        }

        // Test 9
        if (obj.hasTeen(14, 2, 20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(14, 2, 20) expected true");
            failed++;
        }

        // Test 10
        if (obj.hasTeen(4, 2, 20) == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(4, 2, 20) expected false");
            failed++;
        }

        // Test 11
        if (obj.hasTeen(11, 22, 22) == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasTeen(11, 22, 22) expected false");
            failed++;
        }

        System.out.println("hasTeen: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}