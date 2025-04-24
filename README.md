# **ResumeAnalyzerMinorProject** 📝🔍

**ResumeAnalyzerMinorProject** is a powerful **Resume Analyzer** tool designed for Bachelor in Computer Engineering Minor Project to help users analyze their resumes, score them, and get career recommendations. It uses **Natural Language Processing (NLP)** and **Machine Learning** algorithms to extract key details from resumes, such as skills, qualifications, and recommends useful courses and YouTube videos to improve the resume.

## **Features**

- **User & Admin Sections**: Two distinct sections for users and admin with login functionality.
- **Resume Score**: Provides a score based on the quality and relevance of the resume.
- **Career Recommendations**: Matches resumes with potential career options.
- **Resume Writing Tips**: Offers tips to enhance your resume.
- **Courses Recommendations**: Recommends courses to improve skills based on resume content.
- **Skills Recommendations**: Suggests skills that should be highlighted in the resume.
- **YouTube Video Recommendations**: Links to useful videos on resume writing and career preparation.

## **Source**
- **User Information Extraction**: Extracts key information from resumes using **PyResparser**.
- **PDF to Text Conversion**: Extracts text from PDF resumes using **PDFMiner**.
- **Resume Classification**: Uses a **KNN Algorithm** for classifying resumes and providing career suggestions, located in **Classifier.py**.

## **Usage**

### Clone the Repository
1. Clone the repo to your local machine:
    ```bash
    git clone https://github.com/your-username/ResumeAnalyzerMinorProject.git
    ```

### Install Dependencies
2. Open **CMD** in your working directory and install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Run the Application
3. **App.py** is the main Python file for the **Streamlit Web Application**.
4. **Courses.py** contains a list of recommended courses and YouTube video links.
5. Download **XAMPP** (or any other control panel) and start the **Apache** and **SQL** services.
6. To run the app, open **CMD** or any IDE, and type:
    ```bash
    streamlit run App.py
    ```

### Directory Structure:
- **Uploaded_Resumes/**: Contains the uploaded resumes.
- **Classifier.py**: The file that contains the **KNN Algorithm** for classification.

## **Contributing**
Feel free to fork the repo and contribute to the project. Pull requests with new features and bug fixes are always welcome!

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Contact**
If you have any questions or suggestions, reach out to me at [Email](mailto:anishchaulagain2058@gmail.com).
