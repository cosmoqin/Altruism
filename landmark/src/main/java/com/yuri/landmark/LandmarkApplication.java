package com.yuri.landmark;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class LandmarkApplication {

	public static void main(String[] args) {
		System.out.println("LandmarkApplication.main()");
		SpringApplication.run(LandmarkApplication.class, args);
	}

}
