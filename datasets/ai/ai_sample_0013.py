import random

def generateMarkov(text):
  words = text.split(' ')
  markovChain = {}

  for i in range(len(words) - 2):
    current = words[i]
    next = words[i + 1]
    if current in markovChain:
      if next in markovChain[current]:
        markovChain[current][next] += 1
      else:
        markovChain[current][next] = 1
    else:
      markovChain[current] = {next: 1}

  generatedText = ""
  current = random.choice(list(markovChain))
  generatedText += current

  for i in range(100):
    choices = markovChain[current]
    choices = [
      key for key, value in choices.items()
      for i in range(value)
    ]
    try:
      current = random.choice(choices)
      generatedText += " " + current
    except:
      break

  return generatedText

text = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?'

print(generateMarkov(text))