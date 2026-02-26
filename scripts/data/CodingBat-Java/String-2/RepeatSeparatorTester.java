/**
 * Tester for RepeatSeparator - CodingBat Java
 * 11 test cases
 */
public class RepeatSeparatorTester {

    public static void main(String[] args) {
        RepeatSeparator obj = new RepeatSeparator();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.repeatSeparator("Word", "X", 3).equals("WordXWordXWord")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"Word\", \"X\", 3) expected \"WordXWordXWord\"");
            failed++;
        }

        // Test 2
        if (obj.repeatSeparator("This", "And", 2).equals("ThisAndThis")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"This\", \"And\", 2) expected \"ThisAndThis\"");
            failed++;
        }

        // Test 3
        if (obj.repeatSeparator("This", "And", 1).equals("This")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"This\", \"And\", 1) expected \"This\"");
            failed++;
        }

        // Test 4
        if (obj.repeatSeparator("Hi", "-n-", 2).equals("Hi-n-Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"Hi\", \"-n-\", 2) expected \"Hi-n-Hi\"");
            failed++;
        }

        // Test 5
        if (obj.repeatSeparator("AAA", "", 1).equals("AAA")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"AAA\", \"\", 1) expected \"AAA\"");
            failed++;
        }

        // Test 6
        if (obj.repeatSeparator("AAA", "", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"AAA\", \"\", 0) expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.repeatSeparator("A", "B", 5).equals("ABABABABA")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"A\", \"B\", 5) expected \"ABABABABA\"");
            failed++;
        }

        // Test 8
        if (obj.repeatSeparator("abc", "XX", 3).equals("abcXXabcXXabc")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"abc\", \"XX\", 3) expected \"abcXXabcXXabc\"");
            failed++;
        }

        // Test 9
        if (obj.repeatSeparator("abc", "XX", 2).equals("abcXXabc")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"abc\", \"XX\", 2) expected \"abcXXabc\"");
            failed++;
        }

        // Test 10
        if (obj.repeatSeparator("abc", "XX", 1).equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"abc\", \"XX\", 1) expected \"abc\"");
            failed++;
        }

        // Test 11
        if (obj.repeatSeparator("XYZ", "a", 2).equals("XYZaXYZ")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatSeparator(\"XYZ\", \"a\", 2) expected \"XYZaXYZ\"");
            failed++;
        }

        System.out.println("repeatSeparator: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}