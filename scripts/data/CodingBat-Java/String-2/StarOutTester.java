/**
 * Tester for StarOut - CodingBat Java
 * 18 test cases
 */
public class StarOutTester {

    public static void main(String[] args) {
        StarOut obj = new StarOut();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.starOut("ab*cd").equals("ad")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"ab*cd\") expected \"ad\"");
            failed++;
        }

        // Test 2
        if (obj.starOut("ab**cd").equals("ad")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"ab**cd\") expected \"ad\"");
            failed++;
        }

        // Test 3
        if (obj.starOut("sm*eilly").equals("silly")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"sm*eilly\") expected \"silly\"");
            failed++;
        }

        // Test 4
        if (obj.starOut("sm*eil*ly").equals("siy")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"sm*eil*ly\") expected \"siy\"");
            failed++;
        }

        // Test 5
        if (obj.starOut("sm**eil*ly").equals("siy")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"sm**eil*ly\") expected \"siy\"");
            failed++;
        }

        // Test 6
        if (obj.starOut("sm***eil*ly").equals("siy")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"sm***eil*ly\") expected \"siy\"");
            failed++;
        }

        // Test 7
        if (obj.starOut("stringy*").equals("string")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"stringy*\") expected \"string\"");
            failed++;
        }

        // Test 8
        if (obj.starOut("*stringy").equals("tringy")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"*stringy\") expected \"tringy\"");
            failed++;
        }

        // Test 9
        if (obj.starOut("*str*in*gy").equals("ty")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"*str*in*gy\") expected \"ty\"");
            failed++;
        }

        // Test 10
        if (obj.starOut("abc").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"abc\") expected \"abc\"");
            failed++;
        }

        // Test 11
        if (obj.starOut("a*bc").equals("c")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"a*bc\") expected \"c\"");
            failed++;
        }

        // Test 12
        if (obj.starOut("ab").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"ab\") expected \"ab\"");
            failed++;
        }

        // Test 13
        if (obj.starOut("a*b").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"a*b\") expected \"\"");
            failed++;
        }

        // Test 14
        if (obj.starOut("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"a\") expected \"a\"");
            failed++;
        }

        // Test 15
        if (obj.starOut("a*").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"a*\") expected \"\"");
            failed++;
        }

        // Test 16
        if (obj.starOut("*a").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"*a\") expected \"\"");
            failed++;
        }

        // Test 17
        if (obj.starOut("*").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"*\") expected \"\"");
            failed++;
        }

        // Test 18
        if (obj.starOut("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: starOut(\"\") expected \"\"");
            failed++;
        }

        System.out.println("starOut: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}