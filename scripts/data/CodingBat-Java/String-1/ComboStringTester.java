/**
 * Tester for ComboString - CodingBat Java
 * 11 test cases
 */
public class ComboStringTester {

    public static void main(String[] args) {
        ComboString obj = new ComboString();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.comboString("Hello", "hi").equals("hiHellohi")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"Hello\", \"hi\") expected \"hiHellohi\"");
            failed++;
        }

        // Test 2
        if (obj.comboString("hi", "Hello").equals("hiHellohi")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"hi\", \"Hello\") expected \"hiHellohi\"");
            failed++;
        }

        // Test 3
        if (obj.comboString("aaa", "b").equals("baaab")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"aaa\", \"b\") expected \"baaab\"");
            failed++;
        }

        // Test 4
        if (obj.comboString("b", "aaa").equals("baaab")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"b\", \"aaa\") expected \"baaab\"");
            failed++;
        }

        // Test 5
        if (obj.comboString("aaa", "").equals("aaa")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"aaa\", \"\") expected \"aaa\"");
            failed++;
        }

        // Test 6
        if (obj.comboString("", "bb").equals("bb")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"\", \"bb\") expected \"bb\"");
            failed++;
        }

        // Test 7
        if (obj.comboString("aaa", "1234").equals("aaa1234aaa")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"aaa\", \"1234\") expected \"aaa1234aaa\"");
            failed++;
        }

        // Test 8
        if (obj.comboString("aaa", "bb").equals("bbaaabb")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"aaa\", \"bb\") expected \"bbaaabb\"");
            failed++;
        }

        // Test 9
        if (obj.comboString("a", "bb").equals("abba")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"a\", \"bb\") expected \"abba\"");
            failed++;
        }

        // Test 10
        if (obj.comboString("bb", "a").equals("abba")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"bb\", \"a\") expected \"abba\"");
            failed++;
        }

        // Test 11
        if (obj.comboString("xyz", "ab").equals("abxyzab")) {
            passed++;
        } else {
            System.out.println("FAIL: comboString(\"xyz\", \"ab\") expected \"abxyzab\"");
            failed++;
        }

        System.out.println("comboString: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}