
# **SummarizeBot**

SummarizeBot is a web application that allows users to input a URL for an article and receive a summarized version of the article using OpenAI's GPT-4 model. The application is built with FastAPI, Selenium for web scraping, and it runs inside a Docker container.

## **Features**

- **URL Input**: Users can input the URL of an article.
- **Web Scraping**: The application scrapes the article content from the provided URL.
- **Text Summarization**: Summarize the article content using OpenAI's GPT-4 model.
- **Responsive UI**: A simple and responsive web interface for ease of use.

## **Tech Stack**

- **Backend**: FastAPI
- **Web Scraping**: Selenium
- **Language Model**: OpenAI's GPT-4 via `langchain`
- **Containerization**: Docker
- **Frontend**: Basic HTML, CSS

## **Getting Started**

### **Prerequisites**

- **Docker**: Ensure you have Docker installed on your system.
- **Python 3.9+**: Required if you want to run the application locally without Docker.
- **OpenAI API Key**: You need an API key from OpenAI to use the GPT-4 model.

### **Setup**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/summarizebot.git
   cd summarizebot
   ```

2. **Environment Variables**

   Create a `.env` file in the root directory of your project to store your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

3. **Run with Docker**

   To build and run the application using Docker:

   ```bash
   docker build -t summarizebot .
   docker run --env-file .env -p 5000:5000 summarizebot
   ```

   The application will be available at `http://localhost:5000`.

4. **Run Locally (Without Docker)**

   If you prefer to run the application without Docker:

   - **Create a virtual environment**:

     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
     ```

   - **Install dependencies**:

     ```bash
     pip install -r requirements.txt
     ```

   - **Run the application**:

     ```bash
     uvicorn app.app:app --host 0.0.0.0 --port 5000
     ```

   Access the application at `http://localhost:5000`.

### **Usage**

1. **Open the Application**: Navigate to `http://localhost:5000` in your web browser.
2. **Enter an Article URL**: In the provided input field, enter the URL of the article you want to summarize.
3. **Get the Summary**: Click "Summarize" to receive a brief summary of the article.

### **Project Structure**

```plaintext
SummarizeBot/
├── app/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── app.py
│   ├── scraper.py
│   └── summarizer.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   ├── __pycache__/
│   ├── test_app.py
│   ├── test_integration.py
│   ├── test_scraper.py
│   └── test_summarizer.py
├── venv/
├── .env
├── .gitignore
├── Dockerfile
└── requirements.txt
```

- **app/**: Contains the main application files (`app.py`, `scraper.py`, `summarizer.py`).
- **templates/**: HTML template for the frontend.
- **static/**: Static files like CSS.
- **tests/**: Test files for the application.
- **docker/**: Contains Docker-related configurations (optional).
- **.env**: Environment variables (ignored in `.gitignore`).
- **Dockerfile**: Docker configuration file, including setting `PYTHONPATH` to `/app`.
- **requirements.txt**: Python dependencies.

### **Testing**

Run the tests using `pytest`. Ensure your virtual environment is active, or if you're inside the Docker container, `PYTHONPATH` is already set:

```bash
pytest tests/
```

### **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request.

### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### **Contact**

For questions or support, please open an issue or contact the repository owner.
