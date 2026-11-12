package tn.esprit.exam_simulation.Config;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Contact;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.servers.Server;
import org.springframework.context.annotation.Configuration;

@Configuration
@OpenAPIDefinition(
        info = @Info(
                title = "Exam Simulation Service API",
                version = "1.0.0",
                description = """
                        **Microservice : Exam Simulation**

                        Ce service fait partie de la plateforme SpeakUp, dédiée à \
                        l'entraînement et à l'évaluation de l'expression orale.

                        Il est responsable de :
                        - la gestion des examens blancs, de leurs sections et de leurs questions
                        - le déroulement des passations (démarrer, répondre, soumettre)
                        - le chronométrage et l'expiration automatique des passations

                        Technologies : Spring Boot, Spring Data JPA, MySQL.
                        """,
                contact = @Contact(name = "Équipe SpeakUp")
        ),
        servers = @Server(url = "http://localhost:8084", description = "Serveur local")
)
public class Config {
}