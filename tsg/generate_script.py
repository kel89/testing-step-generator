import subprocess
import openai


def get_suggestions(changes):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful developer assistant. "
                        "Your answers should be very brief. "
                        "You are helping with QA work. You will be given a git diff "
                        "and you should look at all the changes made and recommend "
                        "manual testing steps that the reviewer can use to test the "
                        "changes made and be confident that all new changes are working."
                    )
                },
                {
                    "role": "user",
                    "content": changes
                }
            ]
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        print("An error occurred while communicating with OpenAI API:")
        print(str(e))
        return None


def main(api_key):
    # Set the OpenAI API key
    openai.api_key = api_key

    # Get the diff from the current branch to master
    try:
        diff_output = subprocess.check_output(
            ['git', 'diff', 'master'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running git diff:")
        print(e.output.decode())
        return

    changes = diff_output.decode('utf-8')

    # If the diff is empty, inform the user
    if not changes.strip():
        print("No changes detected between the current branch and master.")
        return

    # Get suggestions based on the changes
    suggestions = get_suggestions(changes)

    # If suggestions were returned, print them
    if suggestions:
        print("Suggested Manual Testing Steps:\n")
        print(suggestions)
    else:
        print("Failed to generate suggestions.")
