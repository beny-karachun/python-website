/**
 * Tester for MakeChocolate - CodingBat Java
 * 24 test cases
 */
public class MakeChocolateTester {

    public static void main(String[] args) {
        MakeChocolate obj = new MakeChocolate();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.makeChocolate(4, 1, 9) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(4, 1, 9) expected 4");
            failed++;
        }

        // Test 2
        if (obj.makeChocolate(4, 1, 10) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(4, 1, 10) expected -1");
            failed++;
        }

        // Test 3
        if (obj.makeChocolate(4, 1, 7) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(4, 1, 7) expected 2");
            failed++;
        }

        // Test 4
        if (obj.makeChocolate(6, 2, 7) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 2, 7) expected 2");
            failed++;
        }

        // Test 5
        if (obj.makeChocolate(4, 1, 5) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(4, 1, 5) expected 0");
            failed++;
        }

        // Test 6
        if (obj.makeChocolate(4, 1, 4) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(4, 1, 4) expected 4");
            failed++;
        }

        // Test 7
        if (obj.makeChocolate(5, 4, 9) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(5, 4, 9) expected 4");
            failed++;
        }

        // Test 8
        if (obj.makeChocolate(9, 3, 18) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(9, 3, 18) expected 3");
            failed++;
        }

        // Test 9
        if (obj.makeChocolate(3, 1, 9) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(3, 1, 9) expected -1");
            failed++;
        }

        // Test 10
        if (obj.makeChocolate(1, 2, 7) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(1, 2, 7) expected -1");
            failed++;
        }

        // Test 11
        if (obj.makeChocolate(1, 2, 6) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(1, 2, 6) expected 1");
            failed++;
        }

        // Test 12
        if (obj.makeChocolate(1, 2, 5) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(1, 2, 5) expected 0");
            failed++;
        }

        // Test 13
        if (obj.makeChocolate(6, 1, 10) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 1, 10) expected 5");
            failed++;
        }

        // Test 14
        if (obj.makeChocolate(6, 1, 11) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 1, 11) expected 6");
            failed++;
        }

        // Test 15
        if (obj.makeChocolate(6, 1, 12) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 1, 12) expected -1");
            failed++;
        }

        // Test 16
        if (obj.makeChocolate(6, 1, 13) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 1, 13) expected -1");
            failed++;
        }

        // Test 17
        if (obj.makeChocolate(6, 2, 10) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 2, 10) expected 0");
            failed++;
        }

        // Test 18
        if (obj.makeChocolate(6, 2, 11) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 2, 11) expected 1");
            failed++;
        }

        // Test 19
        if (obj.makeChocolate(6, 2, 12) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(6, 2, 12) expected 2");
            failed++;
        }

        // Test 20
        if (obj.makeChocolate(60, 100, 550) == 50) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(60, 100, 550) expected 50");
            failed++;
        }

        // Test 21
        if (obj.makeChocolate(1000, 1000000, 5000006) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(1000, 1000000, 5000006) expected 6");
            failed++;
        }

        // Test 22
        if (obj.makeChocolate(7, 1, 12) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(7, 1, 12) expected 7");
            failed++;
        }

        // Test 23
        if (obj.makeChocolate(7, 1, 13) == -1) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(7, 1, 13) expected -1");
            failed++;
        }

        // Test 24
        if (obj.makeChocolate(7, 2, 13) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: makeChocolate(7, 2, 13) expected 3");
            failed++;
        }

        System.out.println("makeChocolate: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}