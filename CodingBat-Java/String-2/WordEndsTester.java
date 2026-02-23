/**
 * Tester for WordEnds - CodingBat Java
 * 13 test cases
 */
public class WordEndsTester {

    public static void main(String[] args) {
        WordEnds obj = new WordEnds();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.wordEnds("abcXY123XYijk", "XY").equals("c13i")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abcXY123XYijk\", \"XY\") expected \"c13i\"");
            failed++;
        }

        // Test 2
        if (obj.wordEnds("XY123XY", "XY").equals("13")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"XY123XY\", \"XY\") expected \"13\"");
            failed++;
        }

        // Test 3
        if (obj.wordEnds("XY1XY", "XY").equals("11")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"XY1XY\", \"XY\") expected \"11\"");
            failed++;
        }

        // Test 4
        if (obj.wordEnds("XYXY", "XY").equals("XY")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"XYXY\", \"XY\") expected \"XY\"");
            failed++;
        }

        // Test 5
        if (obj.wordEnds("XY", "XY").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"XY\", \"XY\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.wordEnds("Hi", "XY").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"Hi\", \"XY\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.wordEnds("", "XY").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"\", \"XY\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.wordEnds("abc1xyz1i1j", "1").equals("cxziij")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abc1xyz1i1j\", \"1\") expected \"cxziij\"");
            failed++;
        }

        // Test 9
        if (obj.wordEnds("abc1xyz1", "1").equals("cxz")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abc1xyz1\", \"1\") expected \"cxz\"");
            failed++;
        }

        // Test 10
        if (obj.wordEnds("abc1xyz11", "1").equals("cxz11")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abc1xyz11\", \"1\") expected \"cxz11\"");
            failed++;
        }

        // Test 11
        if (obj.wordEnds("abc1xyz1abc", "abc").equals("11")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abc1xyz1abc\", \"abc\") expected \"11\"");
            failed++;
        }

        // Test 12
        if (obj.wordEnds("abc1xyz1abc", "b").equals("acac")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abc1xyz1abc\", \"b\") expected \"acac\"");
            failed++;
        }

        // Test 13
        if (obj.wordEnds("abc1abc1abc", "abc").equals("1111")) {
            passed++;
        } else {
            System.out.println("FAIL: wordEnds(\"abc1abc1abc\", \"abc\") expected \"1111\"");
            failed++;
        }

        System.out.println("wordEnds: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}