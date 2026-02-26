/**
 * Tester for EveryNth - CodingBat Java
 * 7 test cases
 */
public class EveryNthTester {

    public static void main(String[] args) {
        EveryNth obj = new EveryNth();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.everyNth("Miracle", 2).equals("Mrce")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"Miracle\", 2) expected \"Mrce\"");
            failed++;
        }

        // Test 2
        if (obj.everyNth("abcdefg", 2).equals("aceg")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"abcdefg\", 2) expected \"aceg\"");
            failed++;
        }

        // Test 3
        if (obj.everyNth("abcdefg", 3).equals("adg")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"abcdefg\", 3) expected \"adg\"");
            failed++;
        }

        // Test 4
        if (obj.everyNth("Chocolate", 3).equals("Cca")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"Chocolate\", 3) expected \"Cca\"");
            failed++;
        }

        // Test 5
        if (obj.everyNth("Chocolates", 3).equals("Ccas")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"Chocolates\", 3) expected \"Ccas\"");
            failed++;
        }

        // Test 6
        if (obj.everyNth("Chocolates", 4).equals("Coe")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"Chocolates\", 4) expected \"Coe\"");
            failed++;
        }

        // Test 7
        if (obj.everyNth("Chocolates", 100).equals("C")) {
            passed++;
        } else {
            System.out.println("FAIL: everyNth(\"Chocolates\", 100) expected \"C\"");
            failed++;
        }

        System.out.println("everyNth: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}