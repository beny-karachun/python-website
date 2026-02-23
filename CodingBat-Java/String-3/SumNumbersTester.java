/**
 * Tester for SumNumbers - CodingBat Java
 * 9 test cases
 */
public class SumNumbersTester {

    public static void main(String[] args) {
        SumNumbers obj = new SumNumbers();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sumNumbers("abc123xyz") == 123) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"abc123xyz\") expected 123");
            failed++;
        }

        // Test 2
        if (obj.sumNumbers("aa11b33") == 44) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"aa11b33\") expected 44");
            failed++;
        }

        // Test 3
        if (obj.sumNumbers("7 11") == 18) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"7 11\") expected 18");
            failed++;
        }

        // Test 4
        if (obj.sumNumbers("Chocolate") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"Chocolate\") expected 0");
            failed++;
        }

        // Test 5
        if (obj.sumNumbers("5hoco1a1e") == 7) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"5hoco1a1e\") expected 7");
            failed++;
        }

        // Test 6
        if (obj.sumNumbers("5$$1;;1!!") == 7) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"5$$1;;1!!\") expected 7");
            failed++;
        }

        // Test 7
        if (obj.sumNumbers("a1234bb11") == 1245) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"a1234bb11\") expected 1245");
            failed++;
        }

        // Test 8
        if (obj.sumNumbers("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"\") expected 0");
            failed++;
        }

        // Test 9
        if (obj.sumNumbers("a22bbb3") == 25) {
            passed++;
        } else {
            System.out.println("FAIL: sumNumbers(\"a22bbb3\") expected 25");
            failed++;
        }

        System.out.println("sumNumbers: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}