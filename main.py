from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
from wordcloud import WordCloud
from io import BytesIO

app = Flask(__name__)
api = Api(app)

class WordCloudAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('text', required=True)  # add userId arg
        args = parser.parse_args()  # parse arguments to dictionary
        # Generate a word cloud image
        wordcloud = WordCloud(background_color="white", min_font_size=2, max_font_size=50, stopwords="", relative_scaling=1).generate_from_text(args['text'])
        img_io = BytesIO()
        pil_img = wordcloud.to_image()
        pil_img.save(img_io, 'JPEG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')

api.add_resource(WordCloudAPI, '/wordcloud')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)  # run our Flask app
