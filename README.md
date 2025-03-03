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

# AWS CICD Deployment with GitHub Actions 🚀

1. **Login to AWS console** 🔑

2. **Create IAM user for deployment** 👤

    - **Access Required**:
        - EC2: Virtual machine
        - ECR: Elastic Container Registry to save your Docker image in AWS

    - **Deployment Steps**:
        1. Build Docker image of the source code 🐳
        2. Push your Docker image to ECR 📤
        3. Launch your EC2 instance 🚀
        4. Pull your image from ECR in EC2 📥
        5. Launch your Docker image in EC2 🖥️

    - **Policies**:
        - AmazonEC2ContainerRegistryFullAccess
        - AmazonEC2FullAccess

3. **Create ECR repo to store/save Docker image** 🗄️

    - Save the URI: `970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot`

4. **Create EC2 machine (Ubuntu)** 🖥️

5. **Install Docker in EC2 Machine** 🐳

    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

6. **Configure EC2 as self-hosted runner** 🏃‍♂️

    Go to `Settings > Actions > Runners > New self-hosted runner`, choose OS, then run commands one by one.

7. **Setup GitHub secrets** 🔐

    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION
    - ECR_REPO
    - PINECONE_API_KEY
    - GOOGLE_API_KEY
