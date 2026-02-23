/**
 * Tester for AlarmClock - CodingBat Java
 * 9 test cases
 */
public class AlarmClockTester {

    public static void main(String[] args) {
        AlarmClock obj = new AlarmClock();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.alarmClock(1, false).equals("7:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(1, false) expected \"7:00\"");
            failed++;
        }

        // Test 2
        if (obj.alarmClock(5, false).equals("7:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(5, false) expected \"7:00\"");
            failed++;
        }

        // Test 3
        if (obj.alarmClock(0, false).equals("10:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(0, false) expected \"10:00\"");
            failed++;
        }

        // Test 4
        if (obj.alarmClock(6, false).equals("10:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(6, false) expected \"10:00\"");
            failed++;
        }

        // Test 5
        if (obj.alarmClock(0, true).equals("off")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(0, true) expected \"off\"");
            failed++;
        }

        // Test 6
        if (obj.alarmClock(6, true).equals("off")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(6, true) expected \"off\"");
            failed++;
        }

        // Test 7
        if (obj.alarmClock(1, true).equals("10:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(1, true) expected \"10:00\"");
            failed++;
        }

        // Test 8
        if (obj.alarmClock(3, true).equals("10:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(3, true) expected \"10:00\"");
            failed++;
        }

        // Test 9
        if (obj.alarmClock(5, true).equals("10:00")) {
            passed++;
        } else {
            System.out.println("FAIL: alarmClock(5, true) expected \"10:00\"");
            failed++;
        }

        System.out.println("alarmClock: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}