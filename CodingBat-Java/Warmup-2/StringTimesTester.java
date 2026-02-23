/**
 * Tester for StringTimes - CodingBat Java
 * 10 test cases
 */
public class StringTimesTester {

    public static void main(String[] args) {
        StringTimes obj = new StringTimes();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringTimes("Hi", 2).equals("HiHi")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"Hi\", 2) expected \"HiHi\"");
            failed++;
        }

        // Test 2
        if (obj.stringTimes("Hi", 3).equals("HiHiHi")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"Hi\", 3) expected \"HiHiHi\"");
            failed++;
        }

        // Test 3
        if (obj.stringTimes("Hi", 1).equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"Hi\", 1) expected \"Hi\"");
            failed++;
        }

        // Test 4
        if (obj.stringTimes("Hi", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"Hi\", 0) expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.stringTimes("Hi", 5).equals("HiHiHiHiHi")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"Hi\", 5) expected \"HiHiHiHiHi\"");
            failed++;
        }

        // Test 6
        if (obj.stringTimes("Oh Boy!", 2).equals("Oh Boy!Oh Boy!")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"Oh Boy!\", 2) expected \"Oh Boy!Oh Boy!\"");
            failed++;
        }

        // Test 7
        if (obj.stringTimes("x", 4).equals("xxxx")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"x\", 4) expected \"xxxx\"");
            failed++;
        }

        // Test 8
        if (obj.stringTimes("", 4).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"\", 4) expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.stringTimes("code", 2).equals("codecode")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"code\", 2) expected \"codecode\"");
            failed++;
        }

        // Test 10
        if (obj.stringTimes("code", 3).equals("codecodecode")) {
            passed++;
        } else {
            System.out.println("FAIL: stringTimes(\"code\", 3) expected \"codecodecode\"");
            failed++;
        }

        System.out.println("stringTimes: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}