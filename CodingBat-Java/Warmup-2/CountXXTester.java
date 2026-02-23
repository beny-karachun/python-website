/**
 * Tester for CountXX - CodingBat Java
 * 9 test cases
 */
public class CountXXTester {

    public static void main(String[] args) {
        CountXX obj = new CountXX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countXX("abcxx") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"abcxx\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countXX("xxx") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"xxx\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countXX("xxxx") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"xxxx\") expected 3");
            failed++;
        }

        // Test 4
        if (obj.countXX("abc") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"abc\") expected 0");
            failed++;
        }

        // Test 5
        if (obj.countXX("Hello there") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"Hello there\") expected 0");
            failed++;
        }

        // Test 6
        if (obj.countXX("Hexxo thxxe") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"Hexxo thxxe\") expected 2");
            failed++;
        }

        // Test 7
        if (obj.countXX("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.countXX("Kittens") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"Kittens\") expected 0");
            failed++;
        }

        // Test 9
        if (obj.countXX("Kittensxxx") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countXX(\"Kittensxxx\") expected 2");
            failed++;
        }

        System.out.println("countXX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}