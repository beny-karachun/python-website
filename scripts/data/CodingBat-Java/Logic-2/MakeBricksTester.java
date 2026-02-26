/**
 * Tester for MakeBricks - CodingBat Java
 * 29 test cases
 */
public class MakeBricksTester {

    public static void main(String[] args) {
        MakeBricks obj = new MakeBricks();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.makeBricks(3, 1, 8) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(3, 1, 8) expected true");
            failed++;
        }

        // Test 2
        if (obj.makeBricks(3, 1, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(3, 1, 9) expected false");
            failed++;
        }

        // Test 3
        if (obj.makeBricks(3, 2, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(3, 2, 10) expected true");
            failed++;
        }

        // Test 4
        if (obj.makeBricks(3, 2, 8) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(3, 2, 8) expected true");
            failed++;
        }

        // Test 5
        if (obj.makeBricks(3, 2, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(3, 2, 9) expected false");
            failed++;
        }

        // Test 6
        if (obj.makeBricks(6, 1, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(6, 1, 11) expected true");
            failed++;
        }

        // Test 7
        if (obj.makeBricks(6, 0, 11) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(6, 0, 11) expected false");
            failed++;
        }

        // Test 8
        if (obj.makeBricks(1, 4, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(1, 4, 11) expected true");
            failed++;
        }

        // Test 9
        if (obj.makeBricks(0, 3, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(0, 3, 10) expected true");
            failed++;
        }

        // Test 10
        if (obj.makeBricks(1, 4, 12) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(1, 4, 12) expected false");
            failed++;
        }

        // Test 11
        if (obj.makeBricks(3, 1, 7) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(3, 1, 7) expected true");
            failed++;
        }

        // Test 12
        if (obj.makeBricks(1, 1, 7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(1, 1, 7) expected false");
            failed++;
        }

        // Test 13
        if (obj.makeBricks(2, 1, 7) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(2, 1, 7) expected true");
            failed++;
        }

        // Test 14
        if (obj.makeBricks(7, 1, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(7, 1, 11) expected true");
            failed++;
        }

        // Test 15
        if (obj.makeBricks(7, 1, 8) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(7, 1, 8) expected true");
            failed++;
        }

        // Test 16
        if (obj.makeBricks(7, 1, 13) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(7, 1, 13) expected false");
            failed++;
        }

        // Test 17
        if (obj.makeBricks(43, 1, 46) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(43, 1, 46) expected true");
            failed++;
        }

        // Test 18
        if (obj.makeBricks(40, 1, 46) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(40, 1, 46) expected false");
            failed++;
        }

        // Test 19
        if (obj.makeBricks(40, 2, 47) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(40, 2, 47) expected true");
            failed++;
        }

        // Test 20
        if (obj.makeBricks(40, 2, 50) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(40, 2, 50) expected true");
            failed++;
        }

        // Test 21
        if (obj.makeBricks(40, 2, 52) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(40, 2, 52) expected false");
            failed++;
        }

        // Test 22
        if (obj.makeBricks(22, 2, 33) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(22, 2, 33) expected false");
            failed++;
        }

        // Test 23
        if (obj.makeBricks(0, 2, 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(0, 2, 10) expected true");
            failed++;
        }

        // Test 24
        if (obj.makeBricks(1000000, 1000, 1000100) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(1000000, 1000, 1000100) expected true");
            failed++;
        }

        // Test 25
        if (obj.makeBricks(2, 1000000, 100003) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(2, 1000000, 100003) expected false");
            failed++;
        }

        // Test 26
        if (obj.makeBricks(20, 0, 19) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(20, 0, 19) expected true");
            failed++;
        }

        // Test 27
        if (obj.makeBricks(20, 0, 21) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(20, 0, 21) expected false");
            failed++;
        }

        // Test 28
        if (obj.makeBricks(20, 4, 51) == false) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(20, 4, 51) expected false");
            failed++;
        }

        // Test 29
        if (obj.makeBricks(20, 4, 39) == true) {
            passed++;
        } else {
            System.out.println("FAIL: makeBricks(20, 4, 39) expected true");
            failed++;
        }

        System.out.println("makeBricks: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}