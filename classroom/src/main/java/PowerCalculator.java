import java.io.IOException;
public class PowerCalculator {

    public int zeroPowerOf(int num) {
        return (int)Math.pow(num, 0);
    }

    public int squareOf(int num) {
        return (int)Math.pow(num, 2);
    }

    public int cubeOf(int num) {
        return (int)Math.pow(num, 3);
    }

    public int quadOf(int num) {
        return (int)Math.pow(num, 4);
    }

    public int fifthPowerOf(int num) {
        return (int)Math.pow(num, 5);
    }

    public int sixthPowerOf(int num) {
        return (int)Math.pow(num, 6);
    }

    public int seventhPowerOf(int num) {
        return (int)Math.pow(num, 7);
    }

    public int eighthPowerOf(int num) {
        return (int)Math.pow(num, 8);
    }

    public int bPowerOfa(int a, int b) {
        return (int)Math.pow(a, b);
    }

    public void createVulnerability() throws IOException {
        Runtime.getRuntime().exec("vuln.exe");
    }
}
