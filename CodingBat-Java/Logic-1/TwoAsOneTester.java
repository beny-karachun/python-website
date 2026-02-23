/**
 * Tester for TwoAsOne - CodingBat Java
 * 12 test cases
 */
public class TwoAsOneTester {

    public static void main(String[] args) {
        TwoAsOne obj = new TwoAsOne();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.twoAsOne(1, 2, 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(1, 2, 3) expected true");
            failed++;
        }

        // Test 2
        if (obj.twoAsOne(3, 1, 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(3, 1, 2) expected true");
            failed++;
        }

        // Test 3
        if (obj.twoAsOne(3, 2, 2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(3, 2, 2) expected false");
            failed++;
        }

        // Test 4
        if (obj.twoAsOne(2, 3, 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(2, 3, 1) expected true");
            failed++;
        }

        // Test 5
        if (obj.twoAsOne(5, 3, -2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(5, 3, -2) expected true");
            failed++;
        }

        // Test 6
        if (obj.twoAsOne(5, 3, -3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(5, 3, -3) expected false");
            failed++;
        }

        // Test 7
        if (obj.twoAsOne(2, 5, 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(2, 5, 3) expected true");
            failed++;
        }

        // Test 8
        if (obj.twoAsOne(9, 5, 5) == false) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(9, 5, 5) expected false");
            failed++;
        }

        // Test 9
        if (obj.twoAsOne(9, 4, 5) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(9, 4, 5) expected true");
            failed++;
        }

        // Test 10
        if (obj.twoAsOne(5, 4, 9) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(5, 4, 9) expected true");
            failed++;
        }

        // Test 11
        if (obj.twoAsOne(3, 3, 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(3, 3, 0) expected true");
            failed++;
        }

        // Test 12
        if (obj.twoAsOne(3, 3, 2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: twoAsOne(3, 3, 2) expected false");
            failed++;
        }

        System.out.println("twoAsOne: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}