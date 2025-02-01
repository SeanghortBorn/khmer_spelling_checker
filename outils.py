import xml.etree.ElementTree as ET
import difflib

def read_txt_file(txt_file):
    """Read text from a TXT file."""
    with open(txt_file, 'r', encoding='utf-8') as file:
        return file.read().strip()

# def read_xml_file(xml_file):
#     """Extract text content from an XML file."""
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#     return ''.join(root.itertext()).strip()

def read_xml_file(xml_file):
    """Extract text content from the 'content' section of an XML file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    content_text = ''
    for elem in root.findall(".//content"):
        content_text += ''.join(elem.itertext()).strip() + ' '
    return content_text.strip()

def compare_texts(ground_truth_text, input_text):
    """Compare texts and return spelling mistakes."""
    ground_truth_words = ground_truth_text.split()
    input_words = input_text.split()
    
    # Using difflib to find differences
    diff = difflib.ndiff(ground_truth_words, input_words)
    
    mistakes = []
    for word in diff:
        if word.startswith('- '):  # Word missing in input file
            mistakes.append((word[2:], 'Missing'))
        elif word.startswith('+ '):  # Additional (possibly incorrect) word in input file
            mistakes.append((word[2:], 'Incorrect'))
    
    return mistakes

def detect_spelling(ground_truth_file, input_file):
    ground_truth_text = read_txt_file(ground_truth_file)
    input_text = read_xml_file(input_file)
    
    mistakes = compare_texts(ground_truth_text, input_text)
    
    if mistakes:
        print("Spelling Mistakes Detected:")
        for word, error_type in mistakes:
            print(f"{word}\n: {error_type}\n")
    else:
        print("No spelling mistakes detected.")