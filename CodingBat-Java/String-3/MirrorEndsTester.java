/**
 * Tester for MirrorEnds - CodingBat Java
 * 11 test cases
 */
public class MirrorEndsTester {

    public static void main(String[] args) {
        MirrorEnds obj = new MirrorEnds();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.mirrorEnds("abXYZba").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"abXYZba\") expected \"ab\"");
            failed++;
        }

        // Test 2
        if (obj.mirrorEnds("abca").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"abca\") expected \"a\"");
            failed++;
        }

        // Test 3
        if (obj.mirrorEnds("aba").equals("aba")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"aba\") expected \"aba\"");
            failed++;
        }

        // Test 4
        if (obj.mirrorEnds("abab").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"abab\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.mirrorEnds("xxx").equals("xxx")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"xxx\") expected \"xxx\"");
            failed++;
        }

        // Test 6
        if (obj.mirrorEnds("xxYxx").equals("xxYxx")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"xxYxx\") expected \"xxYxx\"");
            failed++;
        }

        // Test 7
        if (obj.mirrorEnds("Hi and iH").equals("Hi ")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"Hi and iH\") expected \"Hi \"");
            failed++;
        }

        // Test 8
        if (obj.mirrorEnds("x").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"x\") expected \"x\"");
            failed++;
        }

        // Test 9
        if (obj.mirrorEnds("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.mirrorEnds("123and then 321").equals("123")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"123and then 321\") expected \"123\"");
            failed++;
        }

        // Test 11
        if (obj.mirrorEnds("band andab").equals("ba")) {
            passed++;
        } else {
            System.out.println("FAIL: mirrorEnds(\"band andab\") expected \"ba\"");
            failed++;
        }

        System.out.println("mirrorEnds: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}