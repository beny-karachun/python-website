/**
 * Tester for SumLimit - CodingBat Java
 * 15 test cases
 */
public class SumLimitTester {

    public static void main(String[] args) {
        SumLimit obj = new SumLimit();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sumLimit(2, 3) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(2, 3) expected 5");
            failed++;
        }

        // Test 2
        if (obj.sumLimit(8, 3) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(8, 3) expected 8");
            failed++;
        }

        // Test 3
        if (obj.sumLimit(8, 1) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(8, 1) expected 9");
            failed++;
        }

        // Test 4
        if (obj.sumLimit(11, 39) == 50) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(11, 39) expected 50");
            failed++;
        }

        // Test 5
        if (obj.sumLimit(11, 99) == 11) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(11, 99) expected 11");
            failed++;
        }

        // Test 6
        if (obj.sumLimit(0, 0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(0, 0) expected 0");
            failed++;
        }

        // Test 7
        if (obj.sumLimit(99, 0) == 99) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(99, 0) expected 99");
            failed++;
        }

        // Test 8
        if (obj.sumLimit(99, 1) == 99) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(99, 1) expected 99");
            failed++;
        }

        // Test 9
        if (obj.sumLimit(123, 1) == 124) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(123, 1) expected 124");
            failed++;
        }

        // Test 10
        if (obj.sumLimit(1, 123) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(1, 123) expected 1");
            failed++;
        }

        // Test 11
        if (obj.sumLimit(23, 60) == 83) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(23, 60) expected 83");
            failed++;
        }

        // Test 12
        if (obj.sumLimit(23, 80) == 23) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(23, 80) expected 23");
            failed++;
        }

        // Test 13
        if (obj.sumLimit(9000, 1) == 9001) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(9000, 1) expected 9001");
            failed++;
        }

        // Test 14
        if (obj.sumLimit(90000000, 1) == 90000001) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(90000000, 1) expected 90000001");
            failed++;
        }

        // Test 15
        if (obj.sumLimit(9000, 1000) == 9000) {
            passed++;
        } else {
            System.out.println("FAIL: sumLimit(9000, 1000) expected 9000");
            failed++;
        }

        System.out.println("sumLimit: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}