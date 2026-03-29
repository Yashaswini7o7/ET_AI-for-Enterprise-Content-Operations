def check_compliance(content: str):
    banned_words = ["fake", "scam"]

    issues = []
    for word in banned_words:
        if word in content.lower():
            issues.append(f"Contains banned word: {word}")

    return {
        "approved": len(issues) == 0,
        "issues": issues
    }
