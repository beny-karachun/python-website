/**
 * Tester for NonStart - CodingBat Java
 * 9 test cases
 */
public class NonStartTester {

    public static void main(String[] args) {
        NonStart obj = new NonStart();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.nonStart("Hello", "There").equals("ellohere")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"Hello\", \"There\") expected \"ellohere\"");
            failed++;
        }

        // Test 2
        if (obj.nonStart("java", "code").equals("avaode")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"java\", \"code\") expected \"avaode\"");
            failed++;
        }

        // Test 3
        if (obj.nonStart("shotl", "java").equals("hotlava")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"shotl\", \"java\") expected \"hotlava\"");
            failed++;
        }

        // Test 4
        if (obj.nonStart("ab", "xy").equals("by")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"ab\", \"xy\") expected \"by\"");
            failed++;
        }

        // Test 5
        if (obj.nonStart("ab", "x").equals("b")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"ab\", \"x\") expected \"b\"");
            failed++;
        }

        // Test 6
        if (obj.nonStart("x", "ac").equals("c")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"x\", \"ac\") expected \"c\"");
            failed++;
        }

        // Test 7
        if (obj.nonStart("a", "x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"a\", \"x\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.nonStart("kit", "kat").equals("itat")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"kit\", \"kat\") expected \"itat\"");
            failed++;
        }

        // Test 9
        if (obj.nonStart("mart", "dart").equals("artart")) {
            passed++;
        } else {
            System.out.println("FAIL: nonStart(\"mart\", \"dart\") expected \"artart\"");
            failed++;
        }

        System.out.println("nonStart: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}