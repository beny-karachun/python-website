/**
 * Tester for FrontBack - CodingBat Java
 * 8 test cases
 */
public class FrontBackTester {

    public static void main(String[] args) {
        FrontBack obj = new FrontBack();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.frontBack("code").equals("eodc")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"code\") expected \"eodc\"");
            failed++;
        }

        // Test 2
        if (obj.frontBack("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"a\") expected \"a\"");
            failed++;
        }

        // Test 3
        if (obj.frontBack("ab").equals("ba")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"ab\") expected \"ba\"");
            failed++;
        }

        // Test 4
        if (obj.frontBack("abc").equals("cba")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"abc\") expected \"cba\"");
            failed++;
        }

        // Test 5
        if (obj.frontBack("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.frontBack("Chocolate").equals("ehocolatC")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"Chocolate\") expected \"ehocolatC\"");
            failed++;
        }

        // Test 7
        if (obj.frontBack("aavJ").equals("Java")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"aavJ\") expected \"Java\"");
            failed++;
        }

        // Test 8
        if (obj.frontBack("hello").equals("oellh")) {
            passed++;
        } else {
            System.out.println("FAIL: frontBack(\"hello\") expected \"oellh\"");
            failed++;
        }

        System.out.println("frontBack: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}