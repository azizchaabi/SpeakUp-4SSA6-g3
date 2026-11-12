# Diagramme de Communication - Architecture SpeakUP

Ce document présente le diagramme de communication global et les flux d'échanges entre l'utilisateur, l'interface utilisateur (Frontend) et les différents microservices du projet **SpeakUP**.

---

## Aperçu Visuel

![Diagramme de Communication SpeakUP](diagramme-de-communication.png)

---

## Diagramme Mermaid

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

    %% Interactions Frontend vers Microservices
    Frontend -->|"REST API"| LC
    Frontend -->|"REST API"| OP
    Frontend -->|"REST API"| ES
    Frontend -->|"REST API"| EF
    Frontend -->|"REST API"| PD

    %% Flux Learning Content
    LC -->|"Cours et exercices"| OP
    LC -->|"Contenu des examens"| ES

    %% Flux Oral Practice
    OP -->|"Audio enregistré"| AI
    OP -->|"Historique des séances"| PD

    %% Flux Exam Simulation
    ES -->|"Réponses orales"| AI
    ES -->|"Résultats de l'examen"| EF
    ES -->|"Historique des examens"| PD

    %% Flux AI Speech Analysis
    AI -->|"Résultats d'analyse"| EF

    %% Flux Evaluation & Feedback
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

## Description des Composants et des Flux

### 1. Acteurs et Interface
- **Apprenant / Formateur** : Utilisateurs finaux qui interagissent avec l'application web pour s'entraîner, passer des examens oraux ou consulter les résultats.
- **Frontend React** : Point d'accès interactif permettant la saisie utilisateur, l'enregistrement vocal et la restitution visuelle des feedbacks et tableaux de bord. Communique via des API REST avec les microservices métier.

### 2. Microservices Métier
| Microservice | Rôle | Échanges Entrants | Échanges Sortants |
|---|---|---|---|
| **Learning Content** | Fournit les cours, thèmes d'entraînement et sujets d'examens. | `REST API` (Frontend) | `Cours et exercices` → Oral Practice<br>`Contenu des examens` → Exam Simulation |
| **Oral Practice** | Gère les sessions libres et guidées d'expression orale. | `REST API` (Frontend)<br>`Cours et exercices` (Learning Content) | `Audio enregistré` → AI Speech Analysis<br>`Historique des séances` → Progress & Dashboard |
| **Exam Simulation** | Orchestre les simulations d'épreuves orales CECRL en temps limité. | `REST API` (Frontend)<br>`Contenu des examens` (Learning Content) | `Réponses orales` → AI Speech Analysis<br>`Résultats de l'examen` → Evaluation & Feedback<br>`Historique des examens` → Progress & Dashboard |
| **AI Speech Analysis** | Réalise la transcription (STT) et l'analyse acoustique/linguistique (fluidité, prononciation, grammaire). | `Audio enregistré` (Oral Practice)<br>`Réponses orales` (Exam Simulation) | `Résultats d'analyse` → Evaluation & Feedback |
| **Evaluation & Feedback** | Consolide les métriques d'analyse et génère les notations et recommandations pédagogiques. | `REST API` (Frontend)<br>`Résultats d'analyse` (AI Speech Analysis)<br>`Résultats de l'examen` (Exam Simulation) | `Notes et feedbacks` → Progress & Dashboard |
| **Progress & Dashboard** | Centralise et agrège les indicateurs de suivi et la progression de l'apprenant. | `REST API` (Frontend)<br>`Historique des séances` (Oral Practice)<br>`Notes et feedbacks` (Evaluation & Feedback)<br>`Historique des examens` (Exam Simulation) | Restitution des tableaux de bord vers le Frontend via `REST API` |
