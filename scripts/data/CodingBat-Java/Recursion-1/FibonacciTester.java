/**
 * Tester for Fibonacci - CodingBat Java
 * 8 test cases
 */
public class FibonacciTester {

    public static void main(String[] args) {
        Fibonacci obj = new Fibonacci();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.fibonacci(0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(0) expected 0");
            failed++;
        }

        // Test 2
        if (obj.fibonacci(1) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(1) expected 1");
            failed++;
        }

        // Test 3
        if (obj.fibonacci(2) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(2) expected 1");
            failed++;
        }

        // Test 4
        if (obj.fibonacci(3) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(3) expected 2");
            failed++;
        }

        // Test 5
        if (obj.fibonacci(4) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(4) expected 3");
            failed++;
        }

        // Test 6
        if (obj.fibonacci(5) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(5) expected 5");
            failed++;
        }

        // Test 7
        if (obj.fibonacci(6) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(6) expected 8");
            failed++;
        }

        // Test 8
        if (obj.fibonacci(7) == 13) {
            passed++;
        } else {
            System.out.println("FAIL: fibonacci(7) expected 13");
            failed++;
        }

        System.out.println("fibonacci: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}