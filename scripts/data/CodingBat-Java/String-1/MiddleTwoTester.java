/**
 * Tester for MiddleTwo - CodingBat Java
 * 5 test cases
 */
public class MiddleTwoTester {

    public static void main(String[] args) {
        MiddleTwo obj = new MiddleTwo();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.middleTwo("string").equals("ri")) {
            passed++;
        } else {
            System.out.println("FAIL: middleTwo(\"string\") expected \"ri\"");
            failed++;
        }

        // Test 2
        if (obj.middleTwo("code").equals("od")) {
            passed++;
        } else {
            System.out.println("FAIL: middleTwo(\"code\") expected \"od\"");
            failed++;
        }

        // Test 3
        if (obj.middleTwo("Practice").equals("ct")) {
            passed++;
        } else {
            System.out.println("FAIL: middleTwo(\"Practice\") expected \"ct\"");
            failed++;
        }

        // Test 4
        if (obj.middleTwo("ab").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: middleTwo(\"ab\") expected \"ab\"");
            failed++;
        }

        // Test 5
        if (obj.middleTwo("0123456789").equals("45")) {
            passed++;
        } else {
            System.out.println("FAIL: middleTwo(\"0123456789\") expected \"45\"");
            failed++;
        }

        System.out.println("middleTwo: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}