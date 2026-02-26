/**
 * Tester for Factorial - CodingBat Java
 * 9 test cases
 */
public class FactorialTester {

    public static void main(String[] args) {
        Factorial obj = new Factorial();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.factorial(1) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(1) expected 1");
            failed++;
        }

        // Test 2
        if (obj.factorial(2) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(2) expected 2");
            failed++;
        }

        // Test 3
        if (obj.factorial(3) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(3) expected 6");
            failed++;
        }

        // Test 4
        if (obj.factorial(4) == 24) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(4) expected 24");
            failed++;
        }

        // Test 5
        if (obj.factorial(5) == 120) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(5) expected 120");
            failed++;
        }

        // Test 6
        if (obj.factorial(6) == 720) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(6) expected 720");
            failed++;
        }

        // Test 7
        if (obj.factorial(7) == 5040) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(7) expected 5040");
            failed++;
        }

        // Test 8
        if (obj.factorial(8) == 40320) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(8) expected 40320");
            failed++;
        }

        // Test 9
        if (obj.factorial(12) == 479001600) {
            passed++;
        } else {
            System.out.println("FAIL: factorial(12) expected 479001600");
            failed++;
        }

        System.out.println("factorial: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}