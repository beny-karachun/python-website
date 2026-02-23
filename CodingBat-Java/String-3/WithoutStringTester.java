/**
 * Tester for WithoutString - CodingBat Java
 * 19 test cases
 */
public class WithoutStringTester {

    public static void main(String[] args) {
        WithoutString obj = new WithoutString();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.withoutString("Hello there", "llo").equals("He there")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"Hello there\", \"llo\") expected \"He there\"");
            failed++;
        }

        // Test 2
        if (obj.withoutString("Hello there", "e").equals("Hllo thr")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"Hello there\", \"e\") expected \"Hllo thr\"");
            failed++;
        }

        // Test 3
        if (obj.withoutString("Hello there", "x").equals("Hello there")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"Hello there\", \"x\") expected \"Hello there\"");
            failed++;
        }

        // Test 4
        if (obj.withoutString("This is a FISH", "IS").equals("Th  a FH")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"This is a FISH\", \"IS\") expected \"Th  a FH\"");
            failed++;
        }

        // Test 5
        if (obj.withoutString("THIS is a FISH", "is").equals("TH  a FH")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"THIS is a FISH\", \"is\") expected \"TH  a FH\"");
            failed++;
        }

        // Test 6
        if (obj.withoutString("THIS is a FISH", "iS").equals("TH  a FH")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"THIS is a FISH\", \"iS\") expected \"TH  a FH\"");
            failed++;
        }

        // Test 7
        if (obj.withoutString("abxxxxab", "xx").equals("abab")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"abxxxxab\", \"xx\") expected \"abab\"");
            failed++;
        }

        // Test 8
        if (obj.withoutString("abxxxab", "xx").equals("abxab")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"abxxxab\", \"xx\") expected \"abxab\"");
            failed++;
        }

        // Test 9
        if (obj.withoutString("abxxxab", "x").equals("abab")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"abxxxab\", \"x\") expected \"abab\"");
            failed++;
        }

        // Test 10
        if (obj.withoutString("xxx", "x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"xxx\", \"x\") expected \"\"");
            failed++;
        }

        // Test 11
        if (obj.withoutString("xxx", "xx").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"xxx\", \"xx\") expected \"x\"");
            failed++;
        }

        // Test 12
        if (obj.withoutString("xyzzy", "Y").equals("xzz")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"xyzzy\", \"Y\") expected \"xzz\"");
            failed++;
        }

        // Test 13
        if (obj.withoutString("", "x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"\", \"x\") expected \"\"");
            failed++;
        }

        // Test 14
        if (obj.withoutString("abcabc", "b").equals("acac")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"abcabc\", \"b\") expected \"acac\"");
            failed++;
        }

        // Test 15
        if (obj.withoutString("AA22bb", "2").equals("AAbb")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"AA22bb\", \"2\") expected \"AAbb\"");
            failed++;
        }

        // Test 16
        if (obj.withoutString("1111", "1").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"1111\", \"1\") expected \"\"");
            failed++;
        }

        // Test 17
        if (obj.withoutString("1111", "11").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"1111\", \"11\") expected \"\"");
            failed++;
        }

        // Test 18
        if (obj.withoutString("MkjtMkx", "Mk").equals("jtx")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"MkjtMkx\", \"Mk\") expected \"jtx\"");
            failed++;
        }

        // Test 19
        if (obj.withoutString("Hi HoHo", "Ho").equals("Hi ")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutString(\"Hi HoHo\", \"Ho\") expected \"Hi \"");
            failed++;
        }

        System.out.println("withoutString: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}