/**
 * Tester for StringMatch - CodingBat Java
 * 10 test cases
 */
public class StringMatchTester {

    public static void main(String[] args) {
        StringMatch obj = new StringMatch();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringMatch("xxcaazz", "xxbaaz") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"xxcaazz\", \"xxbaaz\") expected 3");
            failed++;
        }

        // Test 2
        if (obj.stringMatch("abc", "abc") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"abc\", \"abc\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.stringMatch("abc", "axc") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"abc\", \"axc\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.stringMatch("hello", "he") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"hello\", \"he\") expected 1");
            failed++;
        }

        // Test 5
        if (obj.stringMatch("he", "hello") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"he\", \"hello\") expected 1");
            failed++;
        }

        // Test 6
        if (obj.stringMatch("h", "hello") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"h\", \"hello\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.stringMatch("", "hello") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"\", \"hello\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.stringMatch("aabbccdd", "abbbxxd") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"aabbccdd\", \"abbbxxd\") expected 1");
            failed++;
        }

        // Test 9
        if (obj.stringMatch("aaxxaaxx", "iaxxai") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"aaxxaaxx\", \"iaxxai\") expected 3");
            failed++;
        }

        // Test 10
        if (obj.stringMatch("iaxxai", "aaxxaaxx") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: stringMatch(\"iaxxai\", \"aaxxaaxx\") expected 3");
            failed++;
        }

        System.out.println("stringMatch: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}