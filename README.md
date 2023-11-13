# python_chatbot

A stupid (kinda) chatbot that make reponses accrooding to its knowledge base.

For example, if the user input is:
```
"How are you?
```

The bot would search for questions that are similar to the user input and return the closest repsonse if found one. Otherwise, it would ask the user to teach them the answer. That is,

```
"I'm good"   # if "I'm good" is the corresponding answer to "how are you" in the knowledge base

OR

"I don't know the answer. Can you teach me?"   # if such question doesn't exist in the knowledge base
```

User can also manully teach the bot by type ```teaching mode```, then the bot would ask for question and answer to be stored in the knowledge base.

**Example**
```
Bot: Hi, I'm an AI chatbot, feel free to ask a question or teach me something new by type "teaching mode"!
You: Hi, how are you?
Bot: I'm good, how about you?
You: I'm okay
Bot: I don't know the answer. Can you teach me?
Type the answer or "skip" to skip:
You: Great, what do you want to talk about today?
Bot: Thank you! I learned a new response.
...
```
