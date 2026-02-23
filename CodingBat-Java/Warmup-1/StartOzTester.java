/**
 * Tester for StartOz - CodingBat Java
 * 12 test cases
 */
public class StartOzTester {

    public static void main(String[] args) {
        StartOz obj = new StartOz();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.startOz("ozymandias").equals("oz")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"ozymandias\") expected \"oz\"");
            failed++;
        }

        // Test 2
        if (obj.startOz("bzoo").equals("z")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"bzoo\") expected \"z\"");
            failed++;
        }

        // Test 3
        if (obj.startOz("oxx").equals("o")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"oxx\") expected \"o\"");
            failed++;
        }

        // Test 4
        if (obj.startOz("oz").equals("oz")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"oz\") expected \"oz\"");
            failed++;
        }

        // Test 5
        if (obj.startOz("ounce").equals("o")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"ounce\") expected \"o\"");
            failed++;
        }

        // Test 6
        if (obj.startOz("o").equals("o")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"o\") expected \"o\"");
            failed++;
        }

        // Test 7
        if (obj.startOz("abc").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"abc\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.startOz("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.startOz("zoo").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"zoo\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.startOz("aztec").equals("z")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"aztec\") expected \"z\"");
            failed++;
        }

        // Test 11
        if (obj.startOz("zzzz").equals("z")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"zzzz\") expected \"z\"");
            failed++;
        }

        // Test 12
        if (obj.startOz("oznic").equals("oz")) {
            passed++;
        } else {
            System.out.println("FAIL: startOz(\"oznic\") expected \"oz\"");
            failed++;
        }

        System.out.println("startOz: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}