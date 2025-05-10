import math
from collections import Counter
import os
import logging

def shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy

def analyze_file_entropy(file_path: str, threshold: float = 7.5):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        
        with open(file_path, 'rb') as f:
            content = f.read()
            entropy = shannon_entropy(content)
            logging.info(f"File: {file_path}")
            logging.info(f"Entropy: {entropy:.4f} / 8.0")
            
            if entropy > threshold:
                logging.warning(" Warning: High entropy – potential hidden or malicious content.")
            else:
                logging.info("File entropy within normal range")
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Analysis complete.")

def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    file_path = input("Enter the file path: ")
    threshold = float(input("Enter the threshold (default: 7.5): ") or 7.5)
    analyze_file_entropy(file_path, threshold)

if __name__ == "__main__":
    main()