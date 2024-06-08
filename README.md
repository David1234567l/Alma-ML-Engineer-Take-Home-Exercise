# Alma-ML-Engineer-Take-Home-Exercise
<img width="1440" alt="Design Workflow" src="https://github.com/David1234567l/Alma-ML-Engineer-Take-Home-Exercise/assets/35432315/d4b56c42-f247-47c9-bf65-67bf2d9f49f8">
### Explanation:

1. **User**: The end user interacts with the system by uploading their CV and receiving the assessment results.
2. **FastAPI Backend**: The main server handling API requests, including receiving the CV and returning results.
3. **LLM GPT-4**: The language model used for extracting relevant information from the CV.
4. **Database**: Optional storage for processed data and assessment results.
5. **Extraction Logic**: The logic for extracting information from the CV using the LLM.
6. **Assessment Logic**: The logic for assessing the extracted information against O-1A criteria.
7. **Store Results**: The process of saving the assessment results to the database.
8. **Return Results**: The final step where the system returns the assessment results to the user.
