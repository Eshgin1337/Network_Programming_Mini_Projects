package com.example.gatlingproj;

import net.andreinc.mockneat.MockNeat;
import org.springframework.http.HttpStatus;
import org.springframework.util.MultiValueMap;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedWriter;

@RestController
public class AuthController {
    @Autowired
    Repository Repository;

    @GetMapping("/generate_mock_data")
    public List<String> mockData(@RequestParam Integer size) throws IOException {
        MockNeat mock = MockNeat.threadLocal();

        List<String> generator = mock.fmt("#{email},#{password}")
                .param("email", mock.emails())
                .param("password", mock.passwords())
                .list(size)
                .val();

        BufferedWriter writer = new BufferedWriter(new FileWriter(String.format("mock_data_%d.csv", size)));
        writer.write("email,password" + "\n");
        for (String row : generator) {
            writer.write(row + "\n");
        }
        writer.close();

        return generator;
    }

    @PostMapping("/register")
    public ResponseEntity<User> register(@RequestParam MultiValueMap<String,String> paramMap) {
        try {
            String email = paramMap.get("email").get(0);
            String password = paramMap.get("password").get(0);

            User user = new User(email, password);
            User addedUser = Repository.save(user);

            return ResponseEntity.status(HttpStatus.CREATED).body(addedUser);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
        }
    }
}
