/**
 * Tester for Max1020 - CodingBat Java
 * 11 test cases
 */
public class Max1020Tester {

    public static void main(String[] args) {
        Max1020 obj = new Max1020();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.max1020(11, 19) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(11, 19) expected 19");
            failed++;
        }

        // Test 2
        if (obj.max1020(19, 11) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(19, 11) expected 19");
            failed++;
        }

        // Test 3
        if (obj.max1020(11, 9) == 11) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(11, 9) expected 11");
            failed++;
        }

        // Test 4
        if (obj.max1020(9, 21) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(9, 21) expected 0");
            failed++;
        }

        // Test 5
        if (obj.max1020(10, 21) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(10, 21) expected 10");
            failed++;
        }

        // Test 6
        if (obj.max1020(21, 10) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(21, 10) expected 10");
            failed++;
        }

        // Test 7
        if (obj.max1020(9, 11) == 11) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(9, 11) expected 11");
            failed++;
        }

        // Test 8
        if (obj.max1020(23, 10) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(23, 10) expected 10");
            failed++;
        }

        // Test 9
        if (obj.max1020(20, 10) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(20, 10) expected 20");
            failed++;
        }

        // Test 10
        if (obj.max1020(7, 20) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(7, 20) expected 20");
            failed++;
        }

        // Test 11
        if (obj.max1020(17, 16) == 17) {
            passed++;
        } else {
            System.out.println("FAIL: max1020(17, 16) expected 17");
            failed++;
        }

        System.out.println("max1020: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}