/**
 * Tester for CloseFar - CodingBat Java
 * 12 test cases
 */
public class CloseFarTester {

    public static void main(String[] args) {
        CloseFar obj = new CloseFar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.closeFar(1, 2, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(1, 2, 10) expected true");
            failed++;
        }

        // Test 2
        if (obj.closeFar(1, 2, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(1, 2, 3) expected false");
            failed++;
        }

        // Test 3
        if (obj.closeFar(4, 1, 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(4, 1, 3) expected true");
            failed++;
        }

        // Test 4
        if (obj.closeFar(4, 5, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(4, 5, 3) expected false");
            failed++;
        }

        // Test 5
        if (obj.closeFar(4, 3, 5) == false) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(4, 3, 5) expected false");
            failed++;
        }

        // Test 6
        if (obj.closeFar(-1, 10, 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(-1, 10, 0) expected true");
            failed++;
        }

        // Test 7
        if (obj.closeFar(0, -1, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(0, -1, 10) expected true");
            failed++;
        }

        // Test 8
        if (obj.closeFar(10, 10, 8) == true) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(10, 10, 8) expected true");
            failed++;
        }

        // Test 9
        if (obj.closeFar(10, 8, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(10, 8, 9) expected false");
            failed++;
        }

        // Test 10
        if (obj.closeFar(8, 9, 10) == false) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(8, 9, 10) expected false");
            failed++;
        }

        // Test 11
        if (obj.closeFar(8, 9, 7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(8, 9, 7) expected false");
            failed++;
        }

        // Test 12
        if (obj.closeFar(8, 6, 9) == true) {
            passed++;
        } else {
            System.out.println("FAIL: closeFar(8, 6, 9) expected true");
            failed++;
        }

        System.out.println("closeFar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}