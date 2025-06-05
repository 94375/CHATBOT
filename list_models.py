import google.generativeai as genai

API_KEY = "AIzaSyB91-4FG33qNy-Y-MHgXRtHBm7hDTxaFYA"
genai.configure(api_key=API_KEY)

for m in genai.list_models():
    print(f"Model name: {m.name}")
    print(f"  Supported methods: {getattr(m, 'supported_generation_methods', 'Unknown')}")
    print()
    