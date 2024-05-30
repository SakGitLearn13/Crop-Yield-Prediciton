from flask import Flask, jsonify, request, render_template
import pandas as pd
import json
import pickle
import datetime

# loading models
dtr = pickle.load(open('model/dtr.pkl', 'rb'))
preprocessor = pickle.load(open('model/preprocessor.pkl', 'rb'))

# creating flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        State = request.form['State']
        District = request.form['District']
        Season = request.form['Season']
        Crop = request.form['Crop']
        Fertilizer, Pesticide = get_fertilizer_pesticide_data(State, District, Crop, Season)
        Avg_rainfall = request.form['Avg_rainfall']
        Temperature = request.form['Temperature']
        Area = request.form['Area']
        
        # Get current year
        Year = get_current_year()

        # Create a DataFrame with the correct column names
        feature_dict = {
            'State': [State],
            'District': [District],
            'Year': [Year],
            'Season': [Season],
            'Crop': [Crop],
            'Fertilizer': [Fertilizer],
            'Pesticide': [Pesticide],
            'Avg_rainfall': [Avg_rainfall],
            'Temperature': [Temperature],
            'Area': [Area],
        }
        features = pd.DataFrame(feature_dict)
        print(feature_dict)
        # Preprocessing of user input
        transformed_features = preprocessor.transform(features)

        predicted_value = dtr.predict(transformed_features).reshape(1, -1)
        return render_template('index.html', result=predicted_value)

# Route for fetching distinct state names
@app.route('/get_state', methods=['GET'])
def get_state():
    data = pd.read_csv('data/Crop_Data.csv')
    states = data['State'].unique().tolist()
    return jsonify(states=states)

@app.route('/get_districts', methods=['GET'])
def get_districts():
    state = request.args.get('state')
    
    # Load state_districts from JSON file
    with open('data/state_districts.json', 'r') as file:
        state_districts = json.load(file)
        
    districts = state_districts.get(state, [])
    return jsonify(districts=districts)


# Route for fetching distinct crop names
@app.route('/get_crops', methods=['GET'])
def get_crops():
    data = pd.read_csv('data/Crop_Data.csv')
    crops = data['Crop'].unique().tolist()
    return jsonify(crops=crops)

# Function to get current year
def get_current_year():
    return datetime.datetime.now().year

# Function to get fertilizer and pesticide data
def get_fertilizer_pesticide_data(State, District, Crop, Season):

    # Load the JSON file into a DataFrame
    grouped_df = pd.read_json('data\grouped_df.json')

    # Filter data for the specified State, District, Crop, and Season
    filtered_data = grouped_df[(grouped_df['State'] == State) & 
                               (grouped_df['District'] == District) & 
                               (grouped_df['Crop'] == Crop) &
                               (grouped_df['Season'] == Season)]

    if not filtered_data.empty:
        # Extract the Fertilizer and Pesticide values
        avg_fertilizer = filtered_data.iloc[0]['Avg_Fertilizer']
        avg_pesticide = filtered_data.iloc[0]['Avg_Pesticide']
        return avg_fertilizer, avg_pesticide
    else:
        return None, None
    
    return fertilizer_data, pesticide_data

# python main
if __name__ == '__main__':
    app.run(debug=True)
