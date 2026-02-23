/**
 * Tester for CaughtSpeeding - CodingBat Java
 * 12 test cases
 */
public class CaughtSpeedingTester {

    public static void main(String[] args) {
        CaughtSpeeding obj = new CaughtSpeeding();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.caughtSpeeding(60, false) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(60, false) expected 0");
            failed++;
        }

        // Test 2
        if (obj.caughtSpeeding(65, false) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(65, false) expected 1");
            failed++;
        }

        // Test 3
        if (obj.caughtSpeeding(65, true) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(65, true) expected 0");
            failed++;
        }

        // Test 4
        if (obj.caughtSpeeding(80, false) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(80, false) expected 1");
            failed++;
        }

        // Test 5
        if (obj.caughtSpeeding(85, false) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(85, false) expected 2");
            failed++;
        }

        // Test 6
        if (obj.caughtSpeeding(85, true) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(85, true) expected 1");
            failed++;
        }

        // Test 7
        if (obj.caughtSpeeding(70, false) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(70, false) expected 1");
            failed++;
        }

        // Test 8
        if (obj.caughtSpeeding(75, false) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(75, false) expected 1");
            failed++;
        }

        // Test 9
        if (obj.caughtSpeeding(75, true) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(75, true) expected 1");
            failed++;
        }

        // Test 10
        if (obj.caughtSpeeding(40, false) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(40, false) expected 0");
            failed++;
        }

        // Test 11
        if (obj.caughtSpeeding(40, true) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(40, true) expected 0");
            failed++;
        }

        // Test 12
        if (obj.caughtSpeeding(90, false) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: caughtSpeeding(90, false) expected 2");
            failed++;
        }

        System.out.println("caughtSpeeding: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}