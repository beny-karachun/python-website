/**
 * Tester for XyzThere - CodingBat Java
 * 14 test cases
 */
public class XyzThereTester {

    public static void main(String[] args) {
        XyzThere obj = new XyzThere();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.xyzThere("abcxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"abcxyz\") expected true");
            failed++;
        }

        // Test 2
        if (obj.xyzThere("abc.xyz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"abc.xyz\") expected false");
            failed++;
        }

        // Test 3
        if (obj.xyzThere("xyz.abc") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"xyz.abc\") expected true");
            failed++;
        }

        // Test 4
        if (obj.xyzThere("abcxy") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"abcxy\") expected false");
            failed++;
        }

        // Test 5
        if (obj.xyzThere("xyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"xyz\") expected true");
            failed++;
        }

        // Test 6
        if (obj.xyzThere("xy") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"xy\") expected false");
            failed++;
        }

        // Test 7
        if (obj.xyzThere("x") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"x\") expected false");
            failed++;
        }

        // Test 8
        if (obj.xyzThere("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"\") expected false");
            failed++;
        }

        // Test 9
        if (obj.xyzThere("abc.xyzxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"abc.xyzxyz\") expected true");
            failed++;
        }

        // Test 10
        if (obj.xyzThere("abc.xxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"abc.xxyz\") expected true");
            failed++;
        }

        // Test 11
        if (obj.xyzThere(".xyz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\".xyz\") expected false");
            failed++;
        }

        // Test 12
        if (obj.xyzThere("12.xyz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"12.xyz\") expected false");
            failed++;
        }

        // Test 13
        if (obj.xyzThere("12xyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"12xyz\") expected true");
            failed++;
        }

        // Test 14
        if (obj.xyzThere("1.xyz.xyz2.xyz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzThere(\"1.xyz.xyz2.xyz\") expected false");
            failed++;
        }

        System.out.println("xyzThere: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}