/**
 * Tester for NTwice - CodingBat Java
 * 7 test cases
 */
public class NTwiceTester {

    public static void main(String[] args) {
        NTwice obj = new NTwice();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.nTwice("Hello", 2).equals("Helo")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Hello\", 2) expected \"Helo\"");
            failed++;
        }

        // Test 2
        if (obj.nTwice("Chocolate", 3).equals("Choate")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Chocolate\", 3) expected \"Choate\"");
            failed++;
        }

        // Test 3
        if (obj.nTwice("Chocolate", 1).equals("Ce")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Chocolate\", 1) expected \"Ce\"");
            failed++;
        }

        // Test 4
        if (obj.nTwice("Chocolate", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Chocolate\", 0) expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.nTwice("Hello", 4).equals("Hellello")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Hello\", 4) expected \"Hellello\"");
            failed++;
        }

        // Test 6
        if (obj.nTwice("Code", 4).equals("CodeCode")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Code\", 4) expected \"CodeCode\"");
            failed++;
        }

        // Test 7
        if (obj.nTwice("Code", 2).equals("Code")) {
            passed++;
        } else {
            System.out.println("FAIL: nTwice(\"Code\", 2) expected \"Code\"");
            failed++;
        }

        System.out.println("nTwice: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}