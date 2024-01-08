# Scientific Article Explorer 

Answered questions based on abstracts retrieved from ArXiv or PubMed after search term entered. Returns pdfs of sources.

## Getting Started

### Prerequisites

- Python 3.10
- pip

### Installation

1. **Clone the repository:**

    ```bash
    git clone [repository URL]
    ```

2. **Create a .env file to store your OpenAI API key:**

    Create a file named `.env` in the root directory and add the following line:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```

3. **Set up your environment:**

    For example (or conda):
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements_qa.txt
    ```

5. **Run the app:**

    ```bash
    streamlit run app_qa.py
    ```


