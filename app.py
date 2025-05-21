import streamlit as st
import requests

st.set_page_config(page_title="Zentrium AI Assistant")

st.title("Zentrium AI - Your Private Business Automation Assistant")

# Input box for your question
user_input = st.text_area("Ask your assistant:", height=150)

if st.button("Send"):
    if not user_input.strip():
        st.warning("Please enter a question or prompt.")
    else:
        with st.spinner("Thinking..."):
            # OpenRouter API info
            API_URL = "https://openrouter.ai/api/v1/chat/completions"
            API_KEY = st.secrets["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"]  # Store your key securely in Streamlit secrets

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            }

            # Build messages for the chat completion
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a senior automation consultant for Zentrium AI. "
                        "Help the user by providing professional business automation guidance, "
                        "cold email templates, cold call scripts, and company research insights."
                    )
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]

            payload = {
                "model": "meta-llama/llama-3.3-8b-instruct:free",
                "messages": messages,
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                answer = data["choices"][0]["message"]["content"]
                st.markdown("### Assistant's Response:")
                st.write(answer)
            except Exception as e:
                st.error(f"API Error: {e}")
