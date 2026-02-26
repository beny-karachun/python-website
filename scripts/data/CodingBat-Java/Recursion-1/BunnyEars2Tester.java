/**
 * Tester for BunnyEars2 - CodingBat Java
 * 8 test cases
 */
public class BunnyEars2Tester {

    public static void main(String[] args) {
        BunnyEars2 obj = new BunnyEars2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.bunnyEars2(0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(0) expected 0");
            failed++;
        }

        // Test 2
        if (obj.bunnyEars2(1) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(1) expected 2");
            failed++;
        }

        // Test 3
        if (obj.bunnyEars2(2) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(2) expected 5");
            failed++;
        }

        // Test 4
        if (obj.bunnyEars2(3) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(3) expected 7");
            failed++;
        }

        // Test 5
        if (obj.bunnyEars2(4) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(4) expected 10");
            failed++;
        }

        // Test 6
        if (obj.bunnyEars2(5) == 12) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(5) expected 12");
            failed++;
        }

        // Test 7
        if (obj.bunnyEars2(6) == 15) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(6) expected 15");
            failed++;
        }

        // Test 8
        if (obj.bunnyEars2(10) == 25) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars2(10) expected 25");
            failed++;
        }

        System.out.println("bunnyEars2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}