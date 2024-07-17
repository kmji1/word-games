import pronouncing
from openai import OpenAI
from config import OPENAI_API_KEY, ORG

client = OpenAI(
  api_key=OPENAI_API_KEY,
  organization=ORG,
)

usedWords = []
toRhyme = input("What's the starting word? ")
yourCommand = "Generate a funny, contextually correct without punctuation sentence where the last word rhymes with, but isn't " + toRhyme
myCommand = "You are in a diss rhyming game where you have to guess the last word of your opponent's sentence using context clues, where the word rhymes with, but isn't" + toRhyme

def myTurn():
    bar = input("What's your sentence? ")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": myCommand},
            {"role": "user", "content": "You so dumb, you need to go back to"},
            {"role": "assistant", "content": "school"},
            {"role": "user", "content": bar},
        ]
    )

    answer = response.choices[0].message.content
    print(answer)
    correct = input("correct? (y/n) ")
    if (correct=="y"):
        if answer in usedWords:
            print("word already used")
        else:
            usedWords.append(answer)
            return True
    else:
        return False

def yourTurn():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're in a diss rhyming battle game where your opponent is trying to guess the last word of your sentence through context clues"},
            {"role": "user", "content": "Generate a funny, contextually correct sentence without punctuation where the last word rhymes with cart"},
            {"role": "assistant", "content": "You smell so stinky, I could call you a fart"},
            {"role": "user", "content": yourCommand},
        ]
    )
    bar = response.choices[0].message.content
    print(bar[0:bar.rfind(" ")])
    answer = input("Fill in the blank: ")
    if answer == bar[bar.rfind(" ")+1:]:
        if bar[bar.rfind(" ")+1:] in usedWords:
            print("word already used")
            return False
        else:
            print("correct, your turn!")
            return True
    else:
        print("nope, the word was " + bar[bar.rfind(" ")+1:])
        return False

def main():
    while True:
        if (yourTurn()==False):
            break
        if (myTurn()==False):
            break

main()
