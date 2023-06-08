# What-s-the-sound-like-
Machine learning model to classify the musical instrument with data augmentation

## Description:
This repository contains a web application developed for musical instrument classification using machine learning techniques. The application is built using Streamlit and deployed with Docker. The project utilizes the IRMAS dataset, which consists of audio recordings of 11 different musical instruments, including human voice.
## Model used:
The machine learning models used for training the dataset are k-Nearest Neighbors (kNN) and Support Vector Machine (SVM) classifiers from scikit-learn. The models achieved an accuracy of 87% in instrument classification.

To improve the performance and diversity of the dataset, data augmentation techniques were applied using the librosa library. These techniques included stretching the wavelength, time shifting the audio data, and adding background noise.

## ## Web App Usage
To use the web app, users can record an audio sample of a solo instrument and submit it for prediction. The deployed model will classify the instrument based on the input audio.

To use the web app, follow the steps below:
1. Install Docker: Visit the official Docker website (https://www.docker.com/) and follow the instructions to download and install Docker for your operating system.
2. Build the Docker image: Open a terminal or command prompt, navigate to the project directory, and run the following command:
 ```  
  docker build -t Dockerfile .
  docker run -it -p 8501:8501 streamlitwebapp:latest
  
```
This will start the web app on port 8501. You can access the application by opening a web browser and navigating to `http://localhost:8501`.

## Contributing

If you'd like to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch with your changes.
- Submit a pull request.

## License

This project is licensed under the GNU License. See the LICENSE file for more information.
