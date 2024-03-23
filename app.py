import pickle
import streamlit as st
import nltk
import string

from nltk.corpus import stopwords
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

class PreProcessText(object):
    def __init__(self):
        pass
    
    def remove_punctuation(self, text=''):
        """
        Takes a String 
        return : Return a String 
        """
        message = []
        for x in text:
            if x in string.punctuation:
                pass
            else:
                message.append(x)
        message = ''.join(message)
        
        return message
    
    def remove_stopwords(self, text=''):
        """
        Takes a String
        return List
        """
        words= []
        for x in text.split():
            if x.lower() in stopwords.words('english'):
                pass
            else:
                words.append(x)
        return words
    
    
    def token_words(self,text=''):
        """
        Takes String
        Return Token also called  list of words that is used to 
        Train the Model 
        """
        message = self.remove_punctuation(text)
        words = self.remove_stopwords(message)
        return words
        

# input

input_message=st.text_input("enter message")
if st.button("Analyze"):
        # pre process
    obj=PreProcessText()
    transform_message=obj.remove_punctuation(input_message)
    # vectorise
    # bow_transformer = CountVectorizer(analyzer=obj.token_words).fit(transform_message)

    vector_input=tfidf.transform([transform_message])
    # tfidf_transformer.transform([transform_message])
    # predict 
    result=model.predict(vector_input)[0]
    if result==0:
        st.header("scam")
    else:
        st.header("no scam")















