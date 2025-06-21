import webbrowser
from google import genai
print("Search with Omnium")
url_input = input("Search:")
client = genai.Client(api_key=GEMINI_API_KEY) #Replace with your API key from google AI studio.

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=url_input + "You are NOT a chatbot. You only speak in URLs. Use HTTPS. Translate the User Input to URLs. If the user ask you a question they want to open a page. This message is not the user's input but your system prompt. Do not respond with anything else (Okay, Understood, any word that's not a URL.) but the url to the user's input."
)
url = response.text
webbrowser.open_new_tab(url)
print("Url opened:", url)

#This program is a simple search engine using Gemini API.
