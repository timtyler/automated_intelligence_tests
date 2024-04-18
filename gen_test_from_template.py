import sys

def process_file(filename):
  """Processes a file, removing lines starting with "Rationale:" and replacing lines starting with "The correct answer is:" with a generic version."""

  with open(filename, 'r') as f:
    for line in f:
      if line.startswith("The correct answer is:"):
	    # Replace with generic line
        print("The correct answer is: ")
      elif not line.startswith("Rationale:"):
	    # Print line without modification
        print(line, end='')

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: py gen_test_from_template.py <filename>")
  else:
    print("Please answer these multiple choice questions.")
    print("Output your answer letter first. It could help if notes are appended, but they should not contain line breaks.")
    print("")
    process_file(sys.argv[1])
