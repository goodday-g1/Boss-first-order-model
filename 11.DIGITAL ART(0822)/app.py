<<<<<<< HEAD
from flask import Flask, render_template, Response, request, jsonify, send_from_directory
from camera import VideoCamera
from werkzeug.utils import secure_filename
import os

=======
from flask import Flask, render_template, Response, request, jsonify, send_from_directory, send_file 
from camera import VideoCamera
from werkzeug.utils import secure_filename
import os
import uuid
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return render_template("/index.html")



@app.route('/style')
def style():
    return render_template("/generic.html")
=======
    return render_template("/home.html")

@app.route('/style')
def style():
    return render_template("/style.html")
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813

@app.route('/style1', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['upload-file']
        if file:
            filename = secure_filename(file.filename)
<<<<<<< HEAD
            file.save(os.path.join(os.getcwd()+"/my_photographs1/", "1.jpg"))
            tasks = []

            return jsonify({'tasks': tasks})
=======
            file.save(os.path.join(os.getcwd()+"/my_photographs1/", filename))
            
            return jsonify({'filename': filename})
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813

@app.route('/style2/<param>', methods=['GET'])
def style2(param) ->str:
    # param = request.form['id']
    print(param)
    # if __name__ == '__main__':
    #     os.system("python main.py --model_name=model_"+param+ " --phase=inference --image_size=1280 --ii_dir ./my_photographs1/ --save_dir=./save_processed_images_here/")
    os.system("python main.py --model_name=model_"+param+ " --phase=inference --image_size=1280 --ii_dir ./my_photographs1/ --save_dir=./save_processed_images_here/")
<<<<<<< HEAD
    return param , " ajax"

@app.route('/file/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='save_processed_images_here', filename=filename)
=======
    UUnumber= uuid.uuid1()
    return jsonify({'UUnumber': UUnumber})

@app.route('/file/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # return send_from_directory(directory='save_processed_images_here', filename=filename, as_attachment=True)
    return send_file(os.path.join('save_processed_images_here', filename[:-4]+'_stylized.jpg'), as_attachment=True)
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813

##################################################################################
@app.route('/style_video')
def style_video():
    return render_template("/style_video.html")

def style_gen(style_camera):
    while True:
        frame = style_camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/style_video_feed')
def style_video_feed():
    return Response(style_gen(StyleVideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')
##################################################################################

<<<<<<< HEAD
@app.route('/firstordervideo')
def first():
    return render_template("/generic1.html")
=======
@app.route('/first')
def first():
    return render_template("/firstordervideo.html")
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813

####################################################################################
@app.route('/faceswap')
def faceswap():
<<<<<<< HEAD
    return render_template("/generic0.html")
=======
    return render_template("/faceswap.html")
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813
####################################################################################

@app.route('/faceswap_video')
def faceswap_video():
    return render_template("/faceswap_video.html")

#######################################################################################
@app.route('/about')
def about():
    return render_template("/about.html")

<<<<<<< HEAD
from flask import send_from_directory


=======
>>>>>>> 71ce120aec8805419ae83cc01a1b3afd919cf813
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
