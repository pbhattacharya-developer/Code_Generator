import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
   

def generate_code(user_input, language):
    prompt = f"""
    Generate code in {language} that does the following:

    {user_input}

    Provide only the code, no explanations or comments unless absolutely necessary.
    Don't include any delimiters at the beginning and the ending of the code.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text

def main():
    st.title("Code Generator")
    
    user_input = st.text_input("Enter your query:")
    
    languages = ["Python", "JavaScript", "Java", "SQL", "C++", "C#","Go", "Swift","R", "Ruby"]
    chosen_language = st.selectbox("Choose a programming language:", languages)

    if st.button("Generate Code"):
        generated_code = generate_code(user_input, chosen_language)
        st.subheader("Generated Code:")
        st.code(generated_code)

        extensions = {  # Store extensions in a variable
            "Python": "py",
            "JavaScript": "js",
            "Java": "java",
            "SQL": "sql",
            "C++": "cpp",
            "C#": "cs",
            "Go": "go",
            "Swift": "swift",
            "R": "r",
            "Ruby": "rb",
        }

        extension = extensions.get(chosen_language, "txt")  # Get extension

        file_name = f"generated_code.{extension}"  # *Now* use f-string

        st.download_button(
            label="Download Code",
            data=generated_code,
            file_name=file_name,  # Use the pre-constructed filename
            mime="text/plain"
        )


if __name__ == "__main__":
    main()