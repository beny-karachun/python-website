/**
 * Tester for Last2 - CodingBat Java
 * 13 test cases
 */
public class Last2Tester {

    public static void main(String[] args) {
        Last2 obj = new Last2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.last2("hixxhi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"hixxhi\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.last2("xaxxaxaxx") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"xaxxaxaxx\") expected 1");
            failed++;
        }

        // Test 3
        if (obj.last2("axxxaaxx") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"axxxaaxx\") expected 2");
            failed++;
        }

        // Test 4
        if (obj.last2("xxaxxaxxaxx") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"xxaxxaxxaxx\") expected 3");
            failed++;
        }

        // Test 5
        if (obj.last2("xaxaxaxx") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"xaxaxaxx\") expected 0");
            failed++;
        }

        // Test 6
        if (obj.last2("xxxx") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"xxxx\") expected 2");
            failed++;
        }

        // Test 7
        if (obj.last2("13121312") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"13121312\") expected 1");
            failed++;
        }

        // Test 8
        if (obj.last2("11212") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"11212\") expected 1");
            failed++;
        }

        // Test 9
        if (obj.last2("13121311") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"13121311\") expected 0");
            failed++;
        }

        // Test 10
        if (obj.last2("1717171") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"1717171\") expected 2");
            failed++;
        }

        // Test 11
        if (obj.last2("hi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"hi\") expected 0");
            failed++;
        }

        // Test 12
        if (obj.last2("h") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"h\") expected 0");
            failed++;
        }

        // Test 13
        if (obj.last2("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: last2(\"\") expected 0");
            failed++;
        }

        System.out.println("last2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}