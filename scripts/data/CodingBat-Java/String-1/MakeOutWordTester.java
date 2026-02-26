/**
 * Tester for MakeOutWord - CodingBat Java
 * 5 test cases
 */
public class MakeOutWordTester {

    public static void main(String[] args) {
        MakeOutWord obj = new MakeOutWord();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.makeOutWord("<<>>", "Yay").equals("<<Yay>>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeOutWord(\"<<>>\", \"Yay\") expected \"<<Yay>>\"");
            failed++;
        }

        // Test 2
        if (obj.makeOutWord("<<>>", "WooHoo").equals("<<WooHoo>>")) {
            passed++;
        } else {
            System.out.println("FAIL: makeOutWord(\"<<>>\", \"WooHoo\") expected \"<<WooHoo>>\"");
            failed++;
        }

        // Test 3
        if (obj.makeOutWord("[[]]", "word").equals("[[word]]")) {
            passed++;
        } else {
            System.out.println("FAIL: makeOutWord(\"[[]]\", \"word\") expected \"[[word]]\"");
            failed++;
        }

        // Test 4
        if (obj.makeOutWord("HHoo", "Hello").equals("HHHellooo")) {
            passed++;
        } else {
            System.out.println("FAIL: makeOutWord(\"HHoo\", \"Hello\") expected \"HHHellooo\"");
            failed++;
        }

        // Test 5
        if (obj.makeOutWord("abyz", "YAY").equals("abYAYyz")) {
            passed++;
        } else {
            System.out.println("FAIL: makeOutWord(\"abyz\", \"YAY\") expected \"abYAYyz\"");
            failed++;
        }

        System.out.println("makeOutWord: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}