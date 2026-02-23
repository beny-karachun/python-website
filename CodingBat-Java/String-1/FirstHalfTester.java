/**
 * Tester for FirstHalf - CodingBat Java
 * 7 test cases
 */
public class FirstHalfTester {

    public static void main(String[] args) {
        FirstHalf obj = new FirstHalf();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.firstHalf("WooHoo").equals("Woo")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"WooHoo\") expected \"Woo\"");
            failed++;
        }

        // Test 2
        if (obj.firstHalf("HelloThere").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"HelloThere\") expected \"Hello\"");
            failed++;
        }

        // Test 3
        if (obj.firstHalf("abcdef").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"abcdef\") expected \"abc\"");
            failed++;
        }

        // Test 4
        if (obj.firstHalf("ab").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"ab\") expected \"a\"");
            failed++;
        }

        // Test 5
        if (obj.firstHalf("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.firstHalf("0123456789").equals("01234")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"0123456789\") expected \"01234\"");
            failed++;
        }

        // Test 7
        if (obj.firstHalf("kitten").equals("kit")) {
            passed++;
        } else {
            System.out.println("FAIL: firstHalf(\"kitten\") expected \"kit\"");
            failed++;
        }

        System.out.println("firstHalf: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}