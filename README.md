# README.md Generator

## Description
This application generates a `README.md` file for a given codebase. It uses various AI models to analyze the code and produce a detailed and structured README file. The application supports models from Anthropic, OpenAI, and Groq.

## Features
- **AI Model Integration**: Supports Claude (Anthropic), GPT-4o (OpenAI), and LLaMA (Groq) models for generating README content.
- **Automated README Generation**: Automatically extracts and formats information from the codebase to create a comprehensive README file.
- **Environment Configuration**: Uses environment variables for API keys.
- **Command-Line Interface**: Provides a CLI for easy usage.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/ryanklapperhakkoda/documentation_assistant.git
    cd documentation_assistant
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    ANTHROPIC_API_KEY=your_anthropic_api_key
    OPENAI_API_KEY=your_openai_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage
To generate a `README.md` file for a given codebase, run the following command:
```bash
python generate_readme.py <file_path> --model <model>
```
- `<file_path>`: Path to the file containing the codebase.
- `<model>`: AI model to use for generation (`claude`, `openai`, `llama`). Default is `claude`.

Example:
```bash
python generate_readme.py example_codebase.py --model openai
```

## Configuration
The application uses environment variables to store API keys. Ensure you have a `.env` file in the root directory with the following keys:
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `GROQ_API_KEY`

## Dependencies
- `anthropic`
- `openai`
- `groq`
- `python-dotenv`
- `argparse`
- `snowflake-connector-python`

Ensure all dependencies are installed by running:
```bash
pip install -r requirements.txt
```

## Entry Points
- **Main Script**: `generate_readme.py`
- **Functions**:
  - `create_readme_file(content, directory)`: Creates the `README.md` file.
  - `read_file_content(file_path)`: Reads the content of the provided file.
  - `generate_readme_claude(client, user_prompt)`: Generates README using Claude model.
  - `generate_readme_openai(client, user_prompt)`: Generates README using OpenAI model.
  - `generate_readme_llama(client, user_prompt)`: Generates README using LLaMA model.
  - `main(file_path, model)`: Main function to handle the process.