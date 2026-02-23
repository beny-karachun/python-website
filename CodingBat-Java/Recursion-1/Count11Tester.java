/**
 * Tester for Count11 - CodingBat Java
 * 11 test cases
 */
public class Count11Tester {

    public static void main(String[] args) {
        Count11 obj = new Count11();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.count11("11abc11") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"11abc11\") expected 2");
            failed++;
        }

        // Test 2
        if (obj.count11("abc11x11x11") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"abc11x11x11\") expected 3");
            failed++;
        }

        // Test 3
        if (obj.count11("111") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"111\") expected 1");
            failed++;
        }

        // Test 4
        if (obj.count11("1111") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"1111\") expected 2");
            failed++;
        }

        // Test 5
        if (obj.count11("1") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"1\") expected 0");
            failed++;
        }

        // Test 6
        if (obj.count11("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.count11("hi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"hi\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.count11("11x111x1111") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"11x111x1111\") expected 4");
            failed++;
        }

        // Test 9
        if (obj.count11("1x111") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"1x111\") expected 1");
            failed++;
        }

        // Test 10
        if (obj.count11("1Hello1") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"1Hello1\") expected 0");
            failed++;
        }

        // Test 11
        if (obj.count11("Hello") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count11(\"Hello\") expected 0");
            failed++;
        }

        System.out.println("count11: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}