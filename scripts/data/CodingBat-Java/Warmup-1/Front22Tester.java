/**
 * Tester for Front22 - CodingBat Java
 * 7 test cases
 */
public class Front22Tester {

    public static void main(String[] args) {
        Front22 obj = new Front22();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.front22("kitten").equals("kikittenki")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"kitten\") expected \"kikittenki\"");
            failed++;
        }

        // Test 2
        if (obj.front22("Ha").equals("HaHaHa")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"Ha\") expected \"HaHaHa\"");
            failed++;
        }

        // Test 3
        if (obj.front22("abc").equals("ababcab")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"abc\") expected \"ababcab\"");
            failed++;
        }

        // Test 4
        if (obj.front22("ab").equals("ababab")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"ab\") expected \"ababab\"");
            failed++;
        }

        // Test 5
        if (obj.front22("a").equals("aaa")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"a\") expected \"aaa\"");
            failed++;
        }

        // Test 6
        if (obj.front22("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.front22("Logic").equals("LoLogicLo")) {
            passed++;
        } else {
            System.out.println("FAIL: front22(\"Logic\") expected \"LoLogicLo\"");
            failed++;
        }

        System.out.println("front22: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}