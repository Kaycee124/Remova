# functions that are important to the project

import os, datetime, time, random

import os
import datetime

def write_messages_to_file(messages):
    """
    Writes an array of messages (dictionaries) to a file in the project folder, overwriting the existing content and appending the timestamp.

    Args:
        messages (list): An array of message dictionaries, each containing 'name', 'number', and 'message' keys.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"messages_{timestamp.replace(':', '-')}.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    content = f"Messages written at {timestamp}:\n"

    for message in messages:
        content += f"Name: {message['name']}\n"
        content += f"Number: {message['number']}\n"
        content += f"Message: {message['message']}\n"
        content += "\n"

    # Add an extra newline at the end
    content += "\n"

    # Create the directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Write the content to the file, overwriting the existing content
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Messages written to {file_path}")
    return file_path

# def read_messages_from_file(file_path):
#     """
#     Reads messages from the specified file.

#     Args:
#         file_path (str): Path to the file containing messages.

#     Returns:
#         list: A list of message dictionaries, each containing 'name', 'number', and 'message' keys.
#     """
#     messages = []
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             lines = file.readlines()

#             # Skipping the first line which contains the timestamp
#             lines = lines[1:]

#             # Parsing messages from the file content
#             current_message = {}
#             for line in lines:
#                 line = line.strip()
#                 if line == "":
#                     # If line is empty, it indicates the end of a message, so add it to the messages list
#                     if current_message:
#                         messages.append(current_message)
#                         current_message = {}
#                 else:
#                     # Splitting each line into key and value pairs
#                     key, value = line.split(": ", 1)
#                     current_message[key] = value

#             # Adding the last message if any
#             if current_message:
#                 messages.append(current_message)

#     except FileNotFoundError:
#         print("File not found.")
    
#     return messages

def read_messages_from_file(file_path):
    """
    Reads messages from the specified file.

    Args:
        file_path (str): Path to the file containing messages.

    Returns:
        list: A list of message dictionaries, each containing 'name', 'number', and 'message' keys.
    """
    messages = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            # Skipping the first line which contains the timestamp
            lines = lines[1:]

            # Parsing messages from the file content
            current_message = {}
            for line in lines:
                line = line.strip()
                if line == "":
                    # If line is empty, it indicates the end of a message, so add it to the messages list
                    if current_message:
                        messages.append(current_message)
                        current_message = {}
                else:
                    # Splitting each line into key and value pairs
                    split_line = line.split(": ", 1)
                    if len(split_line) == 2:
                        key, value = split_line
                        current_message[key] = value

            # Adding the last message if any
            if current_message:
                messages.append(current_message)

    except FileNotFoundError:
        print("File not found.")
    
    return messages

# Example usage:
# Assuming you have the file path
