def analyze_text(text: str) -> dict:
    """Analyzes string to compute total word count and character count."""
    words = text.split()
    return {
        "text": text,
        "word_count": len(words),
        "char_count": len(text)
    }

prompts = []
results = []

# Collect and analyze three prompts
for number in range(1, 4):
    prompt = input(f"Enter prompt {number}: ")
    prompts.append(prompt)
    
    # Store dictionary analysis in results
    analysis = analyze_text(prompt)
    results.append(analysis)

# Find prompt with the highest word count
max_prompt_analysis = max(results, key=lambda item: item["word_count"])

# Display results summary
print("\n--- Prompt Analysis Results ---")
for idx, res in enumerate(results, start=1):
    print(f"Prompt {idx}: {res['word_count']} words | {res['char_count']} chars")

print("\n--- Summary ---")
print(f"Prompt with the most words ({max_prompt_analysis['word_count']} words):")
print(f"\"{max_prompt_analysis['text']}\"")