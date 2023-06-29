from flask import Blueprint, render_template, request
from website.utils.leaf_disease_detection import detect_leaf_disease

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        file.save('website/static/uploads/image.jpeg')  # Save the uploaded file
        result = detect_leaf_disease('website/static/uploads/image.jpeg', 'model.h5')  # Call the leaf disease detection function
        return render_template('home.html', result=result)

    return render_template('home.html')

