/**
 * Tester for NotReplace - CodingBat Java
 * 11 test cases
 */
public class NotReplaceTester {

    public static void main(String[] args) {
        NotReplace obj = new NotReplace();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.notReplace("is test").equals("is not test")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"is test\") expected \"is not test\"");
            failed++;
        }

        // Test 2
        if (obj.notReplace("is-is").equals("is not-is not")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"is-is\") expected \"is not-is not\"");
            failed++;
        }

        // Test 3
        if (obj.notReplace("This is right").equals("This is not right")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"This is right\") expected \"This is not right\"");
            failed++;
        }

        // Test 4
        if (obj.notReplace("This is isabell").equals("This is not isabell")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"This is isabell\") expected \"This is not isabell\"");
            failed++;
        }

        // Test 5
        if (obj.notReplace("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.notReplace("is").equals("is not")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"is\") expected \"is not\"");
            failed++;
        }

        // Test 7
        if (obj.notReplace("isis").equals("isis")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"isis\") expected \"isis\"");
            failed++;
        }

        // Test 8
        if (obj.notReplace("Dis is bliss is").equals("Dis is not bliss is not")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"Dis is bliss is\") expected \"Dis is not bliss is not\"");
            failed++;
        }

        // Test 9
        if (obj.notReplace("is his").equals("is not his")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"is his\") expected \"is not his\"");
            failed++;
        }

        // Test 10
        if (obj.notReplace("xis yis").equals("xis yis")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"xis yis\") expected \"xis yis\"");
            failed++;
        }

        // Test 11
        if (obj.notReplace("AAAis is").equals("AAAis is not")) {
            passed++;
        } else {
            System.out.println("FAIL: notReplace(\"AAAis is\") expected \"AAAis is not\"");
            failed++;
        }

        System.out.println("notReplace: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}