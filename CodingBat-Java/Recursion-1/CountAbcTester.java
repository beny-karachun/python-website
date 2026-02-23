/**
 * Tester for CountAbc - CodingBat Java
 * 12 test cases
 */
public class CountAbcTester {

    public static void main(String[] args) {
        CountAbc obj = new CountAbc();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countAbc("abc") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"abc\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countAbc("abcxxabc") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"abcxxabc\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countAbc("abaxxaba") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"abaxxaba\") expected 2");
            failed++;
        }

        // Test 4
        if (obj.countAbc("ababc") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"ababc\") expected 2");
            failed++;
        }

        // Test 5
        if (obj.countAbc("abxbc") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"abxbc\") expected 0");
            failed++;
        }

        // Test 6
        if (obj.countAbc("aaabc") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"aaabc\") expected 1");
            failed++;
        }

        // Test 7
        if (obj.countAbc("hello") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"hello\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.countAbc("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"\") expected 0");
            failed++;
        }

        // Test 9
        if (obj.countAbc("ab") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"ab\") expected 0");
            failed++;
        }

        // Test 10
        if (obj.countAbc("aba") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"aba\") expected 1");
            failed++;
        }

        // Test 11
        if (obj.countAbc("aca") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"aca\") expected 0");
            failed++;
        }

        // Test 12
        if (obj.countAbc("aaa") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countAbc(\"aaa\") expected 0");
            failed++;
        }

        System.out.println("countAbc: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}