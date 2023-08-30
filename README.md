# PDF_langchain

This is a Streamlit web application that allows you to query content from a PDF document using Langchain's embeddings and question-answering capabilities.

## Getting Started

1. **Installation:**
   - Clone this repository to your local machine.
   - Install the required Python packages using the following command:
     ```
     pip install -r requirements.txt
     ```

2. **Running the App:**
   - In your terminal, navigate to the project directory.
   - Run the Streamlit app using the command:
     ```
     streamlit run streamlit_app.py
     ```

3. **Usage:**
   - Once the app is running, you'll see a sidebar where you can upload a PDF file.
   - After uploading a PDF, enter a question related to the PDF content in the text input field.
   - Click the "Get Answer" button to receive an answer from the chatbot.

## Configuration

- Set your OpenAI API key by replacing `"Your key"` in the `streamlit_app.py` file with your actual API key.

## Dependencies

- Streamlit
- PyPDF2
- langchain

## Results 

<img width="887" alt="Capture1" src="https://github.com/aybstain/PDF_langchain/assets/103702856/8acf340b-6738-498a-8d90-e33ae47133d4">

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
