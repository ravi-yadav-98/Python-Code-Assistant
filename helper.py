
import json
from pathlib import Path


def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)
    

def load_prompt_from_file(file_path):
    """
    Reads a prompt from a given text file.
    
    Args:
        file_path (str): Path to the text file containing the prompt.
    
    Returns:
        str: The content of the text file as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            prompt = file.read().strip()  # Read and strip extra whitespace
        return prompt
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")



def save_chat_history(chat_result, file_path):
    """
    Saves the chat history from a ChatResult object to a text file.

    Args:
        chat_result (ChatResult): The ChatResult object containing the chat history.
        file_path (str or Path): The file path where the chat history should be saved.
    """
    file_path = Path(file_path)
    
    # Extract and format the chat history
    chat_history = chat_result.chat_history
    formatted_history = []

    for message in chat_history:
        role = message.get('role', 'unknown')
        name = message.get('name', 'unknown')
        content = message.get('content', '')

        # Format each message for readability
        formatted_message = f"Role: {role}\nName: {name}\nContent:\n{content}\n{'-'*80}\n"
        formatted_history.append(formatted_message)

    # Save formatted chat history to the file
    try:
        with file_path.open("w", encoding="utf-8") as file:
            file.writelines(formatted_history)
        print(f"Chat history successfully saved to {file_path}")
    except Exception as e:
        print(f"Failed to save chat history: {e}")


