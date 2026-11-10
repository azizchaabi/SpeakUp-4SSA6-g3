# SpeakUP

**Plateforme intelligente d'entraînement et d'évaluation de l'expression
orale en français et en anglais**

SpeakUP est une application web distribuée qui aide les apprenants à
améliorer leur expression orale grâce à des entraînements réguliers, à
l'analyse de leurs prises de parole par l'intelligence artificielle et à
des simulations d'épreuves alignées sur le Cadre européen commun de
référence pour les langues (CECRL).

La plateforme cible les niveaux **B1 à C2** et prend en charge **le
français et l'anglais**.

> **Projet académique --- Module AWD (Architecture Web Distribuée),
> année universitaire 2026--2027.**

------------------------------------------------------------------------

## 1. Problématique et vision

L'expression orale est essentielle dans l'apprentissage d'une langue,
mais les occasions de pratiquer et de recevoir un retour personnalisé
peuvent être limitées. SpeakUP vise à permettre à chaque apprenant de
s'enregistrer, de s'entraîner à son rythme et de recevoir un retour
structuré sur sa prestation.

La plateforme fournit également aux formateurs des outils pour suivre
leurs groupes, examiner les résultats générés automatiquement et ajouter
leurs propres commentaires. L'évaluation par l'IA constitue une aide à
la pédagogie : elle ne remplace pas la décision du formateur.

## 2. Objectifs

-   Permettre l'entraînement oral en français et en anglais.
-   Proposer des activités adaptées aux niveaux B1, B2, C1 et C2.
-   Transcrire les enregistrements vocaux.
-   Analyser plusieurs dimensions de la prise de parole : prononciation,
    fluidité, intonation, lexique, grammaire et cohérence.
-   Fournir un feedback et des pistes d'amélioration.
-   Simuler des épreuves orales et suivre la progression des apprenants.
-   Donner aux formateurs une visibilité sur les résultats de leurs
    groupes.

## 3. Publics cibles et acteurs

  -----------------------------------------------------------------------
  Acteur                              Rôle dans la plateforme
  ----------------------------------- -----------------------------------
  Apprenant                           Choisit une langue et un niveau,
                                      réalise des exercices, enregistre
                                      ses réponses et consulte ses
                                      résultats.

  Formateur                           Crée ou suit des parcours, consulte
                                      les prestations, ajuste si
                                      nécessaire les évaluations et
                                      ajoute des commentaires.

  Établissement                       Pilote plusieurs classes, consulte
                                      des indicateurs agrégés et peut
                                      délivrer des attestations internes.
  -----------------------------------------------------------------------

## 4. Fonctionnalités principales

### 4.1 Enregistrement et analyse vocale

-   Enregistrement depuis le navigateur.
-   Transcription de la parole en texte (Speech-to-Text).
-   Analyse de la prononciation, du débit, des pauses et des
    hésitations.

### 4.2 Correction et feedback personnalisé

-   Repérage des erreurs grammaticales.
-   Analyse de la richesse et de la précision du vocabulaire.
-   Commentaires sur l'intonation et la fluidité.
-   Suggestions de reformulation et d'exercices ciblés.

### 4.3 Simulations d'examens oraux

-   Choix de la langue, de la certification et du niveau visé.
-   Sujet et temps de préparation.
-   Monologue et interaction avec des questions de relance.
-   Résultat estimé selon une grille inspirée des descripteurs du CECRL.

### 4.4 Suivi et tableaux de bord

-   Historique des entraînements et des résultats.
-   Évolution des scores par critère.
-   Visualisation de la progression vers le niveau cible.
-   Suivi des groupes par les formateurs.

## 5. Niveaux et langues pris en charge

  -----------------------------------------------------------------------
  Niveau                              Compétences orales visées
  ----------------------------------- -----------------------------------
  B1                                  Raconter une expérience, décrire un
                                      projet et donner un avis simple en
                                      le justifiant.

  B2                                  Argumenter, présenter des avantages
                                      et des inconvénients et interagir
                                      avec aisance.

  C1                                  Présenter des idées complexes de
                                      façon fluide, structurée et
                                      nuancée.

  C2                                  Défendre un point de vue avec
                                      précision, finesse et adaptation au
                                      contexte.
  -----------------------------------------------------------------------

**Langues :** français (FR) et anglais (EN).

## 6. Architecture microservices

SpeakUP adopte une architecture distribuée. Les capacités métier sont
réparties entre des microservices indépendants. Chaque microservice est
responsable de ses données et expose des interfaces documentées aux
autres composants.

La thématique du projet prévoit **9 microservices métier**. La liste
définitive et les responsabilités doivent être complétées par l'équipe
après validation du découpage.

    N° Microservice   Responsabilité principale   Responsable
  ---- -------------- --------------------------- -------------
     1 À compléter    À compléter                 À compléter
     2 À compléter    À compléter                 À compléter
     3 À compléter    À compléter                 À compléter
     4 À compléter    À compléter                 À compléter
     5 À compléter    À compléter                 À compléter
     6 À compléter    À compléter                 À compléter
     7 À compléter    À compléter                 À compléter
     8 À compléter    À compléter                 À compléter
     9 À compléter    À compléter                 À compléter

### Composants transversaux de l'architecture

La grille de la première validation demande de représenter les
composants suivants :

-   **Frontend** : interface web destinée aux utilisateurs.
-   **API Gateway** : point d'entrée des requêtes vers les
    microservices.
-   **Eureka** : découverte des services.
-   **Config Server** : centralisation de la configuration.
-   **Keycloak** : gestion de l'authentification et des rôles.
-   **Docker** : conteneurisation des composants.
-   **Bases de données** : une base dédiée par microservice, sans base
    métier partagée.

### Communication entre services

Les interactions seront définies dans le diagramme d'architecture et
dans la documentation de chaque microservice.

-   **Synchrone** : API REST et, si retenu, OpenFeign pour les appels
    qui nécessitent une réponse immédiate.
-   **Asynchrone** : événements via un broker de messages (par exemple
    RabbitMQ) pour les traitements longs, notamment l'analyse audio.

Le traitement audio doit être isolé afin qu'une analyse longue ne bloque
pas l'interface. Le choix définitif des protocoles, événements et
mécanismes de reprise sera documenté par l'équipe.

## 7. Focus : AI Speech Analysis Service

Le projet comprend un service spécialisé dans l'analyse des prises de
parole par l'intelligence artificielle. Son périmètre exact, ses API et
ses échanges avec les autres services sont à préciser dans sa fiche de
conception.

Responsabilités envisagées à partir de la thématique :

-   Transcrire les enregistrements vocaux (Speech-to-Text).
-   Contribuer à l'analyse de la prononciation.
-   Mesurer des indicateurs de fluidité : débit, pauses et hésitations.
-   Analyser des éléments d'intonation et de prosodie.
-   Produire des résultats structurés utilisables par les services
    chargés de l'évaluation et du suivi.

**Responsable :** à compléter.

**Technologies et stockage :** à confirmer par l'équipe lors de la
conception technique. Une option envisagée est un service de traitement
IA en Python, exposant une API, avec un stockage adapté à ses propres
données.

## 8. Technologies

La stack finale doit être confirmée par l'équipe et rester cohérente
avec les consignes du module.

  -----------------------------------------------------------------------
  Couche / composant                  Technologie prévue ou à confirmer
  ----------------------------------- -----------------------------------
  Frontend                            À confirmer

  Microservices métier                À confirmer

  API Gateway                         Spring Cloud Gateway (prévu si
                                      stack Spring retenue)

  Service Discovery                   Eureka (prévu)

  Configuration centralisée           Spring Cloud Config Server (prévu)

  Authentification et rôles           Keycloak (prévu)

  Communication asynchrone            RabbitMQ (proposition à valider)

  Bases de données                    Une base dédiée par microservice ;
                                      moteur à préciser

  Conteneurisation                    Docker
  -----------------------------------------------------------------------

## 9. Structure du dépôt

La structure doit respecter les livrables de la Validation 1 :

``` text
SpeakUP/
├── Backend/
│   ├── microservice-1/
│   ├── microservice-2/
│   ├── microservice-3/
│   ├── microservice-4/
│   ├── microservice-5/
│   ├── microservice-6/
│   ├── microservice-7/
│   ├── microservice-8/
│   └── microservice-9/
├── Frontend/
├── Documentation/
│   ├── Presentation/
│   └── Diagrams/
└── README.md
```

Les noms des dossiers Backend devront être remplacés par les noms
définitifs des microservices. Les projets doivent être initialisés dans
le dépôt ; la logique métier complète n'est pas attendue pour la
première validation.

## 10. Données et sources

Les sources envisagées dans la thématique comprennent :

  -----------------------------------------------------------------------
  Source            Langue            Utilisation       Licence indiquée
                                      prévue            dans la
                                                        thématique
  ----------------- ----------------- ----------------- -----------------
  Mozilla Common    FR / EN           Tester la         CC0
  Voice                               transcription     
                                      avec des voix et  
                                      accents variés    

  speechocean762    EN                Calibrer et       CC BY 4.0
                                      évaluer la        
                                      prononciation     

  L2-ARCTIC         EN                Tester la         CC BY-NC 4.0
                                      détection de      
                                      phonèmes mal      
                                      prononcés         

  Multilingual      FR / EN           Références pour   CC BY 4.0
  LibriSpeech                         la fluidité et    
                                      l'intonation      

  Conseil de        FR / EN           Construire les    Citer la source
  l'Europe ---                        grilles et        
  CECRL                               feedbacks par     
                                      niveau            

  France Éducation  FR                S'inspirer du     Droits réservés
  international ---                   format des        
  exemples DELF                       simulations       
  -----------------------------------------------------------------------

Les conditions d'utilisation doivent être vérifiées avant toute
exploitation. Les licences imposant une attribution doivent être citées
dans le dépôt et, le cas échéant, dans l'application. Les contenus
officiels protégés servent de modèles de format et ne doivent pas être
reproduits dans l'application.

### Données vocales et confidentialité

Une voix est une donnée personnelle et peut être une donnée biométrique.
Pour les démonstrations du projet, privilégier les corpus publics, les
voix synthétiques ou les enregistrements de membres de l'équipe réalisés
avec leur consentement. Ne pas enregistrer de véritables apprenants sans
cadre et autorisation appropriés.

## 11. Équipe

**Équipe : 6 étudiants**

    Étudiant Nom et prénom   Microservice attribué
  ---------- --------------- -----------------------
           1 À compléter     À compléter
           2 À compléter     À compléter
           3 À compléter     À compléter
           4 À compléter     À compléter
           5 À compléter     À compléter
           6 À compléter     À compléter

## 12. Démarrage du projet

Les commandes de lancement dépendront de la stack et de la configuration
retenues pour chaque composant. Elles seront ajoutées ici après
l'initialisation des projets.

À documenter pour chaque microservice : 1. Prérequis et versions. 2.
Variables d'environnement nécessaires. 3. Configuration de sa base de
données. 4. Commande de lancement. 5. Port utilisé. 6. Endpoints
disponibles et documentation API.

Ne pas publier de mots de passe, jetons, clés API ou fichiers contenant
des secrets dans le dépôt Git.

## 13. Documentation du projet

Les documents de conception et les supports de présentation sont stockés
dans :

-   `Documentation/Presentation/` : support de la présentation.
-   `Documentation/Diagrams/` : diagrammes d'architecture, de cas
    d'utilisation, de séquence et de données.

La documentation de chaque microservice doit préciser ses
responsabilités, ses entités, sa base de données, ses API REST, ses
interactions et le comportement prévu en cas d'indisponibilité d'un
service appelé.

## 14. Statut

**Étape actuelle :** préparation de la Validation 1 --- présentation du
sujet et modélisation microservices.

À cette étape, les projets des microservices sont initialisés dans le
dépôt. La logique métier complète sera développée après validation de la
conception.

------------------------------------------------------------------------

*SpeakUP --- Parlez, progressez, maîtrisez.*
