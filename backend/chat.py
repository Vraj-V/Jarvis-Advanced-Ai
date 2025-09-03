import os
import eel
from openai import OpenAI

# Expose this function to frontend
@eel.expose
def get_ai_response(user_input):
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		return "API key not set. Please set OPENAI_API_KEY environment variable."
	try:
		client = OpenAI(api_key=api_key)
		completion = client.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{"role": "system", "content": "You are a virtual assistant."},
				{"role": "user", "content": user_input}
			]
		)
		return completion.choices[0].message.content
	except Exception as e:
		return f"Sorry, something went wrong: {str(e)}"
