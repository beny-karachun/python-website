/**
 * Tester for EqualIsNot - CodingBat Java
 * 10 test cases
 */
public class EqualIsNotTester {

    public static void main(String[] args) {
        EqualIsNot obj = new EqualIsNot();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.equalIsNot("This is not") == false) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"This is not\") expected false");
            failed++;
        }

        // Test 2
        if (obj.equalIsNot("This is notnot") == true) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"This is notnot\") expected true");
            failed++;
        }

        // Test 3
        if (obj.equalIsNot("noisxxnotyynotxisi") == true) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"noisxxnotyynotxisi\") expected true");
            failed++;
        }

        // Test 4
        if (obj.equalIsNot("noisxxnotyynotxsi") == false) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"noisxxnotyynotxsi\") expected false");
            failed++;
        }

        // Test 5
        if (obj.equalIsNot("xxxyyyzzzintint") == true) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"xxxyyyzzzintint\") expected true");
            failed++;
        }

        // Test 6
        if (obj.equalIsNot("") == true) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"\") expected true");
            failed++;
        }

        // Test 7
        if (obj.equalIsNot("isisnotnot") == true) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"isisnotnot\") expected true");
            failed++;
        }

        // Test 8
        if (obj.equalIsNot("isisnotno7Not") == false) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"isisnotno7Not\") expected false");
            failed++;
        }

        // Test 9
        if (obj.equalIsNot("isnotis") == false) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"isnotis\") expected false");
            failed++;
        }

        // Test 10
        if (obj.equalIsNot("mis3notpotbotis") == false) {
            passed++;
        } else {
            System.out.println("FAIL: equalIsNot(\"mis3notpotbotis\") expected false");
            failed++;
        }

        System.out.println("equalIsNot: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}