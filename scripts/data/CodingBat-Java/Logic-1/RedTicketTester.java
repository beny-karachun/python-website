/**
 * Tester for RedTicket - CodingBat Java
 * 11 test cases
 */
public class RedTicketTester {

    public static void main(String[] args) {
        RedTicket obj = new RedTicket();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.redTicket(2, 2, 2) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(2, 2, 2) expected 10");
            failed++;
        }

        // Test 2
        if (obj.redTicket(2, 2, 1) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(2, 2, 1) expected 0");
            failed++;
        }

        // Test 3
        if (obj.redTicket(0, 0, 0) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(0, 0, 0) expected 5");
            failed++;
        }

        // Test 4
        if (obj.redTicket(2, 0, 0) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(2, 0, 0) expected 1");
            failed++;
        }

        // Test 5
        if (obj.redTicket(1, 1, 1) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(1, 1, 1) expected 5");
            failed++;
        }

        // Test 6
        if (obj.redTicket(1, 2, 1) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(1, 2, 1) expected 0");
            failed++;
        }

        // Test 7
        if (obj.redTicket(1, 2, 0) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(1, 2, 0) expected 1");
            failed++;
        }

        // Test 8
        if (obj.redTicket(0, 2, 2) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(0, 2, 2) expected 1");
            failed++;
        }

        // Test 9
        if (obj.redTicket(1, 2, 2) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(1, 2, 2) expected 1");
            failed++;
        }

        // Test 10
        if (obj.redTicket(0, 2, 0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(0, 2, 0) expected 0");
            failed++;
        }

        // Test 11
        if (obj.redTicket(1, 1, 2) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: redTicket(1, 1, 2) expected 0");
            failed++;
        }

        System.out.println("redTicket: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}