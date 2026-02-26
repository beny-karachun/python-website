/**
 * Tester for Front3 - CodingBat Java
 * 7 test cases
 */
public class Front3Tester {

    public static void main(String[] args) {
        Front3 obj = new Front3();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.front3("Java").equals("JavJavJav")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"Java\") expected \"JavJavJav\"");
            failed++;
        }

        // Test 2
        if (obj.front3("Chocolate").equals("ChoChoCho")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"Chocolate\") expected \"ChoChoCho\"");
            failed++;
        }

        // Test 3
        if (obj.front3("abc").equals("abcabcabc")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"abc\") expected \"abcabcabc\"");
            failed++;
        }

        // Test 4
        if (obj.front3("abcXYZ").equals("abcabcabc")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"abcXYZ\") expected \"abcabcabc\"");
            failed++;
        }

        // Test 5
        if (obj.front3("ab").equals("ababab")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"ab\") expected \"ababab\"");
            failed++;
        }

        // Test 6
        if (obj.front3("a").equals("aaa")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"a\") expected \"aaa\"");
            failed++;
        }

        // Test 7
        if (obj.front3("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: front3(\"\") expected \"\"");
            failed++;
        }

        System.out.println("front3: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}