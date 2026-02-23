/**
 * Tester for NoX - CodingBat Java
 * 6 test cases
 */
public class NoXTester {

    public static void main(String[] args) {
        NoX obj = new NoX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.noX("xaxb").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: noX(\"xaxb\") expected \"ab\"");
            failed++;
        }

        // Test 2
        if (obj.noX("abc").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: noX(\"abc\") expected \"abc\"");
            failed++;
        }

        // Test 3
        if (obj.noX("xx").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: noX(\"xx\") expected \"\"");
            failed++;
        }

        // Test 4
        if (obj.noX("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: noX(\"\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.noX("axxbxx").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: noX(\"axxbxx\") expected \"ab\"");
            failed++;
        }

        // Test 6
        if (obj.noX("Hellox").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: noX(\"Hellox\") expected \"Hello\"");
            failed++;
        }

        System.out.println("noX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}