/**
 * Tester for ExtraEnd - CodingBat Java
 * 5 test cases
 */
public class ExtraEndTester {

    public static void main(String[] args) {
        ExtraEnd obj = new ExtraEnd();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.extraEnd("Hello").equals("lololo")) {
            passed++;
        } else {
            System.out.println("FAIL: extraEnd(\"Hello\") expected \"lololo\"");
            failed++;
        }

        // Test 2
        if (obj.extraEnd("ab").equals("ababab")) {
            passed++;
        } else {
            System.out.println("FAIL: extraEnd(\"ab\") expected \"ababab\"");
            failed++;
        }

        // Test 3
        if (obj.extraEnd("Hi").equals("HiHiHi")) {
            passed++;
        } else {
            System.out.println("FAIL: extraEnd(\"Hi\") expected \"HiHiHi\"");
            failed++;
        }

        // Test 4
        if (obj.extraEnd("Candy").equals("dydydy")) {
            passed++;
        } else {
            System.out.println("FAIL: extraEnd(\"Candy\") expected \"dydydy\"");
            failed++;
        }

        // Test 5
        if (obj.extraEnd("Code").equals("dedede")) {
            passed++;
        } else {
            System.out.println("FAIL: extraEnd(\"Code\") expected \"dedede\"");
            failed++;
        }

        System.out.println("extraEnd: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}