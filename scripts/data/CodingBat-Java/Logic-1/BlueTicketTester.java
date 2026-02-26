/**
 * Tester for BlueTicket - CodingBat Java
 * 12 test cases
 */
public class BlueTicketTester {

    public static void main(String[] args) {
        BlueTicket obj = new BlueTicket();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.blueTicket(9, 1, 0) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(9, 1, 0) expected 10");
            failed++;
        }

        // Test 2
        if (obj.blueTicket(9, 2, 0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(9, 2, 0) expected 0");
            failed++;
        }

        // Test 3
        if (obj.blueTicket(6, 1, 4) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(6, 1, 4) expected 10");
            failed++;
        }

        // Test 4
        if (obj.blueTicket(6, 1, 5) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(6, 1, 5) expected 0");
            failed++;
        }

        // Test 5
        if (obj.blueTicket(10, 0, 0) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(10, 0, 0) expected 10");
            failed++;
        }

        // Test 6
        if (obj.blueTicket(15, 0, 5) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(15, 0, 5) expected 5");
            failed++;
        }

        // Test 7
        if (obj.blueTicket(5, 15, 5) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(5, 15, 5) expected 10");
            failed++;
        }

        // Test 8
        if (obj.blueTicket(4, 11, 1) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(4, 11, 1) expected 5");
            failed++;
        }

        // Test 9
        if (obj.blueTicket(13, 2, 3) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(13, 2, 3) expected 5");
            failed++;
        }

        // Test 10
        if (obj.blueTicket(8, 4, 3) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(8, 4, 3) expected 0");
            failed++;
        }

        // Test 11
        if (obj.blueTicket(8, 4, 2) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(8, 4, 2) expected 10");
            failed++;
        }

        // Test 12
        if (obj.blueTicket(8, 4, 1) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blueTicket(8, 4, 1) expected 0");
            failed++;
        }

        System.out.println("blueTicket: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}