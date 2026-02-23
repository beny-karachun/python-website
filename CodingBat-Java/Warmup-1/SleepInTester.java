/**
 * Tester for SleepIn - CodingBat Java
 * 4 test cases
 */
public class SleepInTester {

    public static void main(String[] args) {
        SleepIn obj = new SleepIn();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sleepIn(false, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: sleepIn(false, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.sleepIn(true, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: sleepIn(true, false) expected false");
            failed++;
        }

        // Test 3
        if (obj.sleepIn(false, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: sleepIn(false, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.sleepIn(true, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: sleepIn(true, true) expected true");
            failed++;
        }

        System.out.println("sleepIn: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}