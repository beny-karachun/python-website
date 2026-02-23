/**
 * Tester for MinCat - CodingBat Java
 * 6 test cases
 */
public class MinCatTester {

    public static void main(String[] args) {
        MinCat obj = new MinCat();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.minCat("Hello", "Hi").equals("loHi")) {
            passed++;
        } else {
            System.out.println("FAIL: minCat(\"Hello\", \"Hi\") expected \"loHi\"");
            failed++;
        }

        // Test 2
        if (obj.minCat("Hello", "java").equals("ellojava")) {
            passed++;
        } else {
            System.out.println("FAIL: minCat(\"Hello\", \"java\") expected \"ellojava\"");
            failed++;
        }

        // Test 3
        if (obj.minCat("java", "Hello").equals("javaello")) {
            passed++;
        } else {
            System.out.println("FAIL: minCat(\"java\", \"Hello\") expected \"javaello\"");
            failed++;
        }

        // Test 4
        if (obj.minCat("abc", "x").equals("cx")) {
            passed++;
        } else {
            System.out.println("FAIL: minCat(\"abc\", \"x\") expected \"cx\"");
            failed++;
        }

        // Test 5
        if (obj.minCat("x", "abc").equals("xc")) {
            passed++;
        } else {
            System.out.println("FAIL: minCat(\"x\", \"abc\") expected \"xc\"");
            failed++;
        }

        // Test 6
        if (obj.minCat("abc", "").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: minCat(\"abc\", \"\") expected \"\"");
            failed++;
        }

        System.out.println("minCat: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}