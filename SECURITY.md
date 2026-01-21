# Security Configuration Guide

## Environment Variables Setup

This project uses environment variables to securely manage sensitive credentials. Follow these steps:

### 1. Create your .env file

Copy the example file and fill in your actual credentials:
```bash
cp .env.example .env
```

### 2. Configure MongoDB Credentials

Edit the `.env` file with your MongoDB credentials:
```
MONGODB_USERNAME=your_actual_username
MONGODB_PASSWORD=your_actual_password
MONGODB_CLUSTER=your_cluster_url
MONGODB_URL=your_full_mongodb_connection_string
DB_NAME=US_VISA
COLLECTION_NAME=visa_data
```

### 3. Install Required Dependencies

Make sure to install python-dotenv:
```bash
pip install python-dotenv
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### 4. Using Environment Variables in Code

```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access variables
db_name = os.getenv("DB_NAME")
connection_url = os.getenv("MONGODB_URL")
```

## Important Security Notes

⚠️ **NEVER commit the `.env` file to version control!**

The `.gitignore` file is configured to exclude:
- `.env` and all `.env.*` files
- Credential files (`.pem`, `.key`, `.cert`, etc.)
- Secret configuration files
- API keys and tokens

## Files Already Secured

✅ The following have been configured:
- `.env` - Contains all sensitive credentials (git-ignored)
- `.env.example` - Template file (safe to commit)
- `.gitignore` - Updated with comprehensive security patterns
- `notebooks/mongoDB_test.ipynb` - Updated to use environment variables
- `requirements.txt` - Added python-dotenv dependency

## GitHub Security Alerts

If you received GitHub security alerts:
1. Remove any committed `.env` files from Git history
2. Rotate all exposed credentials immediately
3. Update your `.env` file with new credentials
4. Ensure `.gitignore` is properly configured (already done)

### Remove Sensitive Data from Git History

If credentials were previously committed:
```bash
# Using git-filter-repo (recommended)
git filter-repo --path .env --invert-paths

# Or using BFG Repo-Cleaner
bfg --delete-files .env
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

After cleaning:
```bash
git push origin --force --all
```

**⚠️ Remember to rotate all exposed credentials after cleaning Git history!**
