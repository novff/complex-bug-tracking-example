import requests
from datetime import datetime

# Запрос к GitHub API
headers = {"Authorization": "Bearer YOUR_TOKEN"}
issues = requests.get("https://api.github.com/repos/ваш-репозиторий/issues?state=all", headers=headers).json()

report = {
    "open": sum(1 for i in issues if i["state"] == "open"),
    "closed": sum(1 for i in issues if i["state"] == "closed"),
    "time_spent": {}
}

for issue in issues:
    created = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    closed = datetime.strptime(issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ") if issue["closed_at"] else None
    if closed:
        report["time_spent"][issue["number"]] = (closed - created).days
