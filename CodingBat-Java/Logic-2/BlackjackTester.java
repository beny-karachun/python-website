/**
 * Tester for Blackjack - CodingBat Java
 * 15 test cases
 */
public class BlackjackTester {

    public static void main(String[] args) {
        Blackjack obj = new Blackjack();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.blackjack(19, 21) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(19, 21) expected 21");
            failed++;
        }

        // Test 2
        if (obj.blackjack(21, 19) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(21, 19) expected 21");
            failed++;
        }

        // Test 3
        if (obj.blackjack(19, 22) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(19, 22) expected 19");
            failed++;
        }

        // Test 4
        if (obj.blackjack(22, 19) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(22, 19) expected 19");
            failed++;
        }

        // Test 5
        if (obj.blackjack(22, 50) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(22, 50) expected 0");
            failed++;
        }

        // Test 6
        if (obj.blackjack(22, 22) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(22, 22) expected 0");
            failed++;
        }

        // Test 7
        if (obj.blackjack(33, 1) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(33, 1) expected 1");
            failed++;
        }

        // Test 8
        if (obj.blackjack(1, 2) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(1, 2) expected 2");
            failed++;
        }

        // Test 9
        if (obj.blackjack(34, 33) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(34, 33) expected 0");
            failed++;
        }

        // Test 10
        if (obj.blackjack(17, 19) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(17, 19) expected 19");
            failed++;
        }

        // Test 11
        if (obj.blackjack(18, 17) == 18) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(18, 17) expected 18");
            failed++;
        }

        // Test 12
        if (obj.blackjack(16, 23) == 16) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(16, 23) expected 16");
            failed++;
        }

        // Test 13
        if (obj.blackjack(3, 4) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(3, 4) expected 4");
            failed++;
        }

        // Test 14
        if (obj.blackjack(3, 2) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(3, 2) expected 3");
            failed++;
        }

        // Test 15
        if (obj.blackjack(21, 20) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: blackjack(21, 20) expected 21");
            failed++;
        }

        System.out.println("blackjack: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}