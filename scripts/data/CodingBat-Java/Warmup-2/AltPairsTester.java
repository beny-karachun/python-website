/**
 * Tester for AltPairs - CodingBat Java
 * 8 test cases
 */
public class AltPairsTester {

    public static void main(String[] args) {
        AltPairs obj = new AltPairs();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.altPairs("kitten").equals("kien")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"kitten\") expected \"kien\"");
            failed++;
        }

        // Test 2
        if (obj.altPairs("Chocolate").equals("Chole")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"Chocolate\") expected \"Chole\"");
            failed++;
        }

        // Test 3
        if (obj.altPairs("CodingHorror").equals("Congrr")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"CodingHorror\") expected \"Congrr\"");
            failed++;
        }

        // Test 4
        if (obj.altPairs("yak").equals("ya")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"yak\") expected \"ya\"");
            failed++;
        }

        // Test 5
        if (obj.altPairs("ya").equals("ya")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"ya\") expected \"ya\"");
            failed++;
        }

        // Test 6
        if (obj.altPairs("y").equals("y")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"y\") expected \"y\"");
            failed++;
        }

        // Test 7
        if (obj.altPairs("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.altPairs("ThisThatTheOther").equals("ThThThth")) {
            passed++;
        } else {
            System.out.println("FAIL: altPairs(\"ThisThatTheOther\") expected \"ThThThth\"");
            failed++;
        }

        System.out.println("altPairs: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}