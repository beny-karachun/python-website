/**
 * Tester for StringSplosion - CodingBat Java
 * 10 test cases
 */
public class StringSplosionTester {

    public static void main(String[] args) {
        StringSplosion obj = new StringSplosion();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringSplosion("Code").equals("CCoCodCode")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"Code\") expected \"CCoCodCode\"");
            failed++;
        }

        // Test 2
        if (obj.stringSplosion("abc").equals("aababc")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"abc\") expected \"aababc\"");
            failed++;
        }

        // Test 3
        if (obj.stringSplosion("ab").equals("aab")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"ab\") expected \"aab\"");
            failed++;
        }

        // Test 4
        if (obj.stringSplosion("x").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"x\") expected \"x\"");
            failed++;
        }

        // Test 5
        if (obj.stringSplosion("fade").equals("ffafadfade")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"fade\") expected \"ffafadfade\"");
            failed++;
        }

        // Test 6
        if (obj.stringSplosion("There").equals("TThTheTherThere")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"There\") expected \"TThTheTherThere\"");
            failed++;
        }

        // Test 7
        if (obj.stringSplosion("Kitten").equals("KKiKitKittKitteKitten")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"Kitten\") expected \"KKiKitKittKitteKitten\"");
            failed++;
        }

        // Test 8
        if (obj.stringSplosion("Bye").equals("BByBye")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"Bye\") expected \"BByBye\"");
            failed++;
        }

        // Test 9
        if (obj.stringSplosion("Good").equals("GGoGooGood")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"Good\") expected \"GGoGooGood\"");
            failed++;
        }

        // Test 10
        if (obj.stringSplosion("Bad").equals("BBaBad")) {
            passed++;
        } else {
            System.out.println("FAIL: stringSplosion(\"Bad\") expected \"BBaBad\"");
            failed++;
        }

        System.out.println("stringSplosion: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}