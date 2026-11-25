package tn.esprit.exam_simulation;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class ExamSimulationApplication {

    public static void main(String[] args) {
        SpringApplication.run(ExamSimulationApplication.class, args);
    }

}
