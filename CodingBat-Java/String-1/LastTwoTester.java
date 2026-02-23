/**
 * Tester for LastTwo - CodingBat Java
 * 5 test cases
 */
public class LastTwoTester {

    public static void main(String[] args) {
        LastTwo obj = new LastTwo();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.lastTwo("coding").equals("codign")) {
            passed++;
        } else {
            System.out.println("FAIL: lastTwo(\"coding\") expected \"codign\"");
            failed++;
        }

        // Test 2
        if (obj.lastTwo("cat").equals("cta")) {
            passed++;
        } else {
            System.out.println("FAIL: lastTwo(\"cat\") expected \"cta\"");
            failed++;
        }

        // Test 3
        if (obj.lastTwo("ab").equals("ba")) {
            passed++;
        } else {
            System.out.println("FAIL: lastTwo(\"ab\") expected \"ba\"");
            failed++;
        }

        // Test 4
        if (obj.lastTwo("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: lastTwo(\"a\") expected \"a\"");
            failed++;
        }

        // Test 5
        if (obj.lastTwo("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: lastTwo(\"\") expected \"\"");
            failed++;
        }

        System.out.println("lastTwo: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}