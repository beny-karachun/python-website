/**
 * Tester for Count7 - CodingBat Java
 * 13 test cases
 */
public class Count7Tester {

    public static void main(String[] args) {
        Count7 obj = new Count7();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.count7(717) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count7(717) expected 2");
            failed++;
        }

        // Test 2
        if (obj.count7(7) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count7(7) expected 1");
            failed++;
        }

        // Test 3
        if (obj.count7(123) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count7(123) expected 0");
            failed++;
        }

        // Test 4
        if (obj.count7(77) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count7(77) expected 2");
            failed++;
        }

        // Test 5
        if (obj.count7(7123) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count7(7123) expected 1");
            failed++;
        }

        // Test 6
        if (obj.count7(771237) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: count7(771237) expected 3");
            failed++;
        }

        // Test 7
        if (obj.count7(771737) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: count7(771737) expected 4");
            failed++;
        }

        // Test 8
        if (obj.count7(47571) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count7(47571) expected 2");
            failed++;
        }

        // Test 9
        if (obj.count7(777777) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: count7(777777) expected 6");
            failed++;
        }

        // Test 10
        if (obj.count7(70701277) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: count7(70701277) expected 4");
            failed++;
        }

        // Test 11
        if (obj.count7(777576197) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: count7(777576197) expected 5");
            failed++;
        }

        // Test 12
        if (obj.count7(99999) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count7(99999) expected 0");
            failed++;
        }

        // Test 13
        if (obj.count7(99799) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count7(99799) expected 1");
            failed++;
        }

        System.out.println("count7: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}