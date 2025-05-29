# Speech Emotion Recognition (SER) Project using Flask

## Description
This project implements a Speech Emotion Recognition (SER) system. It explores traditional acoustic features and deep learning embeddings from Wav2Vec 2.0 to classify emotions (Angry, Happy, Sad, Neutral, Fearful, Disgusted, Surprised) from input audio files. The system is deployed as a web application using the Flask framework.





---

## 🖼️ Demo Screenshots

Here are screenshots of the Flask web application:



** Emotion Prediction Example:**
![Flask SER App - Prediction Example][(![image](https://github.com/user-attachments/assets/ab50f8de-b000-4a89-b422-48ebf8c57d3d)](https://github.com/Abdessabour2/Speech_emotion_prediction/blob/main/146d1388145c2d108be03ce5cd64c57e5ba80ef3.png)
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
           
