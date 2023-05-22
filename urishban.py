import openai
from mtranslate import translate

target_lang_hy = 'hy'
target_lang_en = 'en'

# Set up your OpenAI API credentials
openai.api_key = 'Your Key API'
while True:
    # Define the prompt for text generation
    prompt = input("Please enter text -- > ")


# text = input("Please enter text -- > ")    
# translated_text = translate(prompt, target_lang_en)
# print(translated_text)
# prompt = translated_text
# Generate text using the OpenAI GPT-3.5 model
    response = openai.Completion.create(
    engine="text-davinci-003",  # Choose the desired model/engine
    prompt=prompt,
    max_tokens=100,  # Adjust the desired length of the generated text
    n=1,  # Generate a single response
    stop=None,  # Specify an optional stop sequence
    temperature=0.7  # Adjust the temperature for text randomness
    )

# Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()
# translated_text = translate(generated_text,target_lang_en)
# Print the generated text
    print(generated_text)
