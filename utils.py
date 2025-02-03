import re
import xml.etree.ElementTree as ET
import pandas as pd
import os

def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Function to clean Khmer text (removing special characters and spaces)
def clean_text(text):
    text = re.sub(r'[^\u1780-\u17FF]', '', text)  # Keep only Khmer characters
    return text

# Function to extract content from XML file
def extract_content_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    content_list = []
    keystroke_data = []
    
    for elem in root.iter('content'):
        if elem.text:
            content_list.append(clean_text(elem.text))
    
    for elem in root.iter('keystroke'):
        keystroke_data.append(elem.text)  # Store keystroke data to analyze deletions
    
    # return ' '.join(content_list), keystroke_data
    return content_list


def save_word_lists_to_excel(word_lists, column_names, output_file):
    # Find the maximum length of the lists
    max_length = max(len(lst) for lst in word_lists)

    # Normalize the lists to the same length by padding with empty strings
    normalized_lists = [lst + [''] * (max_length - len(lst)) for lst in word_lists]

    # Create DataFrame
    df = pd.DataFrame({name: words for name, words in zip(column_names, normalized_lists)})

    # Save to Excel
    df.to_excel(output_file, index=False)

# Function to rename multiple files
def rename_files(participant, folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found.")
        exit()
    files = os.listdir(folder_path)
    for index, filename in enumerate(files):
        old_path = os.path.join(folder_path, filename)
        if os.path.isdir(old_path):
            continue
        new_filename = f"{participant}art{index+1}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")