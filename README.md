# Speech Emotion Recognition (SER) Project using Flask

## Description
This project implements a Speech Emotion Recognition (SER) system. It explores traditional acoustic features and deep learning embeddings from Wav2Vec 2.0 to classify emotions (Angry, Happy, Sad, Neutral, Fearful, Disgusted, Surprised) from input audio files. The system is deployed as a web application using the Flask framework.





---

## 🖼️ Demo Screenshots

Here are screenshots of the Flask web application:



** Emotion Prediction Example:**
![Flask SER App - Prediction Example](![image](https://github.com/user-attachments/assets/ab50f8de-b000-4a89-b422-48ebf8c57d3d)
)
*Figure 2: Example of a predicted emotion displayed to the user after processing an audio file.*



---


---

## 🛠️ Technology Stack
* **Programming Language:** Python 3.8+
* **Core Libraries:**
    * `TensorFlow` / `Keras` (for ANN/CNN model building)
    * `Hugging Face Transformers` (for Wav2Vec 2.0)
    * `Librosa` (for audio processing, feature extraction)
    * `Scikit-learn` (for Random Forest, metrics)
    * `Flask` (for the web application backend)
* **Frontend:** HTML, CSS, JavaScript (within Flask templates)
* **Notebooks:** Jupyter Notebook (`.ipynb`)

---

## ⚙️ Setup and Installation

Follow these steps to set up the development environment and run the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/Speech_emotion_prediction.git
    cd Speech_emotion_prediction
    ```
    *(Replace `[YOUR_USERNAME]` with your GitHub username.)*

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv 
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows:
    # .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    Navigate into the `flask application` directory if your `requirements.txt` is there, or ensure it's in the root.
    ```bash
    pip install -r requirements.txt 
    ```

4.  **Model Placement:**
    * The trained model (e.g., `your_model.h5` or `your_model.pth`) be placed inside the `flask application/model/` directory.
---

## ▶️ How to Run the Flask Application

1.  **Navigate to the Flask application directory:**
    ```bash
    cd Speech_emotion_prediction/flask application
    ```

2.  **Run the Flask application:**
    *(Assuming your main Flask script is named `app.py` or similar inside this folder. Please verify and change `app.py` if needed.)*
    ```bash
    python app.py 
    ```

3.  Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in your Flask app's console output).

---

## 📁 Project File Structure

Based on your screenshots, the structure is approximately:
Okay, thank you for sharing the screenshots of your GitHub repository structure! This is very helpful for tailoring the README.md to accurately reflect your project.

Based on your images (image_d73dda.png and image_d73da2.png) and the LaTeX code for your report (especially the deployment screenshots like flask.png, sup.png, etc.), here's a revised and more detailed README.md example.

Please take the following steps:

Replace the content of your current README.md file in your GitHub repository with the text below.
Create a folder named screenshots in the root directory of your GitHub repository.
From your LaTeX report's figures, choose 1 or 2 best screenshots of your Flask application. For example:
Your flask.png (which shows the overall UI) could be renamed to flask_app_main_interface.png.
One of sup.png, qjqj.png, or wllw.png (which show a prediction) could be renamed to flask_app_prediction_example.png.
Place these renamed image files into the screenshots folder.
Review and update all placeholder text (like [YOUR_USERNAME], URLs, and specific script names if different).
Here's the updated README.md content:

Markdown

# Speech Emotion Recognition (SER) Project using Flask

## Description
This project implements a Speech Emotion Recognition (SER) system. It explores traditional acoustic features and deep learning embeddings from Wav2Vec 2.0 to classify emotions (Angry, Happy, Sad, Neutral, Fearful, Disgusted, Surprised) from input audio files. The system is deployed as a web application using the Flask framework.

---

## 🚀 Live Demo
*(If you have a live demo deployed, add the link here. If not, you can state "The application can be run locally following the instructions below.")*
* **Working Demo Link:** [Link to your deployed Flask application (if any)](YOUR_DEPLOYED_APP_URL_HERE) OR "Demo is run locally."

---

## 🎬 Video Presentation
Watch our 7-minute video presentation that covers the project background, environment setup, code explanation, model details, and a walkthrough of the Flask application:

[![Watch the Video](https://img.youtube.com/vi/YOUR_YOUTUBE_VIDEO_ID/hqdefault.jpg)](https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID)
*(**Reminder:** Upload your video (e.g., to YouTube), get its ID, and replace `YOUR_YOUTUBE_VIDEO_ID` in both URLs. Alternatively, create a thumbnail, add it to `./screenshots/video_thumbnail.png` and use: `[![Video Presentation](./screenshots/video_thumbnail.png)](YOUR_VIDEO_LINK)`)*

---

## 🖼️ Demo Screenshots

Here are screenshots of the Flask web application:

**1. Main Application Interface:**
![Flask SER App - Main Interface](./screenshots/flask_app_main_interface.png)
*Figure 1: The main interface of the Flask application, allowing users to upload a .wav file.*

**2. Emotion Prediction Example:**
![Flask SER App - Prediction Example](./screenshots/flask_app_prediction_example.png)
*Figure 2: Example of a predicted emotion displayed to the user after processing an audio file.*

*(**Instructions:** As mentioned above, please add your chosen `flask.png` and one other UI screenshot to the `screenshots` folder and ensure these paths/filenames match. Update captions as needed.)*

---

## 📋 Table of Contents
* [Project Overview](#description)
* [Live Demo](#-live-demo)
* [Video Presentation](#-video-presentation)
* [Demo Screenshots](#-demo-screenshots)
* [Technology Stack](#-technology-stack)
* [Setup and Installation](#-setup-and-installation)
* [How to Run the Flask Application](#-how-to-run-the-flask-application)
* [Project File Structure](#-project-file-structure)
* [Source Code Documentation](#-source-code-documentation)

---

## 🛠️ Technology Stack
* **Programming Language:** Python 3.8+
* **Core Libraries:**
    * `TensorFlow` / `Keras` (for ANN/CNN model building)
    * `Hugging Face Transformers` (for Wav2Vec 2.0)
    * `Librosa` (for audio processing, feature extraction)
    * `Scikit-learn` (for Random Forest, metrics)
    * `Flask` (for the web application backend)
* **Frontend:** HTML, CSS, JavaScript (within Flask templates)
* **Notebooks:** Jupyter Notebook (`.ipynb`)

---

## ⚙️ Setup and Installation

Follow these steps to set up the development environment and run the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/Speech_emotion_prediction.git
    cd Speech_emotion_prediction
    ```
    *(Replace `[YOUR_USERNAME]` with your GitHub username.)*

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv 
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows:
    # .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    Navigate into the `flask application` directory if your `requirements.txt` is there, or ensure it's in the root.
    ```bash
    pip install -r requirements.txt 
    ```
    *(**Important:** Ensure you have a `requirements.txt` file in your repository. If it's inside the `flask application` folder, users should `cd flask application` before this step, or you should have one in the root that covers all dependencies including notebook ones.)*

4.  **Model Placement:**
    * The trained model (e.g., `your_model.h5` or `your_model.pth`) should be placed inside the `flask application/model/` directory. If you provide it via a Google Drive link in your report, mention here: "Download the trained model from [Your Google Drive Link] and place it in the `flask application/model/` directory."

---

## ▶️ How to Run the Flask Application

1.  **Navigate to the Flask application directory:**
    ```bash
    cd Speech_emotion_prediction/flask application
    ```

2.  **Run the Flask application:**
    *(Assuming your main Flask script is named `app.py` or similar inside this folder. Please verify and change `app.py` if needed.)*
    ```bash
    python app.py 
    ```

3.  Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in your Flask app's console output).

---

## 📁 Project File Structure

Based on your screenshots, the structure is approximately:

Speech_emotion_prediction/
├── flask application/            # Core web application files
│   ├── pycache/            # Python cache (should be in .gitignore)
│   ├── model/                  # Contains the trained SER model(s)
│   │   └── your_trained_model.h5 # Example model file
│   ├── static/                 # CSS, JavaScript, images for Flask UI
│   │   └── style.css           # Example
│   ├── templates/              # HTML templates for Flask
│   │   └── index.html          # Example
│   ├── uploads/                # Temporary storage for user-uploaded audio (consider .gitignore)
│   ├── app.py                  # Main Flask application script (assumption, please verify name)
│   ├── ... (other .py files specific to Flask app if any) ...
│   └── *.wav                   # Example/test .wav files (e.g., 1001_IOM_NEU_XX.wav)
├── screenshots/                
│   ├── flask_app_main_interface.png
│   └── flask_app_prediction_example.png
├── Wav2Vec2Model.ipynb         # Jupyter Notebook for Wav2Vec2 model exploration/training
├── building_model1.ipynb       # Jupyter Notebook for building/training other models (e.g., traditional)
├── extract_features1.ipynb     # Jupyter Notebook for feature extraction experiments
├── .gitignore                  
└── README.md      
## 📄 Source Code Documentation

* **Inline Comments:** All Python scripts (`.py`) and Jupyter Notebooks (`.ipynb`) are documented with inline comments explaining the logic of functions, classes, and critical code sections.
* **Jupyter Notebooks (located in the root directory):**
    * `extract_features1.ipynb`: Details the process of extracting traditional acoustic features from the audio datasets. Includes visualizations and preprocessing steps for these features.
    * `building_model1.ipynb`: Focuses on training and evaluating models (e.g., Random Forest, initial ANNs) using the traditionally extracted features.
    * `Wav2Vec2Model.ipynb`: Covers the experiments with Wav2Vec 2.0, including loading the pre-trained model, feature embedding extraction, data augmentation strategies specific to these embeddings, and training/fine-tuning deep learning models (ANN/CNN) for emotion classification.
* **Flask Application (`flask application/` directory):**
    * `app.py` (or your main Flask script): This is the entry point for the web application. It defines the Flask routes (URLs), handles HTTP requests, manages file uploads, calls the SER model for predictions using the processed audio, and renders the HTML templates to display results to the user.
    * `model/`: This directory stores the final trained SER model (e.g., the CNN model trained on Wav2Vec2 features) that is loaded by the Flask application for inference.
    * `static/`: Contains static assets like CSS files for styling the web interface, JavaScript files for client-side interactions (if any), and images used in the UI.
    * `templates/`: Holds the HTML files that structure the web pages presented to the user (e.g., the upload form, results page).
    * `uploads/`: This folder is used by the Flask application to temporarily store audio files uploaded by users before they are processed. *(Note: Content in this folder is typically transient and might not need to be version-controlled if cleared regularly).*

---
           
