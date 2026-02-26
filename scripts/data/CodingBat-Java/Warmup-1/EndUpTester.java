/**
 * Tester for EndUp - CodingBat Java
 * 7 test cases
 */
public class EndUpTester {

    public static void main(String[] args) {
        EndUp obj = new EndUp();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.endUp("Hello").equals("HeLLO")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"Hello\") expected \"HeLLO\"");
            failed++;
        }

        // Test 2
        if (obj.endUp("hi there").equals("hi thERE")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"hi there\") expected \"hi thERE\"");
            failed++;
        }

        // Test 3
        if (obj.endUp("hi").equals("HI")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"hi\") expected \"HI\"");
            failed++;
        }

        // Test 4
        if (obj.endUp("woo hoo").equals("woo HOO")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"woo hoo\") expected \"woo HOO\"");
            failed++;
        }

        // Test 5
        if (obj.endUp("xyz12").equals("xyZ12")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"xyz12\") expected \"xyZ12\"");
            failed++;
        }

        // Test 6
        if (obj.endUp("x").equals("X")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"x\") expected \"X\"");
            failed++;
        }

        // Test 7
        if (obj.endUp("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: endUp(\"\") expected \"\"");
            failed++;
        }

        System.out.println("endUp: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}