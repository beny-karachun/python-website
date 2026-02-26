/**
 * Tester for NotString - CodingBat Java
 * 7 test cases
 */
public class NotStringTester {

    public static void main(String[] args) {
        NotString obj = new NotString();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.notString("candy").equals("not candy")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"candy\") expected \"not candy\"");
            failed++;
        }

        // Test 2
        if (obj.notString("x").equals("not x")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"x\") expected \"not x\"");
            failed++;
        }

        // Test 3
        if (obj.notString("not bad").equals("not bad")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"not bad\") expected \"not bad\"");
            failed++;
        }

        // Test 4
        if (obj.notString("bad").equals("not bad")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"bad\") expected \"not bad\"");
            failed++;
        }

        // Test 5
        if (obj.notString("not").equals("not")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"not\") expected \"not\"");
            failed++;
        }

        // Test 6
        if (obj.notString("is not").equals("not is not")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"is not\") expected \"not is not\"");
            failed++;
        }

        // Test 7
        if (obj.notString("no").equals("not no")) {
            passed++;
        } else {
            System.out.println("FAIL: notString(\"no\") expected \"not no\"");
            failed++;
        }

        System.out.println("notString: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}