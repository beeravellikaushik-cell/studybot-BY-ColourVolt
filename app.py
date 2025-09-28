# Debug: list all available models for this API key
models = genai.list_models()
for m in models:
    print(m.name)
