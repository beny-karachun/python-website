/**
 * Tester for RepeatEnd - CodingBat Java
 * 8 test cases
 */
public class RepeatEndTester {

    public static void main(String[] args) {
        RepeatEnd obj = new RepeatEnd();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.repeatEnd("Hello", 3).equals("llollollo")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"Hello\", 3) expected \"llollollo\"");
            failed++;
        }

        // Test 2
        if (obj.repeatEnd("Hello", 2).equals("lolo")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"Hello\", 2) expected \"lolo\"");
            failed++;
        }

        // Test 3
        if (obj.repeatEnd("Hello", 1).equals("o")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"Hello\", 1) expected \"o\"");
            failed++;
        }

        // Test 4
        if (obj.repeatEnd("Hello", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"Hello\", 0) expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.repeatEnd("abc", 3).equals("abcabcabc")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"abc\", 3) expected \"abcabcabc\"");
            failed++;
        }

        // Test 6
        if (obj.repeatEnd("1234", 2).equals("3434")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"1234\", 2) expected \"3434\"");
            failed++;
        }

        // Test 7
        if (obj.repeatEnd("1234", 3).equals("234234234")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"1234\", 3) expected \"234234234\"");
            failed++;
        }

        // Test 8
        if (obj.repeatEnd("", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatEnd(\"\", 0) expected \"\"");
            failed++;
        }

        System.out.println("repeatEnd: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}