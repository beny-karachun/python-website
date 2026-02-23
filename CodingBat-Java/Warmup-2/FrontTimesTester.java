/**
 * Tester for FrontTimes - CodingBat Java
 * 7 test cases
 */
public class FrontTimesTester {

    public static void main(String[] args) {
        FrontTimes obj = new FrontTimes();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.frontTimes("Chocolate", 2).equals("ChoCho")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"Chocolate\", 2) expected \"ChoCho\"");
            failed++;
        }

        // Test 2
        if (obj.frontTimes("Chocolate", 3).equals("ChoChoCho")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"Chocolate\", 3) expected \"ChoChoCho\"");
            failed++;
        }

        // Test 3
        if (obj.frontTimes("Abc", 3).equals("AbcAbcAbc")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"Abc\", 3) expected \"AbcAbcAbc\"");
            failed++;
        }

        // Test 4
        if (obj.frontTimes("Ab", 4).equals("AbAbAbAb")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"Ab\", 4) expected \"AbAbAbAb\"");
            failed++;
        }

        // Test 5
        if (obj.frontTimes("A", 4).equals("AAAA")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"A\", 4) expected \"AAAA\"");
            failed++;
        }

        // Test 6
        if (obj.frontTimes("", 4).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"\", 4) expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.frontTimes("Abc", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: frontTimes(\"Abc\", 0) expected \"\"");
            failed++;
        }

        System.out.println("frontTimes: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}