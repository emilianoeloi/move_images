from flask import Flask, render_template, jsonify
import face_recognition

app = Flask(__name__)

@app.route('/')
def index():
    # Carrega a imagem de referência e identifica os rostos
    ref_image = face_recognition.load_image_file('static/images/model_1.JPG')
    ref_face_locations = face_recognition.face_locations(ref_image)
    ref_face_landmarks = face_recognition.face_landmarks(ref_image)

    # Assumindo um único rosto na imagem de referência para simplificação
    ref_data = {
        "BoundingBox": ref_face_locations[0] if ref_face_locations else None,
        "Landmarks": ref_face_landmarks[0] if ref_face_landmarks else None
    }

    # Carrega a imagem a ser identificada de forma similar
    ident_image = face_recognition.load_image_file('static/images/model_2.JPG')
    ident_face_locations = face_recognition.face_locations(ident_image)
    ident_face_landmarks = face_recognition.face_landmarks(ident_image)

    # Assumindo um único rosto na imagem identificada para simplificação
    ident_data = {
        "BoundingBox": ident_face_locations[0] if ident_face_locations else None,
        "Landmarks": ident_face_landmarks[0] if ident_face_landmarks else None
    }

    # Passa ambos os dados para o template
    return render_template('index.html', ref_data=ref_data, ident_data=ident_data)

if __name__ == '__main__':
    app.run(debug=True)
