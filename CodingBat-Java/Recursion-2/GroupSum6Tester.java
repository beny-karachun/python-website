/**
 * Tester for GroupSum6 - CodingBat Java
 * 3 test cases
 */
public class GroupSum6Tester {

    public static void main(String[] args) {
        GroupSum6 obj = new GroupSum6();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.groupSum6(0, {5, 6, 2], 8) == true) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum6(0, [5, 6, 2], 8) expected true");
            failed++;
        }

        // Test 2
        if (obj.groupSum6(0, {5, 6, 2], 9) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum6(0, [5, 6, 2], 9) expected false");
            failed++;
        }

        // Test 3
        if (obj.groupSum6(0, {5, 6, 2], 7) == false) {
            passed++;
        } else {
            System.out.println("FAIL: groupSum6(0, [5, 6, 2], 7) expected false");
            failed++;
        }

        System.out.println("groupSum6: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}