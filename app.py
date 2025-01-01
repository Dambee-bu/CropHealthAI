{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOfabzwdih4qZ/Hsm5q0+0z"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":7,"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":646},"id":"oDyLQMa8RTFk","executionInfo":{"status":"ok","timestamp":1735662399309,"user_tz":0,"elapsed":6462,"user":{"displayName":"Ishmael Manne","userId":"18186348154757738609"}},"outputId":"46e70167-a36e-4e6e-99bd-ab964731e8e1"},"outputs":[{"output_type":"stream","name":"stderr","text":["WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"]},{"output_type":"stream","name":"stdout","text":["Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n","Colab notebook detected. To show errors in colab notebook, set debug=True in launch()\n","* Running on public URL: https://0f5b3efaaf510764c2.gradio.live\n","\n","This share link expires in 72 hours. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)\n"]},{"output_type":"display_data","data":{"text/plain":["<IPython.core.display.HTML object>"],"text/html":["<div><iframe src=\"https://0f5b3efaaf510764c2.gradio.live\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"]},"metadata":{}}],"source":["#!pip install gradio\n","#!pip install tensorflow\n","\n","from IPython import get_ipython\n","from IPython.display import display\n","# %%\n","import gradio as gr\n","from tensorflow.keras.models import load_model\n","from tensorflow.keras.preprocessing.image import img_to_array, load_img\n","import numpy as np\n","\n","# Load the trained CNN model\n","# Mount Google Drive\n","from google.colab import drive\n","drive.mount('/content/drive')\n","\n","# ... (Import necessary libraries)\n","\n","# Load the trained CNN model with the correct path\n","model_path = '/content/drive/MyDrive/Colab Notebooks/classifier.h5'  # Update with your actual folder name if different\n","model = load_model(model_path)\n","\n","# Define the classes (update these based on your model's classes)\n","classes = [\n","    \"Corn_(maize): Healthy\",\n","    \"Corn_(maize): Cercospora_leaf_spot Gray_leaf_spot\",\n","    \"Corn_(maize): Common_rust\",\n","    \"Corn_(maize): Northern_Leaf_Blight\",\n","    \"Pepper,_bell: Healthy\",\n","    \"Pepper,_bell: Bacterial_pepper_spot\",\n","    \"Tomato: healthy\",\n","    \"Tomato: Bacterial_spot\",\n","    \"Tomato: Early_blight\",\n","    \"Tomato: Late_blight\",\n","    \"Tomato: Leaf_mold\",\n","    \"Tomato: Septoria_leaf_spot\",\n","    \"Tomato: Spider_mites Two-spotted_spider_mite\",\n","    \"Tomato: Target_spot\",\n","    \"Tomato: Tomato_Yellow_Leaf_curl_virus\",\n","    \"Tomato: Tomato_mosaic_virus\",\n","]\n","\n","# Prediction function\n","def predict_disease(image):\n","    \"\"\"\n","    Predict plant disease from an uploaded image.\n","    \"\"\"\n","    try:\n","        # Resize image to match model input size\n","        image = image.resize((64, 64))  # Ensure this matches your model's input shape\n","        image_array = img_to_array(image)\n","        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension\n","        image_array = image_array / 255.0  # Normalize pixel values\n","\n","        # Make prediction\n","        prediction = model.predict(image_array)\n","        predicted_class = np.argmax(prediction)  # Get index of max probability\n","        confidence = np.max(prediction)  # Get probability of prediction\n","\n","        # Return the class label and confidence\n","        return f\"{classes[predicted_class]} (Confidence: {confidence:.2f})\"\n","\n","    except Exception as e:\n","        return f\"Error: {str(e)}\"\n","\n","# Gradio interface\n","interface = gr.Interface(\n","    fn=predict_disease,\n","    inputs=gr.Image(type=\"pil\"),  # Accepts an image file\n","    outputs=\"text\",              # Outputs a text result\n","    title=\"Plant Disease Detection\",\n","    description=\"Upload an image of a corn, pepper, or tomato leaf to identify its health status or disease.\"\n",")\n","\n","# Launch the Gradio app\n","if __name__ == \"__main__\":\n","    interface.launch(share=True)\n","\n"]}]}