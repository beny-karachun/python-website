/**
 * Tester for Old35 - CodingBat Java
 * 16 test cases
 */
public class Old35Tester {

    public static void main(String[] args) {
        Old35 obj = new Old35();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.old35(3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(3) expected true");
            failed++;
        }

        // Test 2
        if (obj.old35(10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(10) expected true");
            failed++;
        }

        // Test 3
        if (obj.old35(15) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(15) expected false");
            failed++;
        }

        // Test 4
        if (obj.old35(5) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(5) expected true");
            failed++;
        }

        // Test 5
        if (obj.old35(9) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(9) expected true");
            failed++;
        }

        // Test 6
        if (obj.old35(8) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(8) expected false");
            failed++;
        }

        // Test 7
        if (obj.old35(7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(7) expected false");
            failed++;
        }

        // Test 8
        if (obj.old35(6) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(6) expected true");
            failed++;
        }

        // Test 9
        if (obj.old35(17) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(17) expected false");
            failed++;
        }

        // Test 10
        if (obj.old35(18) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(18) expected true");
            failed++;
        }

        // Test 11
        if (obj.old35(29) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(29) expected false");
            failed++;
        }

        // Test 12
        if (obj.old35(20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(20) expected true");
            failed++;
        }

        // Test 13
        if (obj.old35(21) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(21) expected true");
            failed++;
        }

        // Test 14
        if (obj.old35(22) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(22) expected false");
            failed++;
        }

        // Test 15
        if (obj.old35(45) == false) {
            passed++;
        } else {
            System.out.println("FAIL: old35(45) expected false");
            failed++;
        }

        // Test 16
        if (obj.old35(99) == true) {
            passed++;
        } else {
            System.out.println("FAIL: old35(99) expected true");
            failed++;
        }

        System.out.println("old35: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}