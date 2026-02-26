/**
 * Tester for CountTriple - CodingBat Java
 * 12 test cases
 */
public class CountTripleTester {

    public static void main(String[] args) {
        CountTriple obj = new CountTriple();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countTriple("abcXXXabc") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"abcXXXabc\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countTriple("xxxabyyyycd") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"xxxabyyyycd\") expected 3");
            failed++;
        }

        // Test 3
        if (obj.countTriple("a") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"a\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.countTriple("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"\") expected 0");
            failed++;
        }

        // Test 5
        if (obj.countTriple("XXXabc") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"XXXabc\") expected 1");
            failed++;
        }

        // Test 6
        if (obj.countTriple("XXXXabc") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"XXXXabc\") expected 2");
            failed++;
        }

        // Test 7
        if (obj.countTriple("XXXXXabc") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"XXXXXabc\") expected 3");
            failed++;
        }

        // Test 8
        if (obj.countTriple("222abyyycdXXX") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"222abyyycdXXX\") expected 3");
            failed++;
        }

        // Test 9
        if (obj.countTriple("abYYYabXXXXXab") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"abYYYabXXXXXab\") expected 4");
            failed++;
        }

        // Test 10
        if (obj.countTriple("abYYXabXXYXXab") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"abYYXabXXYXXab\") expected 0");
            failed++;
        }

        // Test 11
        if (obj.countTriple("abYYXabXXYXXab") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"abYYXabXXYXXab\") expected 0");
            failed++;
        }

        // Test 12
        if (obj.countTriple("122abhhh2") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countTriple(\"122abhhh2\") expected 1");
            failed++;
        }

        System.out.println("countTriple: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}