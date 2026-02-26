/**
 * Tester for SpecialEleven - CodingBat Java
 * 20 test cases
 */
public class SpecialElevenTester {

    public static void main(String[] args) {
        SpecialEleven obj = new SpecialEleven();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.specialEleven(22) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(22) expected true");
            failed++;
        }

        // Test 2
        if (obj.specialEleven(23) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(23) expected true");
            failed++;
        }

        // Test 3
        if (obj.specialEleven(24) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(24) expected false");
            failed++;
        }

        // Test 4
        if (obj.specialEleven(21) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(21) expected false");
            failed++;
        }

        // Test 5
        if (obj.specialEleven(11) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(11) expected true");
            failed++;
        }

        // Test 6
        if (obj.specialEleven(12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(12) expected true");
            failed++;
        }

        // Test 7
        if (obj.specialEleven(10) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(10) expected false");
            failed++;
        }

        // Test 8
        if (obj.specialEleven(9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(9) expected false");
            failed++;
        }

        // Test 9
        if (obj.specialEleven(8) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(8) expected false");
            failed++;
        }

        // Test 10
        if (obj.specialEleven(0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(0) expected true");
            failed++;
        }

        // Test 11
        if (obj.specialEleven(1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(1) expected true");
            failed++;
        }

        // Test 12
        if (obj.specialEleven(2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(2) expected false");
            failed++;
        }

        // Test 13
        if (obj.specialEleven(121) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(121) expected true");
            failed++;
        }

        // Test 14
        if (obj.specialEleven(122) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(122) expected true");
            failed++;
        }

        // Test 15
        if (obj.specialEleven(123) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(123) expected false");
            failed++;
        }

        // Test 16
        if (obj.specialEleven(46) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(46) expected false");
            failed++;
        }

        // Test 17
        if (obj.specialEleven(49) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(49) expected false");
            failed++;
        }

        // Test 18
        if (obj.specialEleven(52) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(52) expected false");
            failed++;
        }

        // Test 19
        if (obj.specialEleven(54) == false) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(54) expected false");
            failed++;
        }

        // Test 20
        if (obj.specialEleven(55) == true) {
            passed++;
        } else {
            System.out.println("FAIL: specialEleven(55) expected true");
            failed++;
        }

        System.out.println("specialEleven: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}