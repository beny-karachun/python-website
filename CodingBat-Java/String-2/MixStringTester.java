/**
 * Tester for MixString - CodingBat Java
 * 13 test cases
 */
public class MixStringTester {

    public static void main(String[] args) {
        MixString obj = new MixString();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.mixString("abc", "xyz").equals("axbycz")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"abc\", \"xyz\") expected \"axbycz\"");
            failed++;
        }

        // Test 2
        if (obj.mixString("Hi", "There").equals("HTihere")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"Hi\", \"There\") expected \"HTihere\"");
            failed++;
        }

        // Test 3
        if (obj.mixString("xxxx", "There").equals("xTxhxexre")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"xxxx\", \"There\") expected \"xTxhxexre\"");
            failed++;
        }

        // Test 4
        if (obj.mixString("xxx", "X").equals("xXxx")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"xxx\", \"X\") expected \"xXxx\"");
            failed++;
        }

        // Test 5
        if (obj.mixString("2/", "27 around").equals("22/7 around")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"2/\", \"27 around\") expected \"22/7 around\"");
            failed++;
        }

        // Test 6
        if (obj.mixString("", "Hello").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"\", \"Hello\") expected \"Hello\"");
            failed++;
        }

        // Test 7
        if (obj.mixString("Abc", "").equals("Abc")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"Abc\", \"\") expected \"Abc\"");
            failed++;
        }

        // Test 8
        if (obj.mixString("", "").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"\", \"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.mixString("a", "b").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"a\", \"b\") expected \"ab\"");
            failed++;
        }

        // Test 10
        if (obj.mixString("ax", "b").equals("abx")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"ax\", \"b\") expected \"abx\"");
            failed++;
        }

        // Test 11
        if (obj.mixString("a", "bx").equals("abx")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"a\", \"bx\") expected \"abx\"");
            failed++;
        }

        // Test 12
        if (obj.mixString("So", "Long").equals("SLoong")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"So\", \"Long\") expected \"SLoong\"");
            failed++;
        }

        // Test 13
        if (obj.mixString("Long", "So").equals("LSoong")) {
            passed++;
        } else {
            System.out.println("FAIL: mixString(\"Long\", \"So\") expected \"LSoong\"");
            failed++;
        }

        System.out.println("mixString: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}