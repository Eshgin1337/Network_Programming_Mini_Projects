package org.example.springprojg2;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.Arrays;

@SpringBootApplication
public class Springproj10Application implements CommandLineRunner {

	@Autowired
	private JdbcTemplate jdbcTemplate;

	public static void main(String[] args) {
		SpringApplication.run(Springproj10Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println(Arrays.toString(args));
	}
}
