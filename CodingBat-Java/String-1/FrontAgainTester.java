/**
 * Tester for FrontAgain - CodingBat Java
 * 11 test cases
 */
public class FrontAgainTester {

    public static void main(String[] args) {
        FrontAgain obj = new FrontAgain();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.frontAgain("edited") == true) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"edited\") expected true");
            failed++;
        }

        // Test 2
        if (obj.frontAgain("edit") == false) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"edit\") expected false");
            failed++;
        }

        // Test 3
        if (obj.frontAgain("ed") == true) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"ed\") expected true");
            failed++;
        }

        // Test 4
        if (obj.frontAgain("jj") == true) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"jj\") expected true");
            failed++;
        }

        // Test 5
        if (obj.frontAgain("jjj") == true) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"jjj\") expected true");
            failed++;
        }

        // Test 6
        if (obj.frontAgain("jjjj") == true) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"jjjj\") expected true");
            failed++;
        }

        // Test 7
        if (obj.frontAgain("jjjk") == false) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"jjjk\") expected false");
            failed++;
        }

        // Test 8
        if (obj.frontAgain("x") == false) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"x\") expected false");
            failed++;
        }

        // Test 9
        if (obj.frontAgain("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"\") expected false");
            failed++;
        }

        // Test 10
        if (obj.frontAgain("java") == false) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"java\") expected false");
            failed++;
        }

        // Test 11
        if (obj.frontAgain("javaja") == true) {
            passed++;
        } else {
            System.out.println("FAIL: frontAgain(\"javaja\") expected true");
            failed++;
        }

        System.out.println("frontAgain: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}