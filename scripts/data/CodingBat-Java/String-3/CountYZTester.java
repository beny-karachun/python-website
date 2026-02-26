/**
 * Tester for CountYZ - CodingBat Java
 * 11 test cases
 */
public class CountYZTester {

    public static void main(String[] args) {
        CountYZ obj = new CountYZ();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countYZ("fez day") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"fez day\") expected 2");
            failed++;
        }

        // Test 2
        if (obj.countYZ("day fez") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"day fez\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countYZ("day fyyyz") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"day fyyyz\") expected 2");
            failed++;
        }

        // Test 4
        if (obj.countYZ("day yak") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"day yak\") expected 1");
            failed++;
        }

        // Test 5
        if (obj.countYZ("day:yak") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"day:yak\") expected 1");
            failed++;
        }

        // Test 6
        if (obj.countYZ("!!day--yaz!!") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"!!day--yaz!!\") expected 2");
            failed++;
        }

        // Test 7
        if (obj.countYZ("yak zak") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"yak zak\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.countYZ("DAY abc XYZ") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"DAY abc XYZ\") expected 2");
            failed++;
        }

        // Test 9
        if (obj.countYZ("aaz yyz my") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"aaz yyz my\") expected 3");
            failed++;
        }

        // Test 10
        if (obj.countYZ("y2bz") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"y2bz\") expected 2");
            failed++;
        }

        // Test 11
        if (obj.countYZ("zxyx") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countYZ(\"zxyx\") expected 0");
            failed++;
        }

        System.out.println("countYZ: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}