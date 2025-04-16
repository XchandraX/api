import pandas as pd
import json
import sys
import numpy as np
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
    
    place_id = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    place = df[df['place_id'] == place_id]
    
    if place.empty:
        print(json.dumps(None))
        sys.exit()
    
    place = place.replace({np.nan: None})
    
    result = place[['place_name', 'category', 'city', 'rating', 'place_description', 'place_img', 'gallery_photo_img1', 'gallery_photo_img2', 'gallery_photo_img3', 'place_map']].to_dict(orient="records")
    
    print(json.dumps(result[0]))
    
except Exception as e:
    print(json.dumps({"error": str(e)}))