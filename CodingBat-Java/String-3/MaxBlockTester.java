/**
 * Tester for MaxBlock - CodingBat Java
 * 11 test cases
 */
public class MaxBlockTester {

    public static void main(String[] args) {
        MaxBlock obj = new MaxBlock();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.maxBlock("hoopla") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"hoopla\") expected 2");
            failed++;
        }

        // Test 2
        if (obj.maxBlock("abbCCCddBBBxx") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"abbCCCddBBBxx\") expected 3");
            failed++;
        }

        // Test 3
        if (obj.maxBlock("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.maxBlock("xyz") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"xyz\") expected 1");
            failed++;
        }

        // Test 5
        if (obj.maxBlock("xxyz") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"xxyz\") expected 2");
            failed++;
        }

        // Test 6
        if (obj.maxBlock("xyzz") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"xyzz\") expected 2");
            failed++;
        }

        // Test 7
        if (obj.maxBlock("abbbcbbbxbbbx") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"abbbcbbbxbbbx\") expected 3");
            failed++;
        }

        // Test 8
        if (obj.maxBlock("XXBBBbbxx") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"XXBBBbbxx\") expected 3");
            failed++;
        }

        // Test 9
        if (obj.maxBlock("XXBBBBbbxx") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"XXBBBBbbxx\") expected 4");
            failed++;
        }

        // Test 10
        if (obj.maxBlock("XXBBBbbxxXXXX") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"XXBBBbbxxXXXX\") expected 4");
            failed++;
        }

        // Test 11
        if (obj.maxBlock("XX2222BBBbbXX2222") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: maxBlock(\"XX2222BBBbbXX2222\") expected 4");
            failed++;
        }

        System.out.println("maxBlock: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}