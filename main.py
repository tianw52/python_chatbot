import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
  with open(file_path, 'r') as file:
    data: dict = json.load(file)
  return data

def save_know_base(file_path: str, data: dict):
  with open(file_path, 'w') as file:
    json.dump(data, file, indent = 2)
    
def find_best_match(user_q: str, questions: list[str]) -> str | None:
  matches: list = get_close_matches(user_q, questions, n = 1, cutoff=0.5)
  return matches[0] if matches else None

def get_a_for_q(question: str, knowledge_base: dict):
  for q in knowledge_base["questions"]:
    if q["question"] == question:
      return q["answer"]
    
def manual_teach():
  in_question = input("Please type the question: ")
  in_answer = input("Please provide an answer: ") 
  print("Bot: Thank you! I learned something new.'")   
  return [in_question,in_answer]
    
def chat_bot():
  know_b: dict = load_knowledge_base('knowledge_base.json')
  print('Bot: Hi, I\'m an AI chatbot, feel free to ask a question or teach me something new by type "teaching mode"! ')
  while True:
    user_input: str = input('You: ')
    
    if user_input.lower() in ('quit', 'exit', 'bye'):
      break
    elif user_input.lower() == 'teaching mode':
      while True:
        taught = manual_teach()
        in_a = taught[1]
        in_q = taught[0]
        know_b["questions"].append({"question": in_q, "answer": in_a})
        save_know_base('knowledge_base.json', know_b)
        user_input: str = input('Teach something else?: ')
        if user_input.lower() in ("no", "exit", "quit"):
          break
    else:  
      best_match: str | None = find_best_match(user_input, [q["question"] for q in know_b["questions"]])
      
      if best_match:
        answer: str = get_a_for_q(best_match, know_b)
        print(f'Bot: {answer}')
      else:
        print('Bot: I don\'t know the answer. Can you teach me?')
        new_anwer: str = input('Type the answer or "skip" to skip: ')
        if new_anwer.lower() != 'skip':
          know_b["questions"].append({"question": user_input, "answer": new_anwer})
          save_know_base('knowledge_base.json', know_b)
          print('Bot: Thank you! I learned a new response.')
          
if __name__ == '__main__':
  chat_bot()