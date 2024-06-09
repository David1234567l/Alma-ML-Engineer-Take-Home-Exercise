# O-1A Visa Assessment

This project provides an API to assess how qualified a person is for an O-1A immigration visa based on their CV (.txt format)   

## Project Structure 

```plaintext
O1a-visa-assessment/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
├── data/
│   └── the_sample_cv.txt
├── README.md
├── requirements.txt
└── .env

File Descriptions
main.py: The main entry point of the FastAPI application. 
models.py: Define data models (e.g., for a database). 
schemas.py: Define Pydantic models for request and response validation.
utils.py: Utility functions, such as the functions to interact with the OpenAI API and to assess qualifications.
README.md: Instructions on how to set up and run the application. 
requirements.txt: List of dependencies required for the project. 
.env: Environment variables file to store the OpenAI API key.
 ``` 
<img width="1440" alt="Design Workflow" src="https://github.com/David1234567l/O1A-visa-assesment/assets/35432315/41224e2f-6e62-48de-9da1-52876dcd0a1b">

 Explanation:

1. **User**: The end user interacts with the system by uploading their CV and receiving the assessment results.
2. **FastAPI Backend**: The main server handling API requests, including receiving the CV and returning results.
3. **LLM GPT-4**: The language model used for extracting relevant information from the CV.
4. **Database**: Optional storage for processed data and assessment results.
5. **Extraction Logic**: The logic for extracting information from the CV using the LLM.
6. **Assessment Logic**: The logic for assessing the extracted information against O-1A criteria.
7. **Store Results**: The process of saving the assessment results to the database.
8. **Return Results**: The final step where the system returns the assessment results to the user.

## Setup
## 1.) Clone the repository:

git clone https://github.com/David1234567l/O1A-visa-assesment.git  
cd O1A-visa-assesment
## 2.) Install the dependencies:

pip install -r requirements.txt
## Set up your OpenAI API key:  

## 3.) Create a .env file in the root directory and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key  
## 4.) Run the application:

uvicorn app.main:app --reload   
The API will be available at http://127.0.0.1:8000 
## Usage 
## Eample using cURL:  
You can upload a CV in .txt format through the /upload_cv/ endpoint. The API will return a JSON response with the assessment results.  
curl -X POST "http://127.0.0.1:8000/upload_cv/" -F "file=@/path/to/your/cv.pdf"
## Example using a web form:
## Create a simple HTML file to upload a CV:


```plaintext <!DOCTYPE html>
<!DOCTYPE html> 
<html>
<body>

<h2>Upload CV</h2>
<form action="http://127.0.0.1:8000/upload_cv/" method="post" enctype="multipart/form-data">
  <label for="file">Choose CV:</label>
  <input type="file" id="file" name="file"><br><br>
  <input type="submit" value="Upload CV">
</form>

</body>
</html>

```
## Output (.json format)  

### 1. Extracted Information

The extracted information is evaluated based on the following O-1A visa criteria:
- Awards
- Membership
- Press
- Judging
- Original Contribution
- Scholarly Articles 
- Critical Employment 
- High Remuneration  

Each criterion's information is extracted from the CV using GPT-4. The output should provide clear and concise information for each category.  

### 2. Assessment

The assessment is evaluated based on predefined thresholds:
- **Low:** 1
- **Medium:** 2
- **High:** 3  

The application assigns a qualification level (low, medium, high) based on the number of relevant entries for each criterion. The higher the number of relevant entries, the higher the qualification level.   
 
