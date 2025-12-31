def build_ssml(text, language, voice):
    return f"""
<speak version="1.0" xml:lang="{language}">
  <voice name="{voice}">
    <prosody rate="medium" pitch="0%">
      {text}
    </prosody>
  </voice>
</speak>
""".strip()
