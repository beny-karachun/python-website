/**
 * Tester for AnswerCell - CodingBat Java
 * 6 test cases
 */
public class AnswerCellTester {

    public static void main(String[] args) {
        AnswerCell obj = new AnswerCell();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.answerCell(false, false, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: answerCell(false, false, false) expected true");
            failed++;
        }

        // Test 2
        if (obj.answerCell(false, false, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: answerCell(false, false, true) expected false");
            failed++;
        }

        // Test 3
        if (obj.answerCell(true, false, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: answerCell(true, false, false) expected false");
            failed++;
        }

        // Test 4
        if (obj.answerCell(true, true, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: answerCell(true, true, false) expected true");
            failed++;
        }

        // Test 5
        if (obj.answerCell(false, true, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: answerCell(false, true, false) expected true");
            failed++;
        }

        // Test 6
        if (obj.answerCell(true, true, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: answerCell(true, true, true) expected false");
            failed++;
        }

        System.out.println("answerCell: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}