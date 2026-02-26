/**
 * Tester for ExtraFront - CodingBat Java
 * 6 test cases
 */
public class ExtraFrontTester {

    public static void main(String[] args) {
        ExtraFront obj = new ExtraFront();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.extraFront("Hello").equals("HeHeHe")) {
            passed++;
        } else {
            System.out.println("FAIL: extraFront(\"Hello\") expected \"HeHeHe\"");
            failed++;
        }

        // Test 2
        if (obj.extraFront("ab").equals("ababab")) {
            passed++;
        } else {
            System.out.println("FAIL: extraFront(\"ab\") expected \"ababab\"");
            failed++;
        }

        // Test 3
        if (obj.extraFront("H").equals("HHH")) {
            passed++;
        } else {
            System.out.println("FAIL: extraFront(\"H\") expected \"HHH\"");
            failed++;
        }

        // Test 4
        if (obj.extraFront("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: extraFront(\"\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.extraFront("Candy").equals("CaCaCa")) {
            passed++;
        } else {
            System.out.println("FAIL: extraFront(\"Candy\") expected \"CaCaCa\"");
            failed++;
        }

        // Test 6
        if (obj.extraFront("Code").equals("CoCoCo")) {
            passed++;
        } else {
            System.out.println("FAIL: extraFront(\"Code\") expected \"CoCoCo\"");
            failed++;
        }

        System.out.println("extraFront: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}