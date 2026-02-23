/**
 * Tester for ConCat - CodingBat Java
 * 6 test cases
 */
public class ConCatTester {

    public static void main(String[] args) {
        ConCat obj = new ConCat();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.conCat("abc", "cat").equals("abcat")) {
            passed++;
        } else {
            System.out.println("FAIL: conCat(\"abc\", \"cat\") expected \"abcat\"");
            failed++;
        }

        // Test 2
        if (obj.conCat("dog", "cat").equals("dogcat")) {
            passed++;
        } else {
            System.out.println("FAIL: conCat(\"dog\", \"cat\") expected \"dogcat\"");
            failed++;
        }

        // Test 3
        if (obj.conCat("abc", "").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: conCat(\"abc\", \"\") expected \"abc\"");
            failed++;
        }

        // Test 4
        if (obj.conCat("", "cat").equals("cat")) {
            passed++;
        } else {
            System.out.println("FAIL: conCat(\"\", \"cat\") expected \"cat\"");
            failed++;
        }

        // Test 5
        if (obj.conCat("pig", "g").equals("pig")) {
            passed++;
        } else {
            System.out.println("FAIL: conCat(\"pig\", \"g\") expected \"pig\"");
            failed++;
        }

        // Test 6
        if (obj.conCat("pig", "doggy").equals("pigdoggy")) {
            passed++;
        } else {
            System.out.println("FAIL: conCat(\"pig\", \"doggy\") expected \"pigdoggy\"");
            failed++;
        }

        System.out.println("conCat: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}