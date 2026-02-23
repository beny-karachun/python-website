/**
 * Tester for EvenlySpaced - CodingBat Java
 * 14 test cases
 */
public class EvenlySpacedTester {

    public static void main(String[] args) {
        EvenlySpaced obj = new EvenlySpaced();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.evenlySpaced(2, 4, 6) == true) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(2, 4, 6) expected true");
            failed++;
        }

        // Test 2
        if (obj.evenlySpaced(4, 6, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(4, 6, 2) expected true");
            failed++;
        }

        // Test 3
        if (obj.evenlySpaced(4, 6, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(4, 6, 3) expected false");
            failed++;
        }

        // Test 4
        if (obj.evenlySpaced(6, 2, 4) == true) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(6, 2, 4) expected true");
            failed++;
        }

        // Test 5
        if (obj.evenlySpaced(6, 2, 8) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(6, 2, 8) expected false");
            failed++;
        }

        // Test 6
        if (obj.evenlySpaced(2, 2, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(2, 2, 2) expected true");
            failed++;
        }

        // Test 7
        if (obj.evenlySpaced(2, 2, 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(2, 2, 3) expected false");
            failed++;
        }

        // Test 8
        if (obj.evenlySpaced(9, 10, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(9, 10, 11) expected true");
            failed++;
        }

        // Test 9
        if (obj.evenlySpaced(10, 9, 11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(10, 9, 11) expected true");
            failed++;
        }

        // Test 10
        if (obj.evenlySpaced(10, 9, 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(10, 9, 9) expected false");
            failed++;
        }

        // Test 11
        if (obj.evenlySpaced(2, 4, 4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(2, 4, 4) expected false");
            failed++;
        }

        // Test 12
        if (obj.evenlySpaced(2, 2, 4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(2, 2, 4) expected false");
            failed++;
        }

        // Test 13
        if (obj.evenlySpaced(3, 6, 12) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(3, 6, 12) expected false");
            failed++;
        }

        // Test 14
        if (obj.evenlySpaced(12, 3, 6) == false) {
            passed++;
        } else {
            System.out.println("FAIL: evenlySpaced(12, 3, 6) expected false");
            failed++;
        }

        System.out.println("evenlySpaced: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}