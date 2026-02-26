/**
 * Tester for WithouEnd2 - CodingBat Java
 * 7 test cases
 */
public class WithouEnd2Tester {

    public static void main(String[] args) {
        WithouEnd2 obj = new WithouEnd2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.withouEnd2("Hello").equals("ell")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"Hello\") expected \"ell\"");
            failed++;
        }

        // Test 2
        if (obj.withouEnd2("abc").equals("b")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"abc\") expected \"b\"");
            failed++;
        }

        // Test 3
        if (obj.withouEnd2("ab").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"ab\") expected \"\"");
            failed++;
        }

        // Test 4
        if (obj.withouEnd2("a").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"a\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.withouEnd2("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.withouEnd2("coldy").equals("old")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"coldy\") expected \"old\"");
            failed++;
        }

        // Test 7
        if (obj.withouEnd2("java code").equals("ava cod")) {
            passed++;
        } else {
            System.out.println("FAIL: withouEnd2(\"java code\") expected \"ava cod\"");
            failed++;
        }

        System.out.println("withouEnd2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}