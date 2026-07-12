list=["laptop", "phone", "tablet", "headset", "chromebook" ]
import random

word=random.choice(list)


display = ["_"] * len(word)

chances = 6

print(" ".join(display))

while chances > 0:

    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        chances -= 1
        print("Wrong!")
        print("Remaining chances:", chances)

    print(" ".join(display))

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word.")
        break

if "_" in display:
    print("Game Over!")
    print("The word was:", word)
