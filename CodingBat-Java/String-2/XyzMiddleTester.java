/**
 * Tester for XyzMiddle - CodingBat Java
 * 21 test cases
 */
public class XyzMiddleTester {

    public static void main(String[] args) {
        XyzMiddle obj = new XyzMiddle();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.xyzMiddle("AAxyzBB") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AAxyzBB\") expected true");
            failed++;
        }

        // Test 2
        if (obj.xyzMiddle("AxyzBB") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AxyzBB\") expected true");
            failed++;
        }

        // Test 3
        if (obj.xyzMiddle("AxyzBBB") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AxyzBBB\") expected false");
            failed++;
        }

        // Test 4
        if (obj.xyzMiddle("AxyzBBBB") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AxyzBBBB\") expected false");
            failed++;
        }

        // Test 5
        if (obj.xyzMiddle("AAAxyzB") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AAAxyzB\") expected false");
            failed++;
        }

        // Test 6
        if (obj.xyzMiddle("AAAxyzBB") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AAAxyzBB\") expected true");
            failed++;
        }

        // Test 7
        if (obj.xyzMiddle("AAAAxyzBB") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AAAAxyzBB\") expected false");
            failed++;
        }

        // Test 8
        if (obj.xyzMiddle("AAAAAxyzBBB") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AAAAAxyzBBB\") expected false");
            failed++;
        }

        // Test 9
        if (obj.xyzMiddle("1x345xyz12x4") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"1x345xyz12x4\") expected true");
            failed++;
        }

        // Test 10
        if (obj.xyzMiddle("xyzAxyzBBB") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzAxyzBBB\") expected true");
            failed++;
        }

        // Test 11
        if (obj.xyzMiddle("xyzAxyzBxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzAxyzBxyz\") expected true");
            failed++;
        }

        // Test 12
        if (obj.xyzMiddle("xyzxyzAxyzBxyzxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzxyzAxyzBxyzxyz\") expected true");
            failed++;
        }

        // Test 13
        if (obj.xyzMiddle("xyzxyzxyzBxyzxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzxyzxyzBxyzxyz\") expected true");
            failed++;
        }

        // Test 14
        if (obj.xyzMiddle("xyzxyzAxyzxyzxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzxyzAxyzxyzxyz\") expected true");
            failed++;
        }

        // Test 15
        if (obj.xyzMiddle("xyzxyzAxyzxyzxy") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzxyzAxyzxyzxy\") expected false");
            failed++;
        }

        // Test 16
        if (obj.xyzMiddle("AxyzxyzBB") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"AxyzxyzBB\") expected false");
            failed++;
        }

        // Test 17
        if (obj.xyzMiddle("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"\") expected false");
            failed++;
        }

        // Test 18
        if (obj.xyzMiddle("x") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"x\") expected false");
            failed++;
        }

        // Test 19
        if (obj.xyzMiddle("xy") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xy\") expected false");
            failed++;
        }

        // Test 20
        if (obj.xyzMiddle("xyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyz\") expected true");
            failed++;
        }

        // Test 21
        if (obj.xyzMiddle("xyzz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyzMiddle(\"xyzz\") expected true");
            failed++;
        }

        System.out.println("xyzMiddle: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}