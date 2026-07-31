# ♊ Gemini Operations: Claude Track Integration

This document outlines the workflow and script for retrieving database credentials from Azure Key Vault and saving registered candidates for the Claude Track to MongoDB.

## 🎯 Goal
Save incoming student and instructor candidate details for the **Claude Specialist Track** to a centralized database.

---

## 🔐 Credentials Management (Azure Key Vault)
To follow security best practices, the database connection string is retrieved at runtime from our Azure Key Vault instance.

*   **Key Vault Name**: `dp-kv-deliverypilot`
*   **Key Vault URL**: `https://dp-kv-deliverypilot.vault.azure.net`
*   **Secret Name**: `meditate-mongodb-uri`
*   **Authentication**: Managed securely via the Azure CLI session using `DefaultAzureCredential()`.

---

## 📊 Database Target (MongoDB)
*   **Database Name**: `cambridge_ai_courses`
*   **Collection**: `candidates`
*   **Documents Structure**:
    ```json
    {
      "name": "Candidate Name",
      "email": "candidate@example.com",
      "track": "Claude track",
      "experience": "beginner/intermediate/advanced",
      "status": "Enrolled / Instructor",
      "registration_date": "YYYY-MM-DD"
    }
    ```

---

## 🐍 Script Implementation
The automation script is saved in [`save_candidates.py`](file:///Users/rifaterdemsahin/projects/cambridge-ai-courses/save_candidates.py). 

### 🚀 Running the Script
To fetch the secrets and register the candidates, run:
```bash
python3 save_candidates.py
```

### 📋 Registered Candidates
The following candidates have been successfully stored in MongoDB:
1.  **Rifat Erdem Sahin** 🚀 (Advanced, Enrolled)
2.  **Marianna Nechypor** 💡 (Advanced, Instructor/Adviser)
