/**
 * Tester for PlusOut - CodingBat Java
 * 10 test cases
 */
public class PlusOutTester {

    public static void main(String[] args) {
        PlusOut obj = new PlusOut();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.plusOut("12xy34", "xy").equals("++xy++")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"12xy34\", \"xy\") expected \"++xy++\"");
            failed++;
        }

        // Test 2
        if (obj.plusOut("12xy34", "1").equals("1+++++")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"12xy34\", \"1\") expected \"1+++++\"");
            failed++;
        }

        // Test 3
        if (obj.plusOut("12xy34xyabcxy", "xy").equals("++xy++xy+++xy")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"12xy34xyabcxy\", \"xy\") expected \"++xy++xy+++xy\"");
            failed++;
        }

        // Test 4
        if (obj.plusOut("abXYabcXYZ", "ab").equals("ab++ab++++")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"abXYabcXYZ\", \"ab\") expected \"ab++ab++++\"");
            failed++;
        }

        // Test 5
        if (obj.plusOut("abXYabcXYZ", "abc").equals("++++abc+++")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"abXYabcXYZ\", \"abc\") expected \"++++abc+++\"");
            failed++;
        }

        // Test 6
        if (obj.plusOut("abXYabcXYZ", "XY").equals("++XY+++XY+")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"abXYabcXYZ\", \"XY\") expected \"++XY+++XY+\"");
            failed++;
        }

        // Test 7
        if (obj.plusOut("abXYxyzXYZ", "XYZ").equals("+++++++XYZ")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"abXYxyzXYZ\", \"XYZ\") expected \"+++++++XYZ\"");
            failed++;
        }

        // Test 8
        if (obj.plusOut("--++ab", "++").equals("++++++")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"--++ab\", \"++\") expected \"++++++\"");
            failed++;
        }

        // Test 9
        if (obj.plusOut("aaxxxxbb", "xx").equals("++xxxx++")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"aaxxxxbb\", \"xx\") expected \"++xxxx++\"");
            failed++;
        }

        // Test 10
        if (obj.plusOut("123123", "3").equals("++3++3")) {
            passed++;
        } else {
            System.out.println("FAIL: plusOut(\"123123\", \"3\") expected \"++3++3\"");
            failed++;
        }

        System.out.println("plusOut: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}