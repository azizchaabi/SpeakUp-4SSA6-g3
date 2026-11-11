package com.speakup.oralpractice.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/Hello")
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello World";
    }
}