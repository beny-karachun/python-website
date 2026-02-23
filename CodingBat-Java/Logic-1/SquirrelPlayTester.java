/**
 * Tester for SquirrelPlay - CodingBat Java
 * 13 test cases
 */
public class SquirrelPlayTester {

    public static void main(String[] args) {
        SquirrelPlay obj = new SquirrelPlay();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.squirrelPlay(70, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(70, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.squirrelPlay(95, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(95, false) expected false");
            failed++;
        }

        // Test 3
        if (obj.squirrelPlay(95, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(95, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.squirrelPlay(90, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(90, false) expected true");
            failed++;
        }

        // Test 5
        if (obj.squirrelPlay(90, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(90, true) expected true");
            failed++;
        }

        // Test 6
        if (obj.squirrelPlay(50, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(50, false) expected false");
            failed++;
        }

        // Test 7
        if (obj.squirrelPlay(50, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(50, true) expected false");
            failed++;
        }

        // Test 8
        if (obj.squirrelPlay(100, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(100, false) expected false");
            failed++;
        }

        // Test 9
        if (obj.squirrelPlay(100, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(100, true) expected true");
            failed++;
        }

        // Test 10
        if (obj.squirrelPlay(105, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(105, true) expected false");
            failed++;
        }

        // Test 11
        if (obj.squirrelPlay(59, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(59, false) expected false");
            failed++;
        }

        // Test 12
        if (obj.squirrelPlay(59, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(59, true) expected false");
            failed++;
        }

        // Test 13
        if (obj.squirrelPlay(60, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: squirrelPlay(60, false) expected true");
            failed++;
        }

        System.out.println("squirrelPlay: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}