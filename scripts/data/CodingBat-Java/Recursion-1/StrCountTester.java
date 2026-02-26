/**
 * Tester for StrCount - CodingBat Java
 * 14 test cases
 */
public class StrCountTester {

    public static void main(String[] args) {
        StrCount obj = new StrCount();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.strCount("catcowcat", "cat") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"catcowcat\", \"cat\") expected 2");
            failed++;
        }

        // Test 2
        if (obj.strCount("catcowcat", "cow") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"catcowcat\", \"cow\") expected 1");
            failed++;
        }

        // Test 3
        if (obj.strCount("catcowcat", "dog") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"catcowcat\", \"dog\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.strCount("cacatcowcat", "cat") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"cacatcowcat\", \"cat\") expected 2");
            failed++;
        }

        // Test 5
        if (obj.strCount("xyx", "x") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"xyx\", \"x\") expected 2");
            failed++;
        }

        // Test 6
        if (obj.strCount("iiiijj", "i") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"iiiijj\", \"i\") expected 4");
            failed++;
        }

        // Test 7
        if (obj.strCount("iiiijj", "ii") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"iiiijj\", \"ii\") expected 2");
            failed++;
        }

        // Test 8
        if (obj.strCount("iiiijj", "iii") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"iiiijj\", \"iii\") expected 1");
            failed++;
        }

        // Test 9
        if (obj.strCount("iiiijj", "j") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"iiiijj\", \"j\") expected 2");
            failed++;
        }

        // Test 10
        if (obj.strCount("iiiijj", "jj") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"iiiijj\", \"jj\") expected 1");
            failed++;
        }

        // Test 11
        if (obj.strCount("aaabababab", "ab") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"aaabababab\", \"ab\") expected 4");
            failed++;
        }

        // Test 12
        if (obj.strCount("aaabababab", "aa") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"aaabababab\", \"aa\") expected 1");
            failed++;
        }

        // Test 13
        if (obj.strCount("aaabababab", "a") == 6) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"aaabababab\", \"a\") expected 6");
            failed++;
        }

        // Test 14
        if (obj.strCount("aaabababab", "b") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: strCount(\"aaabababab\", \"b\") expected 4");
            failed++;
        }

        System.out.println("strCount: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}