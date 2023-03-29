import streamlit as st
from PIL import Image
import time


st.header("Gallery of Modern Art")
st.subheader(' ')
st.subheader(' ')
st.subheader(' ')

left, right = st.columns([6,6])

with left:
    image1 = Image.open('/Users/dingma/PycharmProjects/websiteproject/1.jpeg')
    st.image(image1, caption='Henri de Ferrieres')
    image3 = Image.open('/Users/dingma/PycharmProjects/websiteproject/3.jpeg')
    st.image(image3, caption='Modern Art 2')
    image5 = Image.open('/Users/dingma/PycharmProjects/websiteproject/5.jpeg')
    st.image(image5, caption='Modern Art 5')
    image7 = Image.open('/Users/dingma/PycharmProjects/websiteproject/7.jpeg')
    st.image(image7, caption='Modern Art 7')
    image9 = Image.open('/Users/dingma/PycharmProjects/websiteproject/9.jpeg')
    st.image(image9, caption='Modern Art 9')
    image11 = Image.open('/Users/dingma/PycharmProjects/websiteproject/11.jpeg')
    st.image(image11, caption='Modern Art 11')



with right:
    image2 = Image.open('/Users/dingma/PycharmProjects/websiteproject/2.jpeg')
    st.image(image2, caption='Modern Art 1')
    image4 = Image.open('/Users/dingma/PycharmProjects/websiteproject/4.jpeg')
    st.image(image4, caption='Modern Art 4')
    image6 = Image.open('/Users/dingma/PycharmProjects/websiteproject/6.jpeg')
    st.image(image6, caption='Modern Art 6')
    image8 = Image.open('/Users/dingma/PycharmProjects/websiteproject/8.png')
    st.image(image8, caption='Modern Art 8')
    image10 = Image.open('/Users/dingma/PycharmProjects/websiteproject/10.jpeg')
    st.image(image10, caption='Modern Art 10')
    image12 = Image.open('/Users/dingma/PycharmProjects/websiteproject/12.jpeg')
    st.image(image12, caption='Modern Art 12')





with st.sidebar:
    st.header("A brief Introduction on Artists")
    if st.button('Monet'):
        st.write('''Oscar-Claude Monet (UK: /ˈmɒneɪ/, US: /moʊˈneɪ, məˈ-/, French: [klod mɔnɛ]; 14 November 1840 – 5 December 1926) was a French painter and founder of impressionist painting who is seen as a key precursor to modernism, especially in his attempts to paint nature as he perceived it.[1] During his long career, he was the most consistent and prolific practitioner of impressionism's philosophy of expressing one's perceptions before nature, especially as applied to plein air (outdoor) landscape painting.[2] The term "Impressionism" is derived from the title of his painting Impression, soleil levant, exhibited in 1874 (the "exhibition of rejects") initiated by Monet and his associates as an alternative to the Salon.''')
    if st.button('Jean Béraud'):
        st.write(''' Jean Béraud (French: [beʁo]; January 12, 1849[1] – October 4, 1935) was a French painter renowned for his numerous paintings depicting the life of Paris, and the nightlife of Paris society. Pictures of the Champs Elysees, cafés, Montmartre and the banks of the Seine are precisely detailed illustrations of everyday Parisian life during the "Belle Époque". He also painted religious subjects in a contemporary setting.''')
    if st.button('Leonardo da Vinci'):
        st.write('''Leonardo di ser Piero da Vinci[b] (15 April 1452 – 2 May 1519) was an Italian polymath of the High Renaissance who was active as a painter, draughtsman, engineer, scientist, theorist, sculptor, and architect.[3] While his fame initially rested on his achievements as a painter, he also became known for his notebooks, in which he made drawings and notes on a variety of subjects, including anatomy, astronomy, botany, cartography, painting, and paleontology. Leonardo is widely regarded to have been a genius who epitomized the Renaissance humanist ideal,[4] and his collective works comprise a contribution to later generations of artists matched only by that of his younger contemporary, Michelangelo. ''')