/**
 * Tester for GroupSum5 - CodingBat Java
 * 3 test cases
 */
public class GroupSum5Tester {

    public static void main(String[] args) {
        GroupSum5 obj = new GroupSum5();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.groupSum5(0, {2, 5, 10, 4], 19) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum5(0, [2, 5, 10, 4], 19) expected true");
            failed++;
        }

        // Test 2
        if (obj.groupSum5(0, {2, 5, 10, 4], 17) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum5(0, [2, 5, 10, 4], 17) expected true");
            failed++;
        }

        // Test 3
        if (obj.groupSum5(0, {2, 5, 10, 4], 12) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum5(0, [2, 5, 10, 4], 12) expected false");
            failed++;
        }

        System.out.println("groupSum5: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}