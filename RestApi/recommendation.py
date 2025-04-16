import pandas as pd
import json
import sys
import pickle
import os
import numpy as np

# Mendapatkan path absolut ke direktori model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '../models/recommendation_model.pkl')

# Load model dan data yang diperlukan
try:
    with open(model_path, 'rb') as file:
        model_data = pickle.load(file)
        
    df = model_data['df']  # Dataframe 
    similarity_matrix = model_data['similarity_matrix']  # Matriks similaritas
    
    def get_recommendations(place_index, top_n=5):
        similarity_scores = list(enumerate(similarity_matrix[place_index].toarray().flatten()))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        recommended_indices = [i[0] for i in similarity_scores]
        return recommended_indices

    try:
        place_id = int(sys.argv[1]) if len(sys.argv) > 1 else -1
        place_index = df[df['place_id'] == place_id].index[0]
        recommended_indices = get_recommendations(place_index)
        recommended_places = df.iloc[recommended_indices]
        
        result = recommended_places[['place_id', 'place_name', 'category', 'city', 'rating']].to_dict(orient="records")
        print(json.dumps(result))
    except:
        print(json.dumps([]))

except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)