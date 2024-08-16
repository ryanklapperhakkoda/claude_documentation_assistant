import anthropic
import re
import os
from dotenv import load_dotenv
import argparse

def create_readme_file(content, directory):
    # Extract the README content from between the <readme> tags
    readme_content = re.search(r'<readme>(.*?)</readme>', content, re.DOTALL)
    
    if readme_content:
        # Create the README.md file in the same directory as the input file
        readme_path = os.path.join(directory, 'README.md')
        with open(readme_path, 'w') as f:
            f.write(readme_content.group(1).strip())
        print(f"README.md file has been created successfully in {directory}")
    else:
        print("No README content found in the API response.")

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main(file_path):
    load_dotenv()

    client = anthropic.Anthropic(
        api_key = os.environ.get("ANTHROPIC_API_KEY")
    )

    # Read the content of the file
    codebase_content = read_file_content(file_path)

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": f"""You are tasked with generating a README.md file for a given codebase. Make sure the content is placed between <readme> </readme> tags. Your goal is to create a detailed document that explains what the application does and provides instructions for users to run the application. Follow these steps to complete the task:\n\n1. First, you will be provided with the codebase in the following format:\n\n<codebase>\n{codebase_content}\n</codebase>\n\n2. Analyze the codebase thoroughly. Pay attention to:\n   - The main functionality of the application\n   - Technologies and frameworks used\n   - File structure\n   - Dependencies\n   - Configuration files\n   - Entry points of the application\n\n3. Structure your README.md file to include the following sections:\n   - Project Title\n   - Description\n   - Features\n   - Installation\n   - Usage\n   - Configuration (if applicable)\n   - Dependencies\n\n4. For each section, provide detailed and relevant information:\n   - Project Title: Use the name of the main folder or the project name if evident from the codebase.\n   - Description: Briefly explain what the application does and its main purpose.\n   - Features: List the key functionalities of the application.\n   - Installation: Provide step-by-step instructions for setting up the project locally.\n   - Usage: Explain how to run the application and any important commands or scripts.\n   - Configuration: If the app requires any configuration, explain how to set it up.\n   - Dependencies: List all major dependencies and their versions.\n 5. Write in a clear, concise, and professional tone. Use markdown formatting to enhance readability:\n   - Use headers (##, ###) for different sections\n   - Use code blocks (```) for command-line instructions or code snippets\n   - Use bullet points (-) for lists\n   - Use bold (**) or italic (*) for emphasis where appropriate\n\n6. Output your generated README.md file within <readme> tags. Ensure that the content is properly formatted in markdown.\n\nBegin your analysis and README.md generation now. Remember to base all information strictly on the provided codebase."""
            }
        ]
    )

    # Get the directory of the input file
    input_directory = os.path.dirname(os.path.abspath(file_path))

    # Create the README.md file from the API response in the same directory as the input file
    create_readme_file(message.content[0].text, input_directory)

    # Print the API response
    print(message.content[0].text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate README.md from a given codebase file.")
    parser.add_argument("file_path", help="Path to the file containing the codebase")
    args = parser.parse_args()

    main(args.file_path)