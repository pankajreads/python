import random

from google import genai

def generate_ai_word(difficulty="easy"):
    client = genai.Client(api_key="AIzaSyDY4pnlYBI5PcU7zZA0aeLTf3NCb7eekks")
    response = client.models.generate_content(
        model="gemini-2.0-flash", # Use the latest stable version
        contents=f"Generate ONE single English word for Hangman. Difficulty: {difficulty}. Format strictly as 'word: example\nhint: something'."
    )
    
    # Fix 2: Use response.text to get the string
    output = response.text 

    lines = output.strip().split("\n")
    # Adding a small check to ensure the split works
    word = lines[0].split(":")[1].strip().lower()
    hint = lines[1].split(":")[1].strip()

    return word, hint



stages = [
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]


difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

word, hint = generate_ai_word(difficulty)

print("\nHINT:", hint)

live=4
guess_word=["_"]*len(word)
print(''.join(guess_word))
while(live>0):
    guess_letter=(input("Enter your choice of character ").lower())
    if guess_letter in word:
        for char in range(0,len(guess_letter)):
            for i in range (0,len(word)): 
                if(word[i]==guess_letter[char]):
                        guess_word[i]=guess_letter[char]
        print(''.join(guess_word),"you are safe")
    else:
        print(stages[4-live])
        live-=1
    if(''.join(guess_word)==word):
        print("you win")
        break
else:
    print("You are HANGGED")
    print(word)