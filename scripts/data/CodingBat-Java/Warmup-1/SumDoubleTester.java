/**
 * Tester for SumDouble - CodingBat Java
 * 8 test cases
 */
public class SumDoubleTester {

    public static void main(String[] args) {
        SumDouble obj = new SumDouble();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sumDouble(1, 2) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(1, 2) expected 3");
            failed++;
        }

        // Test 2
        if (obj.sumDouble(3, 2) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(3, 2) expected 5");
            failed++;
        }

        // Test 3
        if (obj.sumDouble(2, 2) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(2, 2) expected 8");
            failed++;
        }

        // Test 4
        if (obj.sumDouble(-1, 0) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(-1, 0) expected -1");
            failed++;
        }

        // Test 5
        if (obj.sumDouble(3, 3) == 12) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(3, 3) expected 12");
            failed++;
        }

        // Test 6
        if (obj.sumDouble(0, 0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(0, 0) expected 0");
            failed++;
        }

        // Test 7
        if (obj.sumDouble(0, 1) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(0, 1) expected 1");
            failed++;
        }

        // Test 8
        if (obj.sumDouble(3, 4) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: sumDouble(3, 4) expected 7");
            failed++;
        }

        System.out.println("sumDouble: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}