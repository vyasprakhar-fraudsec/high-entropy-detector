# high-entropy-detector

Detects potential hidden or malicious content in files using Shannon Entropy.

---

## 📌 What is Entropy-Based Detection?

Shannon Entropy is a statistical measure used to detect randomness in data. High entropy values often indicate:

- Encrypted or compressed content  
- Potentially obfuscated or malicious data (e.g., secrets, malware payloads)

This tool helps identify such content by calculating the entropy of strings or file sections.

---

## 🚀 Features

- Calculates Shannon Entropy of strings or file content  
- Flags content above a suspicious threshold (e.g. 7.5+)  
- Useful for detecting:
  - API keys or secrets  
  - Malware payloads  
  - Encoded binaries or shellcode  

---

## 🛠️ How to Use



### 🔹 From Command Line


## 🧪 Sample Output

[INFO] Scanning file: test_data/secrets.txt
[RESULT] Line 2: Potential high entropy string detected (entropy = 4.95)
[RESULT] Line 7: Potential high entropy string detected (entropy = 5.23)
[INFO] Scan complete.

```bash
python high_entropy_detector.py <path_to_file>
