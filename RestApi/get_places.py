import pandas as pd
import json
import pickle
import os

try:
    # Mendapatkan path absolut ke direktori model
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '../models/recommendation_model.pkl')
    
    # Load model data
    with open(model_path, 'rb') as file:
        model_data = pickle.load(file)
    
    df = model_data['df']  # Ambil dataframe dari model
    
    selected_columns = ['place_id', 'place_name', 'category', 'city', 'rating', 'place_img']
    df_sample = df[selected_columns].head(6)
    
    places = df_sample.to_dict(orient="records")
    print(json.dumps(places, indent=4))

except Exception as e:
    print(json.dumps({"error": str(e)}))