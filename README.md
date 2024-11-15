# QueryPDF

## About the Project:
**QueryPDF** is a web app where users can upload PDF files and ask questions based on the content of those PDFs. The app extracts text from the PDFs and answers questions in real time.

## Features:
- **Upload PDFs:** You can upload your PDF files to the system.
- **Real-Time Q&A:** Ask questions about the content of the PDF and get answers immediately.
- **Rate Limiting:** Limits the number of requests to avoid overloading the system.
- **Text Extraction:** The system automatically extracts text from the PDF to answer questions.

## Technologies Used:
- **FastAPI:** To create the web API.
- **WebSocket:** To chat in real-time (Q&A).
- **SQLAlchemy:** For database interaction.
- **Pydantic:** For data validation.
- **PostgreSQL:** The database to store PDF data.
- **Docker:** To run the app in a container.

## How to Set Up the Project

### Prerequisites:
Make sure you have these installed:
- Python 3.x
- PostgreSQL (or another database)
- Docker (optional)

### 1. Clone the Repo:
First, clone the project to your computer:
```bash
git clone https://github.com/Abhigyan2212/QueryPDF.git
cd QueryPDF
Set Up Virtual Environment:
It’s recommended to use a virtual environment. To set it up:

2. For Windows:
python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies:
Next, install the project requirements:
pip install -r requirements.txt

4. Set Up the Database:
Update the .env file with your PostgreSQL database details:
DATABASE_URL=postgresql://username:password@localhost/database_name

5. Migrate the Database:
Run this command to set up the database:
python app/models.py

Run the App:
Start the app using this command:
uvicorn app.main:app --reload
Now, you can access the app at http://127.0.0.1:8000.

How to Use the App:
1. Upload a PDF:
Send a POST request to /upload with your PDF file.
The system will extract text from the PDF.
2. Ask Questions:
Open a WebSocket connection to /query.
Ask a question about the uploaded PDF and get an answer.
3. Rate Limiting:
The system limits how many requests you can send within a certain time to avoid overload.
API Endpoints:
1. POST /upload
Upload a PDF file to the app.
Response: It will confirm if the upload was successful.
2. WebSocket /query
Ask a question about the uploaded PDF.
Response: The system will send an answer based on the PDF content.
Testing:
You can test the app using tools like Postman or any WebSocket client.

To run the tests, use: pytest

Demo:
If available, you can see a video demo of the app’s features.

Deployment:
For deployment, you can use Heroku, AWS, or Docker. If using Docker, run:

docker build -t querypdf .
docker run -p 8000:8000 querypdf

License:
This project is licensed under the MIT License.

---

### How to Use:

- Replace sections like **"Update the `.env` file with your PostgreSQL database details"** with your own specifics if necessary.
- Add more details or instructions for your app as needed.
- You can easily update the repository link, deployment info, or any section as the project evolves.

This structure allows easy updates while keeping everything organized!

