# Obsidian Data Packer
- To tell the truth, GitHub is not entirely safe for private notes. Imagine a 15-year-old hacker discovering a vulnerability that could expose a private repository. If someone has malicious intent toward you, they could exploit this bug and make your private data public.

- What our script does: It is a simple script that utilizes the 7z API to encrypt notes using SHA-256. It creates a password-protected zip file with a specified size limit (in MB you provide during running the script) and then pushes these encrypted backups to GitHub.

## Obsidian Data Packer Solution
**Key Features**
- Military-grade AES-256 encryption via 7z (FIPS 197 compliant)
- Configurable chunk sizing for optimized storage
- Automated GitHub synchronization workflow
- Salted SHA-256 hashing for file integrity verification

1. Download & Install the code.
  ```bash
  git clone https://github.com/Ctmax-ui/obsidian-data-packer.git
  cd obsidian-data-packer
  pip install -r requirements.txt
  ```
2. Paste your notes folder or the folder you want to ecnrypt in this repo root.
3. Run the main.py
5. Make an output folder & link that to your github private repo.
 ```bash
  mkdir output && cd output
  git init
  git remote add origin <your repo url>
 ```
4. Run the main.py or double click on the run.bat **In windows**.


Security Considerations Table
Feature |	Standard GitHub | Obsidian Data Packer
|---------------|:-------------:|:-------------:|
At-rest encryption	|❌ No| ✅ AES-256
Chunked storage	|❌ Single file risk|	✅ Split archives
Local key management	|❌ Relies on GH|	✅ Client-side control
Metadata protection	|❌ Visible structure	| ✅ Obfuscated contents
