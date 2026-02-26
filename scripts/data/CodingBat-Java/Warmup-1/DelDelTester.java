/**
 * Tester for DelDel - CodingBat Java
 * 11 test cases
 */
public class DelDelTester {

    public static void main(String[] args) {
        DelDel obj = new DelDel();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.delDel("adelbc").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"adelbc\") expected \"abc\"");
            failed++;
        }

        // Test 2
        if (obj.delDel("adelHello").equals("aHello")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"adelHello\") expected \"aHello\"");
            failed++;
        }

        // Test 3
        if (obj.delDel("adedbc").equals("adedbc")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"adedbc\") expected \"adedbc\"");
            failed++;
        }

        // Test 4
        if (obj.delDel("abcdel").equals("abcdel")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"abcdel\") expected \"abcdel\"");
            failed++;
        }

        // Test 5
        if (obj.delDel("add").equals("add")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"add\") expected \"add\"");
            failed++;
        }

        // Test 6
        if (obj.delDel("ad").equals("ad")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"ad\") expected \"ad\"");
            failed++;
        }

        // Test 7
        if (obj.delDel("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"a\") expected \"a\"");
            failed++;
        }

        // Test 8
        if (obj.delDel("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.delDel("del").equals("del")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"del\") expected \"del\"");
            failed++;
        }

        // Test 10
        if (obj.delDel("adel").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"adel\") expected \"a\"");
            failed++;
        }

        // Test 11
        if (obj.delDel("aadelbb").equals("aadelbb")) {
            passed++;
        } else {
            System.out.println("FAIL: delDel(\"aadelbb\") expected \"aadelbb\"");
            failed++;
        }

        System.out.println("delDel: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}