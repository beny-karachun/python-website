/**
 * Tester for SumDigits - CodingBat Java
 * 11 test cases
 */
public class SumDigitsTester {

    public static void main(String[] args) {
        SumDigits obj = new SumDigits();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sumDigits(126) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(126) expected 9");
            failed++;
        }

        // Test 2
        if (obj.sumDigits(49) == 13) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(49) expected 13");
            failed++;
        }

        // Test 3
        if (obj.sumDigits(12) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(12) expected 3");
            failed++;
        }

        // Test 4
        if (obj.sumDigits(10) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(10) expected 1");
            failed++;
        }

        // Test 5
        if (obj.sumDigits(1) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(1) expected 1");
            failed++;
        }

        // Test 6
        if (obj.sumDigits(0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(0) expected 0");
            failed++;
        }

        // Test 7
        if (obj.sumDigits(730) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(730) expected 10");
            failed++;
        }

        // Test 8
        if (obj.sumDigits(1111) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(1111) expected 4");
            failed++;
        }

        // Test 9
        if (obj.sumDigits(11111) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(11111) expected 5");
            failed++;
        }

        // Test 10
        if (obj.sumDigits(10110) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(10110) expected 3");
            failed++;
        }

        // Test 11
        if (obj.sumDigits(235) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(235) expected 10");
            failed++;
        }

        System.out.println("sumDigits: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}