#Saving model,Encoder,scaler for production
import os
import pickle

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Save properly
pickle.dump(scaler, open("models/scaler.pkl", 'wb'))
pickle.dump(model_gbc, open("models/model_gbc.pkl", 'wb'))