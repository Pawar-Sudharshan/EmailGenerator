import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are an AI email assistant that only generates professional, polite,
and context-appropriate business emails.

Return only the formatted email.
"""

def generate_email(user_input: str) -> str:
    if not user_input.strip():
        return "Please enter your email intent."

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # or gpt-4o-mini
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=generate_email,
    inputs=gr.Textbox(
        label="Enter your email intent",
        lines=4
    ),
    outputs=gr.Textbox(label="Generated Email"),
    title="📧 Professional Email Generator",
    description="Generate workplace emails using OpenAI API."
)

if __name__ == "__main__":
    demo.launch()
