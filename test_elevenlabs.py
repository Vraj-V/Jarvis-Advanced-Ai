# ElevenLabs TTS test
# Make sure to install elevenlabs: pip install elevenlabs

from elevenlabs import generate, play, set_api_key

# Replace with your ElevenLabs API key
set_api_key("sk_0566e10185418264aaefe08e1c2fa233c4aee4636fd4cd35")

text = "Hello! This is a test of ElevenLabs text-to-speech in your Jarvis project."

# Generate audio
try:
    audio = generate(text=text, voice="eUdJpUEN3EslrgE24PKx")  # Using your provided voiceId
    play(audio)
    print("ElevenLabs TTS test succeeded.")
except Exception as e:
    print(f"Error: {e}")
