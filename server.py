from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

popular_constellations = [
    {
        'id': 1,
        'name': 'Ursa Major (Big Dipper)',
        'season': 'Spring',
        'hemisphere': 'Northern',
        'number of stars': '19',
        'brightest star': 'Alioth',
        'characteristics': 'The Big Dipper is one of the most recognizable constellations in the sky. It is a circumpolar constellation, meaning it is visible year-round in the Northern Hemisphere. The Big Dipper is part of the Ursa Major constellation, which is the third largest constellation in the sky. The Big Dipper is made up of seven bright stars that form a shape that looks like a large ladle or dipper. The two stars that form the front of the ladle are called the Pointers because they point to the North Star, Polaris. The Big Dipper is also known as the Plough in the United Kingdom and Ireland.',
        'image': './media/big-dipper-ss.png',
        'namesake': 'The Big Dipper is named after its resemblance to a large ladle or dipper. The word "dipper" comes from the Old English word "dyppan," which means "to dip." The word "ladle" comes from the Old English word "hlædel," which means "a vessel for drawing out liquid." The Big Dipper is also known as the Plough in the United Kingdom and Ireland.',               
    },
        {
        'id': 2,
        'name': 'Ursa Minor (Small Dipper)',
        'season': 'Spring',
        'hemisphere': 'Northern',
        'number of stars': '19',
        'brightest star': 'Alioth',
        'characteristics': 'info about small dipper',
        'image': './media/big-dipper-ss.png',
        'namesake': 'info about name',               
    },
    {
        'id': 3,
        'name': 'Cygnus (Northern Cross)',
        'season': 'Summer',
        'hemisphere': 'Northern',
        'number of stars': '10',
        'brightest star': 'Deneb',
        'characteristics': 'Cygnus is a prominent constellation in the Northern Hemisphere. It is known for its distinctive shape, which resembles a cross or a swan in flight. Cygnus is also known as the Northern Cross because of its shape. The constellation is home to several bright stars, including Deneb, the brightest star in Cygnus. Cygnus is part of the Hercules family of constellations and is located near the Summer Triangle, a prominent asterism in the summer sky. Cygnus is best seen in the summer months in the Northern Hemisphere.',
        'image': './media/cygnus-ss.png',
        'namesake': 'Cygnus is named after the Latin word for swan. In Greek mythology, Cygnus is associated with several myths, including the story of Zeus and Leda. According to legend, Zeus transformed himself into a swan to seduce Leda, the queen of Sparta. The union between Zeus and Leda produced several children, including Helen of Troy and the twins Castor and Pollux. Cygnus is also associated with the story of Orpheus, a legendary musician who was transformed into a swan after his death.',
    },
    {
        'id': 4,
        'name': 'Cassiopeia',
        'season': 'Fall',
        'hemisphere': 'Northern',
        'number of stars': '8',
        'brightest star': 'Schedar',
        'characteristics': 'Cassiopeia is a circumpolar constellation, meaning it is visible year-round in the Northern Hemisphere. It is named after the queen of Aethiopia in Greek mythology. Cassiopeia is known for its distinctive "W" shape, which is formed by five bright stars. The constellation is located near the North Star, Polaris, and is part of the Perseus family of constellations. Cassiopeia is one of the 48 constellations listed by the 2nd-century astronomer Ptolemy and remains one of the 88 modern constellations recognized by the International Astronomical Union.',
        'image': './media/cassiopea-ss.png',
        'namesake': 'Cassiopeia is named after the queen of Aethiopia in Greek mythology. According to legend, Cassiopeia was the wife of King Cepheus and the mother of Princess Andromeda. She was known for her beauty and vanity, which ultimately led to her downfall. Cassiopeia was placed in the sky as a punishment for her arrogance, where she is forced to circle the North Star for eternity. The constellation is also known as the "Celestial W" because of its distinctive shape.',
    },
    {
       'id': 5,
        'name': 'Orion',
        'season': 'Spring',
        'hemisphere': 'Northern',
        'number of stars': '19',
        'brightest star': 'Alioth',
        'characteristics': 'info',
        'image': './media/big-dipper-ss.png',
        'namesake': 'info',               
    },
]

@app.route('/')
def welcome():
   return render_template('welcome.html')   

@app.route('/learn')
def learn():
   return render_template('learn.html')   

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')   

@app.route('/search')
def search():
   pass

@app.route('/hello')
def hello():
   return render_template('welcome.html')

# VIEW
@app.route('/view/<int:id>')
def view_item(id):
    item = next((item for item in popular_constellations if item['id'] == id), None)
    if item:
        return render_template('view.html', item=item)
    else:
        return "Item not found", 404



if __name__ == '__main__':
   app.run(debug = True)
