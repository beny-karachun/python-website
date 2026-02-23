/**
 * Tester for DeFront - CodingBat Java
 * 19 test cases
 */
public class DeFrontTester {

    public static void main(String[] args) {
        DeFront obj = new DeFront();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.deFront("Hello").equals("llo")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"Hello\") expected \"llo\"");
            failed++;
        }

        // Test 2
        if (obj.deFront("java").equals("va")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"java\") expected \"va\"");
            failed++;
        }

        // Test 3
        if (obj.deFront("away").equals("aay")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"away\") expected \"aay\"");
            failed++;
        }

        // Test 4
        if (obj.deFront("axy").equals("ay")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"axy\") expected \"ay\"");
            failed++;
        }

        // Test 5
        if (obj.deFront("abc").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"abc\") expected \"abc\"");
            failed++;
        }

        // Test 6
        if (obj.deFront("xby").equals("by")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"xby\") expected \"by\"");
            failed++;
        }

        // Test 7
        if (obj.deFront("ab").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"ab\") expected \"ab\"");
            failed++;
        }

        // Test 8
        if (obj.deFront("ax").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"ax\") expected \"a\"");
            failed++;
        }

        // Test 9
        if (obj.deFront("axb").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"axb\") expected \"ab\"");
            failed++;
        }

        // Test 10
        if (obj.deFront("aaa").equals("aa")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"aaa\") expected \"aa\"");
            failed++;
        }

        // Test 11
        if (obj.deFront("xbc").equals("bc")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"xbc\") expected \"bc\"");
            failed++;
        }

        // Test 12
        if (obj.deFront("bbb").equals("bb")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"bbb\") expected \"bb\"");
            failed++;
        }

        // Test 13
        if (obj.deFront("bazz").equals("zz")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"bazz\") expected \"zz\"");
            failed++;
        }

        // Test 14
        if (obj.deFront("ba").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"ba\") expected \"\"");
            failed++;
        }

        // Test 15
        if (obj.deFront("abxyz").equals("abxyz")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"abxyz\") expected \"abxyz\"");
            failed++;
        }

        // Test 16
        if (obj.deFront("hi").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"hi\") expected \"\"");
            failed++;
        }

        // Test 17
        if (obj.deFront("his").equals("s")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"his\") expected \"s\"");
            failed++;
        }

        // Test 18
        if (obj.deFront("xz").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"xz\") expected \"\"");
            failed++;
        }

        // Test 19
        if (obj.deFront("zzz").equals("z")) {
            passed++;
        } else {
            System.out.println("FAIL: deFront(\"zzz\") expected \"z\"");
            failed++;
        }

        System.out.println("deFront: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}