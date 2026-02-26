/**
 * Tester for Triangle - CodingBat Java
 * 8 test cases
 */
public class TriangleTester {

    public static void main(String[] args) {
        Triangle obj = new Triangle();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.triangle(0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(0) expected 0");
            failed++;
        }

        // Test 2
        if (obj.triangle(1) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(1) expected 1");
            failed++;
        }

        // Test 3
        if (obj.triangle(2) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(2) expected 3");
            failed++;
        }

        // Test 4
        if (obj.triangle(3) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(3) expected 6");
            failed++;
        }

        // Test 5
        if (obj.triangle(4) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(4) expected 10");
            failed++;
        }

        // Test 6
        if (obj.triangle(5) == 15) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(5) expected 15");
            failed++;
        }

        // Test 7
        if (obj.triangle(6) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(6) expected 21");
            failed++;
        }

        // Test 8
        if (obj.triangle(7) == 28) {
            passed++;
        } else {
            System.out.println("FAIL: triangle(7) expected 28");
            failed++;
        }

        System.out.println("triangle: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}