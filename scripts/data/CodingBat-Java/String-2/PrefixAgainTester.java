/**
 * Tester for PrefixAgain - CodingBat Java
 * 12 test cases
 */
public class PrefixAgainTester {

    public static void main(String[] args) {
        PrefixAgain obj = new PrefixAgain();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.prefixAgain("abXYabc", 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"abXYabc\", 1) expected true");
            failed++;
        }

        // Test 2
        if (obj.prefixAgain("abXYabc", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"abXYabc\", 2) expected true");
            failed++;
        }

        // Test 3
        if (obj.prefixAgain("abXYabc", 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"abXYabc\", 3) expected false");
            failed++;
        }

        // Test 4
        if (obj.prefixAgain("xyzxyxyxy", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"xyzxyxyxy\", 2) expected true");
            failed++;
        }

        // Test 5
        if (obj.prefixAgain("xyzxyxyxy", 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"xyzxyxyxy\", 3) expected false");
            failed++;
        }

        // Test 6
        if (obj.prefixAgain("Hi12345Hi6789Hi10", 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"Hi12345Hi6789Hi10\", 1) expected true");
            failed++;
        }

        // Test 7
        if (obj.prefixAgain("Hi12345Hi6789Hi10", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"Hi12345Hi6789Hi10\", 2) expected true");
            failed++;
        }

        // Test 8
        if (obj.prefixAgain("Hi12345Hi6789Hi10", 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"Hi12345Hi6789Hi10\", 3) expected true");
            failed++;
        }

        // Test 9
        if (obj.prefixAgain("Hi12345Hi6789Hi10", 4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"Hi12345Hi6789Hi10\", 4) expected false");
            failed++;
        }

        // Test 10
        if (obj.prefixAgain("a", 1) == false) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"a\", 1) expected false");
            failed++;
        }

        // Test 11
        if (obj.prefixAgain("aa", 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"aa\", 1) expected true");
            failed++;
        }

        // Test 12
        if (obj.prefixAgain("ab", 1) == false) {
            passed++;
        } else {
            System.out.println("FAIL: prefixAgain(\"ab\", 1) expected false");
            failed++;
        }

        System.out.println("prefixAgain: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}