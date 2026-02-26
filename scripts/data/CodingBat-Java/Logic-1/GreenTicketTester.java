/**
 * Tester for GreenTicket - CodingBat Java
 * 12 test cases
 */
public class GreenTicketTester {

    public static void main(String[] args) {
        GreenTicket obj = new GreenTicket();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.greenTicket(1, 2, 3) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(1, 2, 3) expected 0");
            failed++;
        }

        // Test 2
        if (obj.greenTicket(2, 2, 2) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(2, 2, 2) expected 20");
            failed++;
        }

        // Test 3
        if (obj.greenTicket(1, 1, 2) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(1, 1, 2) expected 10");
            failed++;
        }

        // Test 4
        if (obj.greenTicket(2, 1, 1) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(2, 1, 1) expected 10");
            failed++;
        }

        // Test 5
        if (obj.greenTicket(1, 2, 1) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(1, 2, 1) expected 10");
            failed++;
        }

        // Test 6
        if (obj.greenTicket(3, 2, 1) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(3, 2, 1) expected 0");
            failed++;
        }

        // Test 7
        if (obj.greenTicket(0, 0, 0) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(0, 0, 0) expected 20");
            failed++;
        }

        // Test 8
        if (obj.greenTicket(2, 0, 0) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(2, 0, 0) expected 10");
            failed++;
        }

        // Test 9
        if (obj.greenTicket(0, 9, 10) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(0, 9, 10) expected 0");
            failed++;
        }

        // Test 10
        if (obj.greenTicket(0, 10, 0) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(0, 10, 0) expected 10");
            failed++;
        }

        // Test 11
        if (obj.greenTicket(9, 9, 9) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(9, 9, 9) expected 20");
            failed++;
        }

        // Test 12
        if (obj.greenTicket(9, 0, 9) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: greenTicket(9, 0, 9) expected 10");
            failed++;
        }

        System.out.println("greenTicket: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}