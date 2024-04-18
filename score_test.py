def check_answers(template_file, test_file):
  """Compares answers in a template file with answers in a test file and calculates the score."""

  correct_answers = 0
  total_answers = 0

  with open(template_file, 'r') as template, open(test_file, 'r') as test:
    template_lines = [line for line in template if line.startswith("The correct answer is: ")]
    test_lines = test.readlines()

    for template_line, test_line in zip(template_lines, test_lines):
      # Extract correct answer letter (e.g., 'A')
      correct_answer = template_line.strip()[-1]  
      user_answer = test_line.strip()[0]  # Extract user's answer letter

      if correct_answer == user_answer:
        correct_answers += 1
        print(f"{user_answer} should be {correct_answer} - CORRECT")
      else:
        print(f"{user_answer} should be {correct_answer} - WRONG")

      total_answers += 1

  return correct_answers, total_answers

if __name__ == "__main__":
  # Replace with actual filenames
  template_filename = "riddles.txt"
  test_filename = "riddles_answers.txt"
  correct_answers, total_answers = check_answers(template_filename, test_filename)
  print(f"Score: {correct_answers}/{total_answers}")
