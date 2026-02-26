/**
 * Tester for IcyHot - CodingBat Java
 * 6 test cases
 */
public class IcyHotTester {

    public static void main(String[] args) {
        IcyHot obj = new IcyHot();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.icyHot(120, -1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: icyHot(120, -1) expected true");
            failed++;
        }

        // Test 2
        if (obj.icyHot(-1, 120) == true) {
            passed++;
        } else {
            System.out.println("FAIL: icyHot(-1, 120) expected true");
            failed++;
        }

        // Test 3
        if (obj.icyHot(2, 120) == false) {
            passed++;
        } else {
            System.out.println("FAIL: icyHot(2, 120) expected false");
            failed++;
        }

        // Test 4
        if (obj.icyHot(-1, 100) == false) {
            passed++;
        } else {
            System.out.println("FAIL: icyHot(-1, 100) expected false");
            failed++;
        }

        // Test 5
        if (obj.icyHot(-2, -2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: icyHot(-2, -2) expected false");
            failed++;
        }

        // Test 6
        if (obj.icyHot(120, 120) == false) {
            passed++;
        } else {
            System.out.println("FAIL: icyHot(120, 120) expected false");
            failed++;
        }

        System.out.println("icyHot: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}