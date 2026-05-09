# ==========================================
# API Configuration Settings
# ==========================================

# Note: For security reasons, the actual API key is managed via Google Colab's userdata (Secrets).

API_SETTINGS = {
    "PROVIDER": "Groq",
    "MODEL_NAME": "llama-3.1-8b-instant",
    "API_KEY": "YOUR_GROQ_API_KEY_HERE", # Replace securely in production
    "MAX_TOKENS": 800,
    "TEMPERATURE": 0.7
}
