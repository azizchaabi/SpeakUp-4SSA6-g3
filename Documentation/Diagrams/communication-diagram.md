# Communication Diagram - SpeakUP Architecture

This document presents the global communication diagram and data flows between users, the Frontend interface, and the microservices of the **SpeakUP** platform.

---

## Visual Overview

![Communication Diagram](communication-diagram.png)

---

## Mermaid Diagram

```mermaid
flowchart TD
    User["Apprenant / Formateur"]
    Frontend["Frontend React"]
    LC["Learning Content"]
    OP["Oral Practice"]
    ES["Exam Simulation"]
    AI["AI Speech Analysis"]
    EF["Evaluation & Feedback"]
    PD["Progress & Dashboard"]

    User <-->|"Interaction"| Frontend

    %% Interactions Frontend to Microservices
    Frontend -->|"REST API"| LC
    Frontend -->|"REST API"| OP
    Frontend -->|"REST API"| ES
    Frontend -->|"REST API"| EF
    Frontend -->|"REST API"| PD

    %% Learning Content Flows
    LC -->|"Cours et exercices"| OP
    LC -->|"Contenu des examens"| ES

    %% Oral Practice Flows
    OP -->|"Audio enregistré"| AI
    OP -->|"Historique des séances"| PD

    %% Exam Simulation Flows
    ES -->|"Réponses orales"| AI
    ES -->|"Résultats de l'examen"| EF
    ES -->|"Historique des examens"| PD

    %% AI Speech Analysis Flows
    AI -->|"Résultats d'analyse"| EF

    %% Evaluation & Feedback Flows
    EF -->|"Notes et feedbacks"| PD

    %% Styles
    classDef actor fill:#e8f0fe,stroke:#4285f4,stroke-width:2px,color:#1a73e8;
    classDef ui fill:#e8f0fe,stroke:#4285f4,stroke-width:2px,color:#1a73e8;
    classDef service fill:#e8f0fe,stroke:#4285f4,stroke-width:1.5px,color:#1a73e8;

    class User actor;
    class Frontend ui;
    class LC,OP,ES,AI,EF,PD service;
```

---

## Flow Description

| Source | Destination | Flow / Description | Type |
|---|---|---|---|
| Apprenant / Formateur | Frontend React | Interaction utilisateur | UI |
| Frontend React | Learning Content, Oral Practice, Exam Simulation, Evaluation & Feedback, Progress & Dashboard | Requêtes d'affichage et d'actions | REST API |
| Learning Content | Oral Practice | Cours et exercices | Métier / Données |
| Learning Content | Exam Simulation | Contenu des examens | Métier / Données |
| Oral Practice | AI Speech Analysis | Audio enregistré | Flux Audio |
| Oral Practice | Progress & Dashboard | Historique des séances | Événement / Données |
| Exam Simulation | AI Speech Analysis | Réponses orales | Flux Audio |
| Exam Simulation | Evaluation & Feedback | Résultats de l'examen | Données d'examen |
| Exam Simulation | Progress & Dashboard | Historique des examens | Événement / Données |
| AI Speech Analysis | Evaluation & Feedback | Résultats d'analyse | Données d'analyse |
| Evaluation & Feedback | Progress & Dashboard | Notes et feedbacks | Métriques de progression |
