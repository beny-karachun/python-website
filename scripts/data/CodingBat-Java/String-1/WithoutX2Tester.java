/**
 * Tester for WithoutX2 - CodingBat Java
 * 12 test cases
 */
public class WithoutX2Tester {

    public static void main(String[] args) {
        WithoutX2 obj = new WithoutX2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.withoutX2("xHi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"xHi\") expected \"Hi\"");
            failed++;
        }

        // Test 2
        if (obj.withoutX2("Hxi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"Hxi\") expected \"Hi\"");
            failed++;
        }

        // Test 3
        if (obj.withoutX2("Hi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"Hi\") expected \"Hi\"");
            failed++;
        }

        // Test 4
        if (obj.withoutX2("xxHi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"xxHi\") expected \"Hi\"");
            failed++;
        }

        // Test 5
        if (obj.withoutX2("Hix").equals("Hix")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"Hix\") expected \"Hix\"");
            failed++;
        }

        // Test 6
        if (obj.withoutX2("xaxb").equals("axb")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"xaxb\") expected \"axb\"");
            failed++;
        }

        // Test 7
        if (obj.withoutX2("xx").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"xx\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.withoutX2("x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"x\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.withoutX2("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.withoutX2("Hello").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"Hello\") expected \"Hello\"");
            failed++;
        }

        // Test 11
        if (obj.withoutX2("Hexllo").equals("Hexllo")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"Hexllo\") expected \"Hexllo\"");
            failed++;
        }

        // Test 12
        if (obj.withoutX2("xHxllo").equals("Hxllo")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX2(\"xHxllo\") expected \"Hxllo\"");
            failed++;
        }

        System.out.println("withoutX2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}