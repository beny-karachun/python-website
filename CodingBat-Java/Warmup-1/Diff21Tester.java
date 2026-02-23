/**
 * Tester for Diff21 - CodingBat Java
 * 12 test cases
 */
public class Diff21Tester {

    public static void main(String[] args) {
        Diff21 obj = new Diff21();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.diff21(19) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(19) expected 2");
            failed++;
        }

        // Test 2
        if (obj.diff21(10) == 11) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(10) expected 11");
            failed++;
        }

        // Test 3
        if (obj.diff21(21) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(21) expected 0");
            failed++;
        }

        // Test 4
        if (obj.diff21(22) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(22) expected 2");
            failed++;
        }

        // Test 5
        if (obj.diff21(25) == 8) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(25) expected 8");
            failed++;
        }

        // Test 6
        if (obj.diff21(30) == 18) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(30) expected 18");
            failed++;
        }

        // Test 7
        if (obj.diff21(0) == 21) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(0) expected 21");
            failed++;
        }

        // Test 8
        if (obj.diff21(1) == 20) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(1) expected 20");
            failed++;
        }

        // Test 9
        if (obj.diff21(2) == 19) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(2) expected 19");
            failed++;
        }

        // Test 10
        if (obj.diff21(-1) == 22) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(-1) expected 22");
            failed++;
        }

        // Test 11
        if (obj.diff21(-2) == 23) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(-2) expected 23");
            failed++;
        }

        // Test 12
        if (obj.diff21(50) == 58) {
            passed++;
        } else {
            System.out.println("FAIL: diff21(50) expected 58");
            failed++;
        }

        System.out.println("diff21: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}