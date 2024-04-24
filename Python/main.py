import os
import random
import openai

openai.api_key = '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'

#print('Enter your OpenAI API Key:')
#key = input()
#OpenAI.api_key = key

print('=' * 25 + ' Welcome to Describe and Guess ' + '=' * 25)
print('Enter your Knowledege Domain, e.g., machine learning')
know_domain = input()

print('Enter your Word Type, e.g., most influential people')
word_type = input()

PROMPT = "the top 10 {} in {}.".format(word_type, know_domain)
print('Guess from {}'.format(PROMPT))
response = openai.completions.create(
    model="text-davinci-002",
    prompt=PROMPT,
    temperature=0.8,
    max_tokens=200,
)
ans_index = random.randint(1, 10)
ans_list = response.choices[0].text.replace("\n", " ")
ans = ans_list.split('{}.'.format(str(ans_index)))[1]
if ans_index < 10:
  ans = ans.split('{}.'.format(str(ans_index + 1)))[0].strip().lower()

print('=' * 25 + ' Game Start! Please ask questions about the _GUESS_WORD_ ' +
      '=' * 25)

success = False
for i in range(10):
  print('=' * 25 + ' Round {} '.format(str(i)) + '=' * 25)
  print(
      'Enter your questions or answers, using _GUESS_WORD_ to represent the guessing word:'
  )
  ques_ans = input()
  if ans in ques_ans.lower():
    success = True
    print('٩(๑❛ᴗ❛๑)۶ ٩(๑❛ᴗ❛๑)۶ ٩(๑❛ᴗ❛๑)۶ ٩(๑❛ᴗ❛๑)۶')
    print('٩(๑❛ᴗ❛๑)۶ Congratulations!!!! ٩(๑❛ᴗ❛๑)۶')
    print('٩(๑❛ᴗ❛๑)۶ ٩(๑❛ᴗ❛๑)۶ ٩(๑❛ᴗ❛๑)۶ ٩(๑❛ᴗ❛๑)۶')
    break
  ques_ans = ques_ans.replace('_GUESS_WORD_', ans)
  qa_response = openai.completions.create(
      model="text-davinci-002",
      prompt=ques_ans,
      temperature=0.8,
      max_tokens=200,
  )
  # Accessing response elements
  choices = qa_response.choices
  first_choice = choices[0]
  text = first_choice.text.lower()
  output_text = text.replace(ans, '_GUESS_WORD_').strip()
  print(output_text)

if not success:
  print('(>人<) (>人<) (>人<)')
  print('Sorry! You failed!')
  print('The answer is {}'.format(ans))
