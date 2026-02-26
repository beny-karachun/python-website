/**
 * Tester for Without2 - CodingBat Java
 * 9 test cases
 */
public class Without2Tester {

    public static void main(String[] args) {
        Without2 obj = new Without2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.without2("HelloHe").equals("lloHe")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"HelloHe\") expected \"lloHe\"");
            failed++;
        }

        // Test 2
        if (obj.without2("HelloHi").equals("HelloHi")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"HelloHi\") expected \"HelloHi\"");
            failed++;
        }

        // Test 3
        if (obj.without2("Hi").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"Hi\") expected \"\"");
            failed++;
        }

        // Test 4
        if (obj.without2("Chocolate").equals("Chocolate")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"Chocolate\") expected \"Chocolate\"");
            failed++;
        }

        // Test 5
        if (obj.without2("xxx").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"xxx\") expected \"x\"");
            failed++;
        }

        // Test 6
        if (obj.without2("xx").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"xx\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.without2("x").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"x\") expected \"x\"");
            failed++;
        }

        // Test 8
        if (obj.without2("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.without2("Fruits").equals("Fruits")) {
            passed++;
        } else {
            System.out.println("FAIL: without2(\"Fruits\") expected \"Fruits\"");
            failed++;
        }

        System.out.println("without2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}