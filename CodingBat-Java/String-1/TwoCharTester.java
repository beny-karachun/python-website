/**
 * Tester for TwoChar - CodingBat Java
 * 15 test cases
 */
public class TwoCharTester {

    public static void main(String[] args) {
        TwoChar obj = new TwoChar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.twoChar("java", 0).equals("ja")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"java\", 0) expected \"ja\"");
            failed++;
        }

        // Test 2
        if (obj.twoChar("java", 2).equals("va")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"java\", 2) expected \"va\"");
            failed++;
        }

        // Test 3
        if (obj.twoChar("java", 3).equals("ja")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"java\", 3) expected \"ja\"");
            failed++;
        }

        // Test 4
        if (obj.twoChar("java", 4).equals("ja")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"java\", 4) expected \"ja\"");
            failed++;
        }

        // Test 5
        if (obj.twoChar("java", -1).equals("ja")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"java\", -1) expected \"ja\"");
            failed++;
        }

        // Test 6
        if (obj.twoChar("Hello", 0).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 0) expected \"He\"");
            failed++;
        }

        // Test 7
        if (obj.twoChar("Hello", 1).equals("el")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 1) expected \"el\"");
            failed++;
        }

        // Test 8
        if (obj.twoChar("Hello", 99).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 99) expected \"He\"");
            failed++;
        }

        // Test 9
        if (obj.twoChar("Hello", 3).equals("lo")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 3) expected \"lo\"");
            failed++;
        }

        // Test 10
        if (obj.twoChar("Hello", 4).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 4) expected \"He\"");
            failed++;
        }

        // Test 11
        if (obj.twoChar("Hello", 5).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 5) expected \"He\"");
            failed++;
        }

        // Test 12
        if (obj.twoChar("Hello", -7).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", -7) expected \"He\"");
            failed++;
        }

        // Test 13
        if (obj.twoChar("Hello", 6).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", 6) expected \"He\"");
            failed++;
        }

        // Test 14
        if (obj.twoChar("Hello", -1).equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"Hello\", -1) expected \"He\"");
            failed++;
        }

        // Test 15
        if (obj.twoChar("yay", 0).equals("ya")) {
            passed++;
        } else {
            System.out.println("FAIL: twoChar(\"yay\", 0) expected \"ya\"");
            failed++;
        }

        System.out.println("twoChar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}