/**
 * Tester for TeaParty - CodingBat Java
 * 13 test cases
 */
public class TeaPartyTester {

    public static void main(String[] args) {
        TeaParty obj = new TeaParty();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.teaParty(6, 8) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(6, 8) expected 1");
            failed++;
        }

        // Test 2
        if (obj.teaParty(3, 8) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(3, 8) expected 0");
            failed++;
        }

        // Test 3
        if (obj.teaParty(20, 6) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(20, 6) expected 2");
            failed++;
        }

        // Test 4
        if (obj.teaParty(12, 6) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(12, 6) expected 2");
            failed++;
        }

        // Test 5
        if (obj.teaParty(11, 6) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(11, 6) expected 1");
            failed++;
        }

        // Test 6
        if (obj.teaParty(11, 4) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(11, 4) expected 0");
            failed++;
        }

        // Test 7
        if (obj.teaParty(4, 5) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(4, 5) expected 0");
            failed++;
        }

        // Test 8
        if (obj.teaParty(5, 5) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(5, 5) expected 1");
            failed++;
        }

        // Test 9
        if (obj.teaParty(6, 6) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(6, 6) expected 1");
            failed++;
        }

        // Test 10
        if (obj.teaParty(5, 10) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(5, 10) expected 2");
            failed++;
        }

        // Test 11
        if (obj.teaParty(5, 9) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(5, 9) expected 1");
            failed++;
        }

        // Test 12
        if (obj.teaParty(10, 4) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(10, 4) expected 0");
            failed++;
        }

        // Test 13
        if (obj.teaParty(10, 20) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: teaParty(10, 20) expected 2");
            failed++;
        }

        System.out.println("teaParty: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}