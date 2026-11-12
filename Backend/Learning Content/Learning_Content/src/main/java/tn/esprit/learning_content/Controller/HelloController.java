package tn.esprit.learning_content.Controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/Hello")
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello from my Learning Content Microservice!";
    }
}
