import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.concurrent.ExecutionException;

import static org.junit.jupiter.api.Assertions.*;

public class PowerCalculatorTest {
    PowerCalculator calculator;

    @BeforeEach
    void setup(){
        calculator = new PowerCalculator();
    }

    @Test
    @DisplayName("Zero power of any number should be zero")
    void testZeroPower() {
        assertEquals(1, calculator.zeroPowerOf(3));
        assertEquals(1, calculator.zeroPowerOf(2));
        assertEquals(1, calculator.zeroPowerOf(643));
    }

    @Test
    @DisplayName("Square of a number should be equal to its multiplication with itself")
    void testSquare() {
        assertEquals(4, calculator.squareOf(2));
        assertEquals(9, calculator.squareOf(3));
    }

    @Test
    @DisplayName("Cube of any number should be equal to its multiplication with its square")
    void testCube() {
        assertEquals(8, calculator.cubeOf(2));
        assertEquals(64, calculator.cubeOf(4));
    }

    @Test
    @DisplayName("b power of a should be equal to a multiplied with itself for b times")
    void testPowerOfTwoNumbers() {
        assertEquals(8, calculator.bPowerOfa(2, 3));
        assertEquals(64, calculator.bPowerOfa(4, 3));
    }

    @Test
    @DisplayName("Negative numbers cannot have square root")
    void testQuad() {
        assertEquals(16, calculator.quadOf(2));
        assertEquals(256, calculator.quadOf(4));
    }
}
