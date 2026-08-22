import csv
import json

def research_app(app, category, website):
    # Instead of calling OpenAI, return a mock response
    return {
        "Auth method": "API Key",
        "Self-serve vs gated": "Self-serve",
        "API surface": "Basic endpoints",
        "Buildability verdict": "Feasible",
        "Evidence": f"{website}/docs"
    }

def main():
    results = []
    with open("data/apps.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Mock researching {row['App']}...")
            result = research_app(row["App"], row["Category"], row["Website"])
            results.append({
                "App": row["App"],
                "Category": row["Category"],
                "Website": row["Website"],
                "Result": result
            })

    with open("data/results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("✅ Mock research complete. Results saved to data/results.json")

if __name__ == "__main__":
    main()
