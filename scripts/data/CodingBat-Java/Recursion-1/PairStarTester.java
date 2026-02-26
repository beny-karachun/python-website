/**
 * Tester for PairStar - CodingBat Java
 * 10 test cases
 */
public class PairStarTester {

    public static void main(String[] args) {
        PairStar obj = new PairStar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.pairStar("hello").equals("hel*lo")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"hello\") expected \"hel*lo\"");
            failed++;
        }

        // Test 2
        if (obj.pairStar("xxyy").equals("x*xy*y")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"xxyy\") expected \"x*xy*y\"");
            failed++;
        }

        // Test 3
        if (obj.pairStar("aaaa").equals("a*a*a*a")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"aaaa\") expected \"a*a*a*a\"");
            failed++;
        }

        // Test 4
        if (obj.pairStar("aaab").equals("a*a*ab")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"aaab\") expected \"a*a*ab\"");
            failed++;
        }

        // Test 5
        if (obj.pairStar("aa").equals("a*a")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"aa\") expected \"a*a\"");
            failed++;
        }

        // Test 6
        if (obj.pairStar("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"a\") expected \"a\"");
            failed++;
        }

        // Test 7
        if (obj.pairStar("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.pairStar("noadjacent").equals("noadjacent")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"noadjacent\") expected \"noadjacent\"");
            failed++;
        }

        // Test 9
        if (obj.pairStar("abba").equals("ab*ba")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"abba\") expected \"ab*ba\"");
            failed++;
        }

        // Test 10
        if (obj.pairStar("abbba").equals("ab*b*ba")) {
            passed++;
        } else {
            System.out.println("FAIL: pairStar(\"abbba\") expected \"ab*b*ba\"");
            failed++;
        }

        System.out.println("pairStar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}