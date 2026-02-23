/**
 * Tester for GroupSum - CodingBat Java
 * 3 test cases
 */
public class GroupSumTester {

    public static void main(String[] args) {
        GroupSum obj = new GroupSum();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.groupSum(0, {2, 4, 8], 10) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum(0, [2, 4, 8], 10) expected true");
            failed++;
        }

        // Test 2
        if (obj.groupSum(0, {2, 4, 8], 14) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum(0, [2, 4, 8], 14) expected true");
            failed++;
        }

        // Test 3
        if (obj.groupSum(0, {2, 4, 8], 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum(0, [2, 4, 8], 9) expected false");
            failed++;
        }

        System.out.println("groupSum: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}