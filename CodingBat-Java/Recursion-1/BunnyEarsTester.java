/**
 * Tester for BunnyEars - CodingBat Java
 * 9 test cases
 */
public class BunnyEarsTester {

    public static void main(String[] args) {
        BunnyEars obj = new BunnyEars();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.bunnyEars(0) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(0) expected 0");
            failed++;
        }

        // Test 2
        if (obj.bunnyEars(1) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(1) expected 2");
            failed++;
        }

        // Test 3
        if (obj.bunnyEars(2) == 4) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(2) expected 4");
            failed++;
        }

        // Test 4
        if (obj.bunnyEars(3) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(3) expected 6");
            failed++;
        }

        // Test 5
        if (obj.bunnyEars(4) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(4) expected 8");
            failed++;
        }

        // Test 6
        if (obj.bunnyEars(5) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(5) expected 10");
            failed++;
        }

        // Test 7
        if (obj.bunnyEars(12) == 24) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(12) expected 24");
            failed++;
        }

        // Test 8
        if (obj.bunnyEars(50) == 100) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(50) expected 100");
            failed++;
        }

        // Test 9
        if (obj.bunnyEars(234) == 468) {
            passed++;
        } else {
            System.out.println("FAIL: bunnyEars(234) expected 468");
            failed++;
        }

        System.out.println("bunnyEars: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}