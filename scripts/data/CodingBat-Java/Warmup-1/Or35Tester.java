/**
 * Tester for Or35 - CodingBat Java
 * 22 test cases
 */
public class Or35Tester {

    public static void main(String[] args) {
        Or35 obj = new Or35();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.or35(3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(3) expected true");
            failed++;
        }

        // Test 2
        if (obj.or35(10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(10) expected true");
            failed++;
        }

        // Test 3
        if (obj.or35(8) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(8) expected false");
            failed++;
        }

        // Test 4
        if (obj.or35(15) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(15) expected true");
            failed++;
        }

        // Test 5
        if (obj.or35(5) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(5) expected true");
            failed++;
        }

        // Test 6
        if (obj.or35(9) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(9) expected true");
            failed++;
        }

        // Test 7
        if (obj.or35(4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(4) expected false");
            failed++;
        }

        // Test 8
        if (obj.or35(7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(7) expected false");
            failed++;
        }

        // Test 9
        if (obj.or35(6) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(6) expected true");
            failed++;
        }

        // Test 10
        if (obj.or35(17) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(17) expected false");
            failed++;
        }

        // Test 11
        if (obj.or35(18) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(18) expected true");
            failed++;
        }

        // Test 12
        if (obj.or35(29) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(29) expected false");
            failed++;
        }

        // Test 13
        if (obj.or35(20) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(20) expected true");
            failed++;
        }

        // Test 14
        if (obj.or35(21) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(21) expected true");
            failed++;
        }

        // Test 15
        if (obj.or35(22) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(22) expected false");
            failed++;
        }

        // Test 16
        if (obj.or35(45) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(45) expected true");
            failed++;
        }

        // Test 17
        if (obj.or35(99) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(99) expected true");
            failed++;
        }

        // Test 18
        if (obj.or35(100) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(100) expected true");
            failed++;
        }

        // Test 19
        if (obj.or35(101) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(101) expected false");
            failed++;
        }

        // Test 20
        if (obj.or35(121) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(121) expected false");
            failed++;
        }

        // Test 21
        if (obj.or35(122) == false) {
            passed++;
        } else {
            System.out.println("FAIL: or35(122) expected false");
            failed++;
        }

        // Test 22
        if (obj.or35(123) == true) {
            passed++;
        } else {
            System.out.println("FAIL: or35(123) expected true");
            failed++;
        }

        System.out.println("or35: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}