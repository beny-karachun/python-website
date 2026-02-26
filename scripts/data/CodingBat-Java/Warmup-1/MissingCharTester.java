/**
 * Tester for MissingChar - CodingBat Java
 * 10 test cases
 */
public class MissingCharTester {

    public static void main(String[] args) {
        MissingChar obj = new MissingChar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.missingChar("kitten", 1).equals("ktten")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"kitten\", 1) expected \"ktten\"");
            failed++;
        }

        // Test 2
        if (obj.missingChar("kitten", 0).equals("itten")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"kitten\", 0) expected \"itten\"");
            failed++;
        }

        // Test 3
        if (obj.missingChar("kitten", 4).equals("kittn")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"kitten\", 4) expected \"kittn\"");
            failed++;
        }

        // Test 4
        if (obj.missingChar("Hi", 0).equals("i")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"Hi\", 0) expected \"i\"");
            failed++;
        }

        // Test 5
        if (obj.missingChar("Hi", 1).equals("H")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"Hi\", 1) expected \"H\"");
            failed++;
        }

        // Test 6
        if (obj.missingChar("code", 0).equals("ode")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"code\", 0) expected \"ode\"");
            failed++;
        }

        // Test 7
        if (obj.missingChar("code", 1).equals("cde")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"code\", 1) expected \"cde\"");
            failed++;
        }

        // Test 8
        if (obj.missingChar("code", 2).equals("coe")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"code\", 2) expected \"coe\"");
            failed++;
        }

        // Test 9
        if (obj.missingChar("code", 3).equals("cod")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"code\", 3) expected \"cod\"");
            failed++;
        }

        // Test 10
        if (obj.missingChar("chocolate", 8).equals("chocolat")) {
            passed++;
        } else {
            System.out.println("FAIL: missingChar(\"chocolate\", 8) expected \"chocolat\"");
            failed++;
        }

        System.out.println("missingChar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}