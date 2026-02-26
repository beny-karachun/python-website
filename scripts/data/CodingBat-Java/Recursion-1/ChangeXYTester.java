/**
 * Tester for ChangeXY - CodingBat Java
 * 10 test cases
 */
public class ChangeXYTester {

    public static void main(String[] args) {
        ChangeXY obj = new ChangeXY();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.changeXY("codex").equals("codey")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"codex\") expected \"codey\"");
            failed++;
        }

        // Test 2
        if (obj.changeXY("xxhixx").equals("yyhiyy")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"xxhixx\") expected \"yyhiyy\"");
            failed++;
        }

        // Test 3
        if (obj.changeXY("xhixhix").equals("yhiyhiy")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"xhixhix\") expected \"yhiyhiy\"");
            failed++;
        }

        // Test 4
        if (obj.changeXY("hiy").equals("hiy")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"hiy\") expected \"hiy\"");
            failed++;
        }

        // Test 5
        if (obj.changeXY("h").equals("h")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"h\") expected \"h\"");
            failed++;
        }

        // Test 6
        if (obj.changeXY("x").equals("y")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"x\") expected \"y\"");
            failed++;
        }

        // Test 7
        if (obj.changeXY("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.changeXY("xxx").equals("yyy")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"xxx\") expected \"yyy\"");
            failed++;
        }

        // Test 9
        if (obj.changeXY("yyhxyi").equals("yyhyyi")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"yyhxyi\") expected \"yyhyyi\"");
            failed++;
        }

        // Test 10
        if (obj.changeXY("hihi").equals("hihi")) {
            passed++;
        } else {
            System.out.println("FAIL: changeXY(\"hihi\") expected \"hihi\"");
            failed++;
        }

        System.out.println("changeXY: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}