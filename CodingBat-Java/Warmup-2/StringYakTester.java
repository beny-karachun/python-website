/**
 * Tester for StringYak - CodingBat Java
 * 7 test cases
 */
public class StringYakTester {

    public static void main(String[] args) {
        StringYak obj = new StringYak();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringYak("yakpak").equals("pak")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"yakpak\") expected \"pak\"");
            failed++;
        }

        // Test 2
        if (obj.stringYak("pakyak").equals("pak")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"pakyak\") expected \"pak\"");
            failed++;
        }

        // Test 3
        if (obj.stringYak("yak123ya").equals("123ya")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"yak123ya\") expected \"123ya\"");
            failed++;
        }

        // Test 4
        if (obj.stringYak("yak").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"yak\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.stringYak("yakxxxyak").equals("xxx")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"yakxxxyak\") expected \"xxx\"");
            failed++;
        }

        // Test 6
        if (obj.stringYak("HiyakHi").equals("HiHi")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"HiyakHi\") expected \"HiHi\"");
            failed++;
        }

        // Test 7
        if (obj.stringYak("xxxyakyyyakzzz").equals("xxxyyzzz")) {
            passed++;
        } else {
            System.out.println("FAIL: stringYak(\"xxxyakyyyakzzz\") expected \"xxxyyzzz\"");
            failed++;
        }

        System.out.println("stringYak: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}