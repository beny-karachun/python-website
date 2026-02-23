/**
 * Tester for HasBad - CodingBat Java
 * 10 test cases
 */
public class HasBadTester {

    public static void main(String[] args) {
        HasBad obj = new HasBad();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.hasBad("badxx") == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"badxx\") expected true");
            failed++;
        }

        // Test 2
        if (obj.hasBad("xbadxx") == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"xbadxx\") expected true");
            failed++;
        }

        // Test 3
        if (obj.hasBad("xxbadxx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"xxbadxx\") expected false");
            failed++;
        }

        // Test 4
        if (obj.hasBad("code") == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"code\") expected false");
            failed++;
        }

        // Test 5
        if (obj.hasBad("bad") == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"bad\") expected true");
            failed++;
        }

        // Test 6
        if (obj.hasBad("ba") == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"ba\") expected false");
            failed++;
        }

        // Test 7
        if (obj.hasBad("xba") == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"xba\") expected false");
            failed++;
        }

        // Test 8
        if (obj.hasBad("xbad") == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"xbad\") expected true");
            failed++;
        }

        // Test 9
        if (obj.hasBad("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"\") expected false");
            failed++;
        }

        // Test 10
        if (obj.hasBad("badyy") == true) {
            passed++;
        } else {
            System.out.println("FAIL: hasBad(\"badyy\") expected true");
            failed++;
        }

        System.out.println("hasBad: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}