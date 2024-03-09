from flask import Flask, render_template, jsonify
import face_recognition

app = Flask(__name__)

@app.route('/')
def index():
    
    ref_image = face_recognition.load_image_file('static/images/model_1.jpg')
    ref_face_locations = face_recognition.face_locations(ref_image)
    ref_face_landmarks = face_recognition.face_landmarks(ref_image)

    ref_data = {
        "BoundingBox": ref_face_locations[0] if ref_face_locations else None,
        "Landmarks": ref_face_landmarks[0] if ref_face_landmarks else None
    }

    ident_image = face_recognition.load_image_file('static/images/model_2.jpg')
    ident_face_locations = face_recognition.face_locations(ident_image)
    ident_face_landmarks = face_recognition.face_landmarks(ident_image)

    ident_data = {
        "BoundingBox": ident_face_locations[0] if ident_face_locations else None,
        "Landmarks": ident_face_landmarks[0] if ident_face_landmarks else None
    }

    return render_template('index.html', ref_data=ref_data, ident_data=ident_data)

if __name__ == '__main__':
    app.run(debug=True)
