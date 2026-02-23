/**
 * Tester for Count8 - CodingBat Java
 * 18 test cases
 */
public class Count8Tester {

    public static void main(String[] args) {
        Count8 obj = new Count8();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.count8(8) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count8(8) expected 1");
            failed++;
        }

        // Test 2
        if (obj.count8(818) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count8(818) expected 2");
            failed++;
        }

        // Test 3
        if (obj.count8(8818) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: count8(8818) expected 4");
            failed++;
        }

        // Test 4
        if (obj.count8(8088) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: count8(8088) expected 4");
            failed++;
        }

        // Test 5
        if (obj.count8(123) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count8(123) expected 0");
            failed++;
        }

        // Test 6
        if (obj.count8(81238) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count8(81238) expected 2");
            failed++;
        }

        // Test 7
        if (obj.count8(88788) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: count8(88788) expected 6");
            failed++;
        }

        // Test 8
        if (obj.count8(8234) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count8(8234) expected 1");
            failed++;
        }

        // Test 9
        if (obj.count8(2348) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count8(2348) expected 1");
            failed++;
        }

        // Test 10
        if (obj.count8(23884) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: count8(23884) expected 3");
            failed++;
        }

        // Test 11
        if (obj.count8(0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: count8(0) expected 0");
            failed++;
        }

        // Test 12
        if (obj.count8(1818188) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: count8(1818188) expected 5");
            failed++;
        }

        // Test 13
        if (obj.count8(8818181) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: count8(8818181) expected 5");
            failed++;
        }

        // Test 14
        if (obj.count8(1080) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count8(1080) expected 1");
            failed++;
        }

        // Test 15
        if (obj.count8(188) == 3) {
            passed++;
        } else {
            System.out.println("FAIL: count8(188) expected 3");
            failed++;
        }

        // Test 16
        if (obj.count8(88888) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: count8(88888) expected 9");
            failed++;
        }

        // Test 17
        if (obj.count8(9898) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: count8(9898) expected 2");
            failed++;
        }

        // Test 18
        if (obj.count8(78) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: count8(78) expected 1");
            failed++;
        }

        System.out.println("count8: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}