# Crop Yield Prediction Project

## Overview 

This project aims to predict crop yields based on various factors such as location, weather conditions, and agricultural inputs. The prediction model is trained on a dataset containing information about crops, agricultural inputs, and environmental conditions.

## Dataset

The dataset used in this project is stored in the `Data` directory and includes the following files:

- `Crop_Data.csv`: Contains information about crop production, agricultural inputs, and environmental conditions.
- `state_districts.json`: Provides a mapping of states to their respective districts.

## Preprocessing

### Data Cleaning

- Removed irrelevant columns such as `Season`.
- Handled missing values and outliers.
- Transformed categorical variables into numerical representations using one-hot encoding.

### Feature Engineering

- Extracted additional features from the dataset, such as the `Year` and `Area` of cultivation.

## Model Training

The project utilizes several regression algorithms for yield prediction:

- **Linear Regression**
- **Lasso Regression**
- **Ridge Regression**
- **K-Nearest Neighbors Regression**
- **Decision Tree Regression**
- **Gradient Boosting Regression**
- **Random Forest Regression**

The models are trained and evaluated using the processed dataset to determine the best-performing algorithm.

## Frontend

The frontend of the project is implemented using Flask, a Python web framework. The frontend files are located in the `templates` directory and include:

- `index.html`: HTML template for the user interface.
- `static/style.css`: CSS file for styling the HTML template.
- `static/script.js`: JavaScript file for client-side scripting.

## Backend

The backend of the project is implemented using Flask as well. The main backend file is `app.py`, which contains the server-side logic for handling user requests and interfacing with the prediction model.

## Libraries Used

The project utilizes the following libraries:

- **pandas**: For data manipulation and preprocessing.
- **scikit-learn**: For machine learning algorithms and evaluation metrics.
- **Flask**: For building the web application.
- **pickle**: For serializing and deserializing Python objects (e.g., trained models).
- **seaborn** and **matplotlib**: For data visualization.

## Usage

To run the project locally:

1. Install the required Python libraries: `pip install -r requirements.txt`
2. Run the Flask app: `python app.py`
3. Access the web interface by navigating to `http://localhost:5000` in your web browser.

## Contributors

- [Saksham Srivastava](https://github.com/SakGitLearn13)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
