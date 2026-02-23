/**
 * Tester for SameStarChar - CodingBat Java
 * 16 test cases
 */
public class SameStarCharTester {

    public static void main(String[] args) {
        SameStarChar obj = new SameStarChar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sameStarChar("xy*yzz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"xy*yzz\") expected true");
            failed++;
        }

        // Test 2
        if (obj.sameStarChar("xy*zzz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"xy*zzz\") expected false");
            failed++;
        }

        // Test 3
        if (obj.sameStarChar("*xa*az") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*xa*az\") expected true");
            failed++;
        }

        // Test 4
        if (obj.sameStarChar("*xa*bz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*xa*bz\") expected false");
            failed++;
        }

        // Test 5
        if (obj.sameStarChar("*xa*a*") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*xa*a*\") expected true");
            failed++;
        }

        // Test 6
        if (obj.sameStarChar("") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"\") expected true");
            failed++;
        }

        // Test 7
        if (obj.sameStarChar("*xa*a*a") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*xa*a*a\") expected true");
            failed++;
        }

        // Test 8
        if (obj.sameStarChar("*xa*a*b") == false) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*xa*a*b\") expected false");
            failed++;
        }

        // Test 9
        if (obj.sameStarChar("*12*2*2") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*12*2*2\") expected true");
            failed++;
        }

        // Test 10
        if (obj.sameStarChar("12*2*3*") == false) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"12*2*3*\") expected false");
            failed++;
        }

        // Test 11
        if (obj.sameStarChar("abcDEF") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"abcDEF\") expected true");
            failed++;
        }

        // Test 12
        if (obj.sameStarChar("XY*YYYY*Z*") == false) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"XY*YYYY*Z*\") expected false");
            failed++;
        }

        // Test 13
        if (obj.sameStarChar("XY*YYYY*Y*") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"XY*YYYY*Y*\") expected true");
            failed++;
        }

        // Test 14
        if (obj.sameStarChar("12*2*3*") == false) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"12*2*3*\") expected false");
            failed++;
        }

        // Test 15
        if (obj.sameStarChar("*") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"*\") expected true");
            failed++;
        }

        // Test 16
        if (obj.sameStarChar("**") == true) {
            passed++;
        } else {
            System.out.println("FAIL: sameStarChar(\"**\") expected true");
            failed++;
        }

        System.out.println("sameStarChar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}