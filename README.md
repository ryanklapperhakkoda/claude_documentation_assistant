# README Generator

## Description

This Python application generates a README.md file for a given codebase using the Anthropic API. It analyzes the provided code and creates a detailed document explaining the application's functionality and providing instructions for users to run it.

## Features

- Analyzes a given codebase
- Generates a structured README.md file
- Uses Anthropic's API for content generation
- Supports command-line arguments for input file specification
- Creates the README.md file in the same directory as the input file

## Installation

1. Clone the repository:
   ```
   git clone claude_readme_generator
   ```

2. Navigate to the project directory:
   ```
   cd claude_readme_generator
   ```

3. Install the required dependencies:
   ```
   pip install anthropic python-dotenv
   ```

4. Set up your Anthropic API key:
   - Create a `.env` file in the project root
   - Add your Anthropic API key to the `.env` file:
     ```
     ANTHROPIC_API_KEY=your_api_key_here
     ```

## Usage

Run the script from the command line, providing the path to the file containing the codebase:

```
python main.py /path/to/your/codebase_file.py
```

The script will analyze the codebase and generate a README.md file in the same directory as the input file.

## Configuration

The application uses environment variables for configuration. Make sure to set up your `.env` file with the following:

- `ANTHROPIC_API_KEY`: Your Anthropic API key

## Dependencies

- anthropic: For interacting with the Anthropic API
- python-dotenv: For loading environment variables from a .env file
- argparse: For parsing command-line arguments

## Note

This README generator is designed to work with the Anthropic API. Make sure you have a valid API key and sufficient credits to use the service.