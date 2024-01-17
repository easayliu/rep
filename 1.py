from emoji import emojize
import random

emojis = ["😀", "😄", "😊", "😎", "😍", "🤩", "😂", "🥳", "😇", "🥰"]
random_emoji = random.choice(emojis)

print(random_emoji)


dizzy = emojize(":tent:")
print (dizzy)