/**
 * Tester for MakeTags - CodingBat Java
 * 7 test cases
 */
public class MakeTagsTester {

    public static void main(String[] args) {
        MakeTags obj = new MakeTags();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.makeTags("i", "Yay").equals("<i>Yay</i>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"i\", \"Yay\") expected \"<i>Yay</i>\"");
            failed++;
        }

        // Test 2
        if (obj.makeTags("i", "Hello").equals("<i>Hello</i>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"i\", \"Hello\") expected \"<i>Hello</i>\"");
            failed++;
        }

        // Test 3
        if (obj.makeTags("cite", "Yay").equals("<cite>Yay</cite>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"cite\", \"Yay\") expected \"<cite>Yay</cite>\"");
            failed++;
        }

        // Test 4
        if (obj.makeTags("address", "here").equals("<address>here</address>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"address\", \"here\") expected \"<address>here</address>\"");
            failed++;
        }

        // Test 5
        if (obj.makeTags("body", "Heart").equals("<body>Heart</body>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"body\", \"Heart\") expected \"<body>Heart</body>\"");
            failed++;
        }

        // Test 6
        if (obj.makeTags("i", "i").equals("<i>i</i>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"i\", \"i\") expected \"<i>i</i>\"");
            failed++;
        }

        // Test 7
        if (obj.makeTags("i", "").equals("<i></i>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeTags(\"i\", \"\") expected \"<i></i>\"");
            failed++;
        }

        System.out.println("makeTags: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}