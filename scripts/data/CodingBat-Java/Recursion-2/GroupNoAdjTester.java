/**
 * Tester for GroupNoAdj - CodingBat Java
 * 3 test cases
 */
public class GroupNoAdjTester {

    public static void main(String[] args) {
        GroupNoAdj obj = new GroupNoAdj();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.groupNoAdj(0, {2, 5, 10, 4], 12) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupNoAdj(0, [2, 5, 10, 4], 12) expected true");
            failed++;
        }

        // Test 2
        if (obj.groupNoAdj(0, {2, 5, 10, 4], 14) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupNoAdj(0, [2, 5, 10, 4], 14) expected false");
            failed++;
        }

        // Test 3
        if (obj.groupNoAdj(0, {2, 5, 10, 4], 7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupNoAdj(0, [2, 5, 10, 4], 7) expected false");
            failed++;
        }

        System.out.println("groupNoAdj: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}