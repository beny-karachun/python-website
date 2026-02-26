/**
 * Tester for CountCode - CodingBat Java
 * 14 test cases
 */
public class CountCodeTester {

    public static void main(String[] args) {
        CountCode obj = new CountCode();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countCode("aaacodebbb") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"aaacodebbb\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countCode("codexxcode") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"codexxcode\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countCode("cozexxcope") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"cozexxcope\") expected 2");
            failed++;
        }

        // Test 4
        if (obj.countCode("cozfxxcope") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"cozfxxcope\") expected 1");
            failed++;
        }

        // Test 5
        if (obj.countCode("xxcozeyycop") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"xxcozeyycop\") expected 1");
            failed++;
        }

        // Test 6
        if (obj.countCode("cozcop") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"cozcop\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.countCode("abcxyz") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"abcxyz\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.countCode("code") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"code\") expected 1");
            failed++;
        }

        // Test 9
        if (obj.countCode("ode") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"ode\") expected 0");
            failed++;
        }

        // Test 10
        if (obj.countCode("c") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"c\") expected 0");
            failed++;
        }

        // Test 11
        if (obj.countCode("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"\") expected 0");
            failed++;
        }

        // Test 12
        if (obj.countCode("AAcodeBBcoleCCccoreDD") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"AAcodeBBcoleCCccoreDD\") expected 3");
            failed++;
        }

        // Test 13
        if (obj.countCode("AAcodeBBcoleCCccorfDD") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"AAcodeBBcoleCCccorfDD\") expected 2");
            failed++;
        }

        // Test 14
        if (obj.countCode("coAcodeBcoleccoreDD") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countCode(\"coAcodeBcoleccoreDD\") expected 3");
            failed++;
        }

        System.out.println("countCode: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}