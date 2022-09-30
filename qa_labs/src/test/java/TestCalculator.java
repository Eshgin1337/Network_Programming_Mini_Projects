import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

public class TestCalculator {
    Calculator calculator;

    @BeforeEach
    void createCalculation() {
        calculator = new Calculator();
    }

    @Test
    @DisplayName("Summation should work fine")
    void testSum() {
        assertEquals(13, calculator.add(4, 9), "Regular summation should work");
    }

    @RepeatedTest(5)
    @DisplayName("Ensure if b is negative of a the result will be zero")
    void testSummingNegative() {
        assertEquals(0, calculator.add(-5, 5), "Summing with its negative should be zero");
        assertEquals(0, calculator.add(5, -5), "Summing with its negative should be zero");
    }
}
