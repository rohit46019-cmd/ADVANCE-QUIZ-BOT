from models.question import Question

def generate_questions_for_prompt(prompt: str, config: dict, api: dict):
    # Demo generator; replace with calls to Gemini/OpenAI/Perplexity using api["service"], api["api_key"]
    qs = []
    for i in range(1, 11):
        qs.append(Question(
            i,
            f"{prompt} — Sample Q{i} 🔎",
            {"A":"Option A","B":"Option B","C":"Option C","D":"Option D"},
            "B",
            "Because 'B' fits the logic (demo)."
        ))
    return qs
