/**
 * Tester for EndsLy - CodingBat Java
 * 9 test cases
 */
public class EndsLyTester {

    public static void main(String[] args) {
        EndsLy obj = new EndsLy();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.endsLy("oddly") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"oddly\") expected true");
            failed++;
        }

        // Test 2
        if (obj.endsLy("y") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"y\") expected false");
            failed++;
        }

        // Test 3
        if (obj.endsLy("oddy") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"oddy\") expected false");
            failed++;
        }

        // Test 4
        if (obj.endsLy("oddl") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"oddl\") expected false");
            failed++;
        }

        // Test 5
        if (obj.endsLy("olydd") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"olydd\") expected false");
            failed++;
        }

        // Test 6
        if (obj.endsLy("ly") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"ly\") expected true");
            failed++;
        }

        // Test 7
        if (obj.endsLy("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"\") expected false");
            failed++;
        }

        // Test 8
        if (obj.endsLy("falsey") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"falsey\") expected false");
            failed++;
        }

        // Test 9
        if (obj.endsLy("evenly") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endsLy(\"evenly\") expected true");
            failed++;
        }

        System.out.println("endsLy: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}