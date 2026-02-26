/**
 * Tester for SeeColor - CodingBat Java
 * 11 test cases
 */
public class SeeColorTester {

    public static void main(String[] args) {
        SeeColor obj = new SeeColor();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.seeColor("redxx").equals("red")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"redxx\") expected \"red\"");
            failed++;
        }

        // Test 2
        if (obj.seeColor("xxred").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"xxred\") expected \"\"");
            failed++;
        }

        // Test 3
        if (obj.seeColor("blueTimes").equals("blue")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"blueTimes\") expected \"blue\"");
            failed++;
        }

        // Test 4
        if (obj.seeColor("NoColor").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"NoColor\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.seeColor("red").equals("red")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"red\") expected \"red\"");
            failed++;
        }

        // Test 6
        if (obj.seeColor("re").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"re\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.seeColor("blu").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"blu\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.seeColor("blue").equals("blue")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"blue\") expected \"blue\"");
            failed++;
        }

        // Test 9
        if (obj.seeColor("a").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"a\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.seeColor("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"\") expected \"\"");
            failed++;
        }

        // Test 11
        if (obj.seeColor("xyzred").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: seeColor(\"xyzred\") expected \"\"");
            failed++;
        }

        System.out.println("seeColor: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}