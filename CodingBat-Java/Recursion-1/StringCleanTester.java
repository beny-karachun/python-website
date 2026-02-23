/**
 * Tester for StringClean - CodingBat Java
 * 6 test cases
 */
public class StringCleanTester {

    public static void main(String[] args) {
        StringClean obj = new StringClean();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringClean("yyzzza").equals("yza")) {
            passed++;
        } else {
            System.out.println("FAIL: stringClean(\"yyzzza\") expected \"yza\"");
            failed++;
        }

        // Test 2
        if (obj.stringClean("abbbcdd").equals("abcd")) {
            passed++;
        } else {
            System.out.println("FAIL: stringClean(\"abbbcdd\") expected \"abcd\"");
            failed++;
        }

        // Test 3
        if (obj.stringClean("Hello").equals("Helo")) {
            passed++;
        } else {
            System.out.println("FAIL: stringClean(\"Hello\") expected \"Helo\"");
            failed++;
        }

        // Test 4
        if (obj.stringClean("XXabcYY").equals("XabcY")) {
            passed++;
        } else {
            System.out.println("FAIL: stringClean(\"XXabcYY\") expected \"XabcY\"");
            failed++;
        }

        // Test 5
        if (obj.stringClean("112ab445").equals("12ab45")) {
            passed++;
        } else {
            System.out.println("FAIL: stringClean(\"112ab445\") expected \"12ab45\"");
            failed++;
        }

        // Test 6
        if (obj.stringClean("Hello Bookkeeper").equals("Helo Bokeper")) {
            passed++;
        } else {
            System.out.println("FAIL: stringClean(\"Hello Bookkeeper\") expected \"Helo Bokeper\"");
            failed++;
        }

        System.out.println("stringClean: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}