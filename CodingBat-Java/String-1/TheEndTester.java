/**
 * Tester for TheEnd - CodingBat Java
 * 10 test cases
 */
public class TheEndTester {

    public static void main(String[] args) {
        TheEnd obj = new TheEnd();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.theEnd("Hello", true).equals("H")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"Hello\", true) expected \"H\"");
            failed++;
        }

        // Test 2
        if (obj.theEnd("Hello", false).equals("o")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"Hello\", false) expected \"o\"");
            failed++;
        }

        // Test 3
        if (obj.theEnd("oh", true).equals("o")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"oh\", true) expected \"o\"");
            failed++;
        }

        // Test 4
        if (obj.theEnd("oh", false).equals("h")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"oh\", false) expected \"h\"");
            failed++;
        }

        // Test 5
        if (obj.theEnd("x", true).equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"x\", true) expected \"x\"");
            failed++;
        }

        // Test 6
        if (obj.theEnd("x", false).equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"x\", false) expected \"x\"");
            failed++;
        }

        // Test 7
        if (obj.theEnd("java", true).equals("j")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"java\", true) expected \"j\"");
            failed++;
        }

        // Test 8
        if (obj.theEnd("chocolate", false).equals("e")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"chocolate\", false) expected \"e\"");
            failed++;
        }

        // Test 9
        if (obj.theEnd("1234", true).equals("1")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"1234\", true) expected \"1\"");
            failed++;
        }

        // Test 10
        if (obj.theEnd("code", false).equals("e")) {
            passed++;
        } else {
            System.out.println("FAIL: theEnd(\"code\", false) expected \"e\"");
            failed++;
        }

        System.out.println("theEnd: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}