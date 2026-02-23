/**
 * Tester for ParrotTrouble - CodingBat Java
 * 10 test cases
 */
public class ParrotTroubleTester {

    public static void main(String[] args) {
        ParrotTrouble obj = new ParrotTrouble();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.parrotTrouble(true, 6) == true) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(true, 6) expected true");
            failed++;
        }

        // Test 2
        if (obj.parrotTrouble(true, 7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(true, 7) expected false");
            failed++;
        }

        // Test 3
        if (obj.parrotTrouble(false, 6) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(false, 6) expected false");
            failed++;
        }

        // Test 4
        if (obj.parrotTrouble(true, 21) == true) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(true, 21) expected true");
            failed++;
        }

        // Test 5
        if (obj.parrotTrouble(false, 21) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(false, 21) expected false");
            failed++;
        }

        // Test 6
        if (obj.parrotTrouble(false, 20) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(false, 20) expected false");
            failed++;
        }

        // Test 7
        if (obj.parrotTrouble(true, 23) == true) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(true, 23) expected true");
            failed++;
        }

        // Test 8
        if (obj.parrotTrouble(false, 23) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(false, 23) expected false");
            failed++;
        }

        // Test 9
        if (obj.parrotTrouble(true, 20) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(true, 20) expected false");
            failed++;
        }

        // Test 10
        if (obj.parrotTrouble(false, 12) == false) {
            passed++;
        } else {
            System.out.println("FAIL: parrotTrouble(false, 12) expected false");
            failed++;
        }

        System.out.println("parrotTrouble: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}