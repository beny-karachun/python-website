/**
 * Tester for StartWord - CodingBat Java
 * 15 test cases
 */
public class StartWordTester {

    public static void main(String[] args) {
        StartWord obj = new StartWord();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.startWord("hippo", "hi").equals("hi")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"hi\") expected \"hi\"");
            failed++;
        }

        // Test 2
        if (obj.startWord("hippo", "xip").equals("hip")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"xip\") expected \"hip\"");
            failed++;
        }

        // Test 3
        if (obj.startWord("hippo", "i").equals("h")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"i\") expected \"h\"");
            failed++;
        }

        // Test 4
        if (obj.startWord("hippo", "ix").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"ix\") expected \"\"");
            failed++;
        }

        // Test 5
        if (obj.startWord("h", "ix").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"h\", \"ix\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.startWord("", "i").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"\", \"i\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.startWord("hip", "zi").equals("hi")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hip\", \"zi\") expected \"hi\"");
            failed++;
        }

        // Test 8
        if (obj.startWord("hip", "zip").equals("hip")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hip\", \"zip\") expected \"hip\"");
            failed++;
        }

        // Test 9
        if (obj.startWord("hip", "zig").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hip\", \"zig\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.startWord("h", "z").equals("h")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"h\", \"z\") expected \"h\"");
            failed++;
        }

        // Test 11
        if (obj.startWord("hippo", "xippo").equals("hippo")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"xippo\") expected \"hippo\"");
            failed++;
        }

        // Test 12
        if (obj.startWord("hippo", "xyz").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"xyz\") expected \"\"");
            failed++;
        }

        // Test 13
        if (obj.startWord("hippo", "hip").equals("hip")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"hippo\", \"hip\") expected \"hip\"");
            failed++;
        }

        // Test 14
        if (obj.startWord("kitten", "cit").equals("kit")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"kitten\", \"cit\") expected \"kit\"");
            failed++;
        }

        // Test 15
        if (obj.startWord("kit", "cit").equals("kit")) {
            passed++;
        } else {
            System.out.println("FAIL: startWord(\"kit\", \"cit\") expected \"kit\"");
            failed++;
        }

        System.out.println("startWord: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}