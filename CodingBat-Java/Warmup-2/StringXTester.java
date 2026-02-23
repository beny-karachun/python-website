/**
 * Tester for StringX - CodingBat Java
 * 8 test cases
 */
public class StringXTester {

    public static void main(String[] args) {
        StringX obj = new StringX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringX("xxHxix").equals("xHix")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"xxHxix\") expected \"xHix\"");
            failed++;
        }

        // Test 2
        if (obj.stringX("abxxxcd").equals("abcd")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"abxxxcd\") expected \"abcd\"");
            failed++;
        }

        // Test 3
        if (obj.stringX("xabxxxcdx").equals("xabcdx")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"xabxxxcdx\") expected \"xabcdx\"");
            failed++;
        }

        // Test 4
        if (obj.stringX("xKittenx").equals("xKittenx")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"xKittenx\") expected \"xKittenx\"");
            failed++;
        }

        // Test 5
        if (obj.stringX("Hello").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"Hello\") expected \"Hello\"");
            failed++;
        }

        // Test 6
        if (obj.stringX("xx").equals("xx")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"xx\") expected \"xx\"");
            failed++;
        }

        // Test 7
        if (obj.stringX("x").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"x\") expected \"x\"");
            failed++;
        }

        // Test 8
        if (obj.stringX("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: stringX(\"\") expected \"\"");
            failed++;
        }

        System.out.println("stringX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}