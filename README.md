# End-to-end Medical Chatbot Generative AI 🤖💬

## How to run? 🚀

### STEPS:

1. **Clone the repository** 📂

    ```bash
    git clone https://github.com/
    ```

2. **Create a conda environment** 🐍

    ```bash
    conda create -n medibot python=3.10 -y
    conda activate medibot
    ```

3. **Install the requirements** 📦

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** 📝

    Add your Pinecone & OpenAI credentials:

    ```ini
    PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

5. **Store embeddings to Pinecone** 🗂️

    ```bash
    python store_index.py
    ```

6. **Run the application** ▶️

    ```bash
    python app.py
    ```

7. **Open up localhost** 🌐

    ```bash
    open up localhost:
    ```

### Techstack Used 🛠️

- Python 🐍
- LangChain 🔗
- Flask 🌶️
- GPT 🧠
- Pinecone 🌲

### Preview

![image](https://github.com/user-attachments/assets/50c2ff97-c9c8-44fe-9f60-99d34f10d4bf)
