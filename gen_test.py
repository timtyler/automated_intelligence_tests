import sys
import time
import google.generativeai as genai

# Generate test questions on a specified subject one at a time in a loop
# Arg1: number of questions to produce
# Arg2: Theme of the questions - e.g. riddles

def query_gemini(user_prompt):
  """
  Queries Gemini API with a user prompt, and returns the model's response.
  Args: user prompt
  Returns: The model's response
  """

  # Read API token from file
  with open("gemini_api_token.txt", "r") as f:
    api_token = f.read().strip()

  # Configure the model with the API token
  genai.configure(api_key=api_token)
  model = genai.GenerativeModel('gemini-1.5-pro-latest')

  # Construct the prompt

  gemini_response = model.generate_content(gemini_prompt)
  response_text = gemini_response.text
  return response_text

# Access specific arguments
script_name = sys.argv[0]
question_count = int(sys.argv[1])
prompt_topic = sys.argv[2]
existing_questions = []

for count in range(question_count):
  gemini_prompt = f"""Output a multiple choice question to act as a test of capability.
  The test question should not closely duplicate any of the questions in the following list:
  {existing_questions}
  This is a list of properties of the test question:
  * The theme of the question is: {prompt_topic}
  * The question should be reasonably short. No rambling on.
  * The questions should be challenging: we do not want questions that are easy to answer.
  * If factual knowledge is needed to answer the question, supply that knowledge in the question.
  * The question should end with a question mark.
  * The question should not be split over more than one line.
  * As far as possible, questions should have an umambiguous correct answer.
  * Question is not about spelling.
  * Question does not involve numbers bigger than 100.
  * Generate between 1 and 4 different incorrect but plausible-sounding answers to the question.
  * Answers should not duplicate other answers.
  * All the answers should be randomly sorted.
  * All the answers should be assigned upper case alphabetic symbols.
  * The first alphabetic symbol should be "A". Do not skip over any letters.
  * The alphabetic symbols should be assigned to the answers in alphabetic order.
  * Output a line with the alphabetic symbol of the correct question answer prefixed by "The correct answer is: ".
  * A rationale for the correct answer should be given on its own line.
  * Question rationales should be underneath all other parts of the question, prefixed by "Rationale: ".
  """
  response_text = query_gemini(gemini_prompt)
  print(f"Question: {count + 1}")
  print(response_text)
  extracted_question = response_text.partition('\n')[0]
  existing_questions.append(extracted_question)
  # Avoid ResourceExhausted exception
  time.sleep(15)
