import sys
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from pymongo import MongoClient

def main():
    print("🚀 Initializing Candidate Registration for Claude Track...")
    
    # 1. Initialize Azure Key Vault Client using DefaultAzureCredential
    vault_url = "https://dp-kv-deliverypilot.vault.azure.net"
    print(f"🔐 Authenticating to Azure Key Vault: {vault_url}...")
    try:
        credential = DefaultAzureCredential()
        vault_client = SecretClient(vault_url=vault_url, credential=credential)
        
        # 2. Retrieve MongoDB connection URI from Key Vault
        print("🔑 Fetching 'meditate-mongodb-uri' secret...")
        secret = vault_client.get_secret("meditate-mongodb-uri")
        mongodb_uri = secret.value
        print("✅ Secret retrieved successfully.")
        
    except Exception as e:
        print(f"❌ Failed to retrieve credentials from Azure Key Vault: {e}", file=sys.stderr)
        sys.exit(1)

    # 3. Connect to MongoDB
    print("📡 Connecting to MongoDB cluster...")
    try:
        mongo_client = MongoClient(mongodb_uri)
        db = mongo_client["cambridge_ai_courses"]
        candidates_col = db["candidates"]
        print("✅ Connected to MongoDB.")
        
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}", file=sys.stderr)
        sys.exit(1)

    # 4. Define candidate details for Claude Track
    sample_candidates = [
        {
            "name": "Rifat Erdem Sahin",
            "email": "rifat@example.com",
            "track": "Claude track",
            "experience": "advanced",
            "status": "Enrolled",
            "registration_date": "2026-07-31"
        },
        {
            "name": "Marianna Nechypor",
            "email": "marianna@example.com",
            "track": "Claude track",
            "experience": "advanced",
            "status": "Instructor/Adviser",
            "registration_date": "2026-07-31"
        }
    ]

    # 5. Save candidates to MongoDB
    print(f"📝 Inserting {len(sample_candidates)} candidates into 'candidates' collection...")
    try:
        for candidate in sample_candidates:
            # Avoid inserting duplicates by using email + track as a unique combination
            existing = candidates_col.find_one({"email": candidate["email"], "track": candidate["track"]})
            if existing:
                print(f"ℹ️ Candidate {candidate['name']} ({candidate['email']}) already exists. Skipping.")
            else:
                result = candidates_col.insert_one(candidate)
                print(f"✅ Saved candidate: {candidate['name']} (ID: {result.inserted_id})")
        
        # Verification Count
        count = candidates_col.count_documents({"track": "Claude track"})
        print(f"📊 Total candidates registered for Claude track: {count}")
        
    except Exception as e:
        print(f"❌ Failed to insert data into MongoDB: {e}", file=sys.stderr)
        sys.exit(1)

    print("🎉 All operations completed successfully!")

if __name__ == "__main__":
    main()
