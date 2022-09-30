import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PermissionManagerTest {
    PermissionManager manager;

    @BeforeEach
    void setUp() {
        manager = new PermissionManager();
    }

    @Test
    @DisplayName("Permission management should work fine")
    void testPermissionCorrectness() {
        manager.set(PermissionLevel.ADMIN);
        assertEquals("ADMIN", manager.get(), "The manager should respond with " +
                "corresponding privilege");

        manager.set(PermissionLevel.DEVELOPER);
        assertEquals("DEVELOPER", manager.get(), "The manager should respond with " +
                "corresponding privilege");

        manager.set(PermissionLevel.USER);
        assertEquals("USER", manager.get(), "The manager should respond with " +
                "corresponding privilege");
    }
}