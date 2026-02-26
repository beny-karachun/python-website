/**
 * Tester for StringE - CodingBat Java
 * 6 test cases
 */
public class StringETester {

    public static void main(String[] args) {
        StringE obj = new StringE();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringE("Hello") == true) {
            passed++;
        } else {
            System.out.println("FAIL: stringE(\"Hello\") expected true");
            failed++;
        }

        // Test 2
        if (obj.stringE("Heelle") == true) {
            passed++;
        } else {
            System.out.println("FAIL: stringE(\"Heelle\") expected true");
            failed++;
        }

        // Test 3
        if (obj.stringE("Heelele") == false) {
            passed++;
        } else {
            System.out.println("FAIL: stringE(\"Heelele\") expected false");
            failed++;
        }

        // Test 4
        if (obj.stringE("Hll") == false) {
            passed++;
        } else {
            System.out.println("FAIL: stringE(\"Hll\") expected false");
            failed++;
        }

        // Test 5
        if (obj.stringE("e") == true) {
            passed++;
        } else {
            System.out.println("FAIL: stringE(\"e\") expected true");
            failed++;
        }

        // Test 6
        if (obj.stringE("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: stringE(\"\") expected false");
            failed++;
        }

        System.out.println("stringE: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}