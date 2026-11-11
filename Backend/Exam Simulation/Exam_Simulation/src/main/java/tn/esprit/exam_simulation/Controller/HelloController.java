
package tn.esprit.exam_simulation.Controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/api/Hello")
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello from my Exam Simulation!";
    }
}
