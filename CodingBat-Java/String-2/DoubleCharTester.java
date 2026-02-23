/**
 * Tester for DoubleChar - CodingBat Java
 * 9 test cases
 */
public class DoubleCharTester {

    public static void main(String[] args) {
        DoubleChar obj = new DoubleChar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.doubleChar("The").equals("TThhee")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"The\") expected \"TThhee\"");
            failed++;
        }

        // Test 2
        if (obj.doubleChar("AAbb").equals("AAAAbbbb")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"AAbb\") expected \"AAAAbbbb\"");
            failed++;
        }

        // Test 3
        if (obj.doubleChar("Hi-There").equals("HHii--TThheerree")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"Hi-There\") expected \"HHii--TThheerree\"");
            failed++;
        }

        // Test 4
        if (obj.doubleChar("Word!").equals("WWoorrdd!!")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"Word!\") expected \"WWoorrdd!!\"");
            failed++;
        }

        // Test 5
        if (obj.doubleChar("!!").equals("!!!!")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"!!\") expected \"!!!!\"");
            failed++;
        }

        // Test 6
        if (obj.doubleChar("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.doubleChar("a").equals("aa")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"a\") expected \"aa\"");
            failed++;
        }

        // Test 8
        if (obj.doubleChar(".").equals("..")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\".\") expected \"..\"");
            failed++;
        }

        // Test 9
        if (obj.doubleChar("aa").equals("aaaa")) {
            passed++;
        } else {
            System.out.println("FAIL: doubleChar(\"aa\") expected \"aaaa\"");
            failed++;
        }

        System.out.println("doubleChar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}