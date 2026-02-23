/**
 * Tester for SameEnds - CodingBat Java
 * 12 test cases
 */
public class SameEndsTester {

    public static void main(String[] args) {
        SameEnds obj = new SameEnds();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sameEnds("abXYab").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"abXYab\") expected \"ab\"");
            failed++;
        }

        // Test 2
        if (obj.sameEnds("xx").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"xx\") expected \"x\"");
            failed++;
        }

        // Test 3
        if (obj.sameEnds("xxx").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"xxx\") expected \"x\"");
            failed++;
        }

        // Test 4
        if (obj.sameEnds("xxxx").equals("xx")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"xxxx\") expected \"xx\"");
            failed++;
        }

        // Test 5
        if (obj.sameEnds("javaXYZjava").equals("java")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"javaXYZjava\") expected \"java\"");
            failed++;
        }

        // Test 6
        if (obj.sameEnds("javajava").equals("java")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"javajava\") expected \"java\"");
            failed++;
        }

        // Test 7
        if (obj.sameEnds("xavaXYZjava").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"xavaXYZjava\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.sameEnds("Hello! and Hello!").equals("Hello!")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"Hello! and Hello!\") expected \"Hello!\"");
            failed++;
        }

        // Test 9
        if (obj.sameEnds("x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"x\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.sameEnds("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"\") expected \"\"");
            failed++;
        }

        // Test 11
        if (obj.sameEnds("abcb").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"abcb\") expected \"\"");
            failed++;
        }

        // Test 12
        if (obj.sameEnds("mymmy").equals("my")) {
            passed++;
        } else {
            System.out.println("FAIL: sameEnds(\"mymmy\") expected \"my\"");
            failed++;
        }

        System.out.println("sameEnds: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}