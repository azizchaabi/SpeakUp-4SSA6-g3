# SpeakUP - AI Speech Analysis Microservice

Microservice REST développé avec **FastAPI** et **Pydantic** pour l'analyse de l'expression orale des apprenants dans le cadre du projet **SpeakUP**.

> **Note importante** : Dans cette version initiale (v1.0.0), le microservice fournit des endpoints opérationnels avec des métriques et des scores **simulés** à des fins de démonstration et d'intégration contractuelle. Aucun modèle lourd de Machine Learning n'est encore chargé.

---

## 1. Fonctionnalités

- **Vérification de santé (Health Check)** : Endpoints pour vérifier la disponibilité et le statut du microservice.
- **Support multilingue** : Consultation des langues gérées (français `fr` et anglais `en`).
- **Analyse orale simulée** : Évaluation du texte prononcé avec calcul de scores de prononciation, fluidité, intonation, score global et feedback pédagogique.
- **Documentation OpenAPI & Swagger UI interactive** : Validation Pydantic stricte, exemples de requêtes/réponses et test direct depuis le navigateur.

---

## 2. Structure du microservice

```text
AI Speech Analysis/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Point d'entrée FastAPI & configuration OpenAPI
│   ├── routers/
│   │   ├── __init__.py
│   │   └── speech_router.py     # Déclaration des routes /api/speech/*
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── speech_schema.py     # Modèles Pydantic de requêtes/réponses
│   └── services/
│       ├── __init__.py
│       └── speech_service.py    # Logique métier et simulation des scores
├── requirements.txt             # Dépendances Python minimales
└── README.md                    # Guide de démarrage et documentation
```

---

## 3. Endpoints de l'API

| Méthode | Endpoint | Description |
|---|---|---|
| `GET` | `/api/speech/hello` | Message confirmant le bon fonctionnement du microservice |
| `GET` | `/api/speech/status` | Statut opérationnel (`UP`) et version du microservice |
| `GET` | `/api/speech/languages` | Liste des langues prises en charge (`fr`, `en`) |
| `POST` | `/api/speech/analyze` | Analyse orale simulée (scores de prononciation, fluidité, intonation, feedback) |

---

## 4. Installation et Démarrage (PowerShell)

### Prérequis
- **Python 3.10+** (testé sous Python 3.13)
- PowerShell

### Étape 1 : Se positionner dans le dossier du microservice

```powershell
Set-Location -Path "Backend\AI Speech Analysis"
```

### Étape 2 : Créer l'environnement virtuel Python

```powershell
python -m venv venv
```

### Étape 3 : Activer l'environnement virtuel

```powershell
.\venv\Scripts\Activate.ps1
```

> *Si l'exécution de scripts est restreinte sur votre machine PowerShell, autorisez-la temporairement pour la session actuelle :*
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> .\venv\Scripts\Activate.ps1
> ```

### Étape 4 : Installer les dépendances

```powershell
pip install -r requirements.txt
```

### Étape 5 : Lancer le serveur de développement

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 5. Accès à la documentation Swagger UI

Une fois le serveur démarré, accédez directement à la documentation interactive dans votre navigateur :

- **Swagger UI** : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Schéma OpenAPI JSON** : [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 6. Exemples de Requêtes et Réponses

### 1. `GET /api/speech/hello`
**Requête (PowerShell) :**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/speech/hello" -Method GET
```
**Réponse JSON :**
```json
{
  "message": "Hello! The SpeakUP AI Speech Analysis microservice is operational."
}
```

---

### 2. `GET /api/speech/status`
**Requête (PowerShell) :**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/speech/status" -Method GET
```
**Réponse JSON :**
```json
{
  "service": "SpeakUP - AI Speech Analysis",
  "status": "UP",
  "version": "1.0.0"
}
```

---

### 3. `GET /api/speech/languages`
**Requête (PowerShell) :**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/speech/languages" -Method GET
```
**Réponse JSON :**
```json
{
  "languages": [
    {
      "code": "fr",
      "name": "French",
      "nativeName": "Français"
    },
    {
      "code": "en",
      "name": "English",
      "nativeName": "English"
    }
  ]
}
```

---

### 4. `POST /api/speech/analyze`

#### En Français (`language: "fr"`)
**Requête (PowerShell) :**
```powershell
$body = @{
    language = "fr"
    text = "Bonjour, je suis ravi de participer à cette séance d'entraînement oral."
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/speech/analyze" -Method POST -Body $body -ContentType "application/json; charset=utf-8"
```

**Réponse JSON :**
```json
{
  "transcription": "Bonjour, je suis ravi de participer à cette séance d'entraînement oral.",
  "pronunciationScore": 88.5,
  "fluencyScore": 91.0,
  "intonationScore": 84.0,
  "overallScore": 87.8,
  "feedback": "Très bonne prononciation et rythme fluide. L'articulation des phonèmes est claire et l'intonation est naturelle.",
  "isSimulated": true
}
```

#### En Anglais (`language: "en"`)
**Requête (cURL) :**
```bash
curl -X POST "http://127.0.0.1:8000/api/speech/analyze" \
  -H "Content-Type: application/json" \
  -d '{"language": "en", "text": "Good morning, I am practicing my English speech skills today."}'
```

**Réponse JSON :**
```json
{
  "transcription": "Good morning, I am practicing my English speech skills today.",
  "pronunciationScore": 87.2,
  "fluencyScore": 89.5,
  "intonationScore": 86.0,
  "overallScore": 87.7,
  "feedback": "Great pronunciation and natural speech rhythm. Vowel sounds are crisp and sentence stress is well modulated.",
  "isSimulated": true
}
```
