/**
 * Tester for BackAround - CodingBat Java
 * 6 test cases
 */
public class BackAroundTester {

    public static void main(String[] args) {
        BackAround obj = new BackAround();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.backAround("cat").equals("tcatt")) {
            passed++;
        } else {
            System.out.println("FAIL: backAround(\"cat\") expected \"tcatt\"");
            failed++;
        }

        // Test 2
        if (obj.backAround("Hello").equals("oHelloo")) {
            passed++;
        } else {
            System.out.println("FAIL: backAround(\"Hello\") expected \"oHelloo\"");
            failed++;
        }

        // Test 3
        if (obj.backAround("a").equals("aaa")) {
            passed++;
        } else {
            System.out.println("FAIL: backAround(\"a\") expected \"aaa\"");
            failed++;
        }

        // Test 4
        if (obj.backAround("abc").equals("cabcc")) {
            passed++;
        } else {
            System.out.println("FAIL: backAround(\"abc\") expected \"cabcc\"");
            failed++;
        }

        // Test 5
        if (obj.backAround("read").equals("dreadd")) {
            passed++;
        } else {
            System.out.println("FAIL: backAround(\"read\") expected \"dreadd\"");
            failed++;
        }

        // Test 6
        if (obj.backAround("boo").equals("obooo")) {
            passed++;
        } else {
            System.out.println("FAIL: backAround(\"boo\") expected \"obooo\"");
            failed++;
        }

        System.out.println("backAround: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}