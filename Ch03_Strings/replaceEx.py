letter="""
Dear <|name|>,
You are selected for the job.
<|date|>"""
print(letter.replace("<|name|>", "Prasunjit").replace("<|date|>", "1st January 2026"))  # Replaces placeholders with actual values