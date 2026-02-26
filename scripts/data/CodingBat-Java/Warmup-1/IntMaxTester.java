/**
 * Tester for IntMax - CodingBat Java
 * 11 test cases
 */
public class IntMaxTester {

    public static void main(String[] args) {
        IntMax obj = new IntMax();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.intMax(1, 2, 3) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(1, 2, 3) expected 3");
            failed++;
        }

        // Test 2
        if (obj.intMax(1, 3, 2) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(1, 3, 2) expected 3");
            failed++;
        }

        // Test 3
        if (obj.intMax(3, 2, 1) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(3, 2, 1) expected 3");
            failed++;
        }

        // Test 4
        if (obj.intMax(9, 3, 3) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(9, 3, 3) expected 9");
            failed++;
        }

        // Test 5
        if (obj.intMax(3, 9, 3) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(3, 9, 3) expected 9");
            failed++;
        }

        // Test 6
        if (obj.intMax(3, 3, 9) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(3, 3, 9) expected 9");
            failed++;
        }

        // Test 7
        if (obj.intMax(8, 2, 3) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(8, 2, 3) expected 8");
            failed++;
        }

        // Test 8
        if (obj.intMax(-3, -1, -2) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(-3, -1, -2) expected -1");
            failed++;
        }

        // Test 9
        if (obj.intMax(6, 2, 5) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(6, 2, 5) expected 6");
            failed++;
        }

        // Test 10
        if (obj.intMax(5, 6, 2) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(5, 6, 2) expected 6");
            failed++;
        }

        // Test 11
        if (obj.intMax(5, 2, 6) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: intMax(5, 2, 6) expected 6");
            failed++;
        }

        System.out.println("intMax: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}