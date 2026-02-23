/**
 * Tester for GroupSumClump - CodingBat Java
 * 3 test cases
 */
public class GroupSumClumpTester {

    public static void main(String[] args) {
        GroupSumClump obj = new GroupSumClump();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.groupSumClump(0, {2, 4, 8], 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSumClump(0, [2, 4, 8], 10) expected true");
            failed++;
        }

        // Test 2
        if (obj.groupSumClump(0, {1, 2, 4, 8, 1], 14) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSumClump(0, [1, 2, 4, 8, 1], 14) expected true");
            failed++;
        }

        // Test 3
        if (obj.groupSumClump(0, {2, 4, 4, 8], 14) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupSumClump(0, [2, 4, 4, 8], 14) expected false");
            failed++;
        }

        System.out.println("groupSumClump: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}