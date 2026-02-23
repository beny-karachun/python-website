/**
 * Tester for MonkeyTrouble - CodingBat Java
 * 4 test cases
 */
public class MonkeyTroubleTester {

    public static void main(String[] args) {
        MonkeyTrouble obj = new MonkeyTrouble();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.monkeyTrouble(true, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: monkeyTrouble(true, true) expected true");
            failed++;
        }

        // Test 2
        if (obj.monkeyTrouble(false, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: monkeyTrouble(false, false) expected true");
            failed++;
        }

        // Test 3
        if (obj.monkeyTrouble(true, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: monkeyTrouble(true, false) expected false");
            failed++;
        }

        // Test 4
        if (obj.monkeyTrouble(false, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: monkeyTrouble(false, true) expected false");
            failed++;
        }

        System.out.println("monkeyTrouble: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}