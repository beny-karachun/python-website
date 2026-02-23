/**
 * Tester for CountPairs - CodingBat Java
 * 11 test cases
 */
public class CountPairsTester {

    public static void main(String[] args) {
        CountPairs obj = new CountPairs();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countPairs("axa") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"axa\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countPairs("axax") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"axax\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countPairs("axbx") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"axbx\") expected 1");
            failed++;
        }

        // Test 4
        if (obj.countPairs("hi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"hi\") expected 0");
            failed++;
        }

        // Test 5
        if (obj.countPairs("hihih") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"hihih\") expected 3");
            failed++;
        }

        // Test 6
        if (obj.countPairs("ihihhh") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"ihihhh\") expected 3");
            failed++;
        }

        // Test 7
        if (obj.countPairs("ihjxhh") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"ihjxhh\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.countPairs("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"\") expected 0");
            failed++;
        }

        // Test 9
        if (obj.countPairs("a") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"a\") expected 0");
            failed++;
        }

        // Test 10
        if (obj.countPairs("aa") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"aa\") expected 0");
            failed++;
        }

        // Test 11
        if (obj.countPairs("aaa") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countPairs(\"aaa\") expected 1");
            failed++;
        }

        System.out.println("countPairs: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}