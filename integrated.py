import whisper
import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords

#  PREDICTION MODEL


tfidf=pickle.load(open('vectorizer.pkl','rb'))
prediction_model=pickle.load(open('model.pkl','rb'))

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
        


# st.title("Transcript app")
# # upload audio file
# audio_file=st.file_uploader("Upload audio",type=["wav","mp3","m4a","mp4"])
# # Loading model
# model=whisper.load_model("base")
# st.sidebar.text("whisper model loaded")


# if st.sidebar.button("Transcribe audio"):
    
#     if audio_file is not None:
#         # TRANSCRIPTION
#         st.sidebar.success("transcribing audio")
#         st.text(audio_file.name)
#         transcription=model.transcribe(audio_file.name)
#         # TRANSCRIPTION COMPLETED
#         # use transcription["text"] to call the text
#         input_message=transcription["text"]
#         obj=PreProcessText()
#         transform_message=obj.remove_punctuation(input_message)
#         vector_input=tfidf.transform([transform_message])
#         result=prediction_model.predict(vector_input)[0]
#         if result==0:
#             st.header("scam")
#         else:
#             st.header("no scam")
        
#         # st.sidebar.success("Transcription completed")
#         # st.markdown(transcription["text"])
    
#     else:
#         st.sidebar.error("please upload file")

# st.sidebar.header("Play Original Audio")
# st.sidebar.audio(audio_file)





# input from audio transcribe

# input_message=st.text_input("enter message")
# input_message=transcription["text"]
# if st.button("Analyze"):
        # pre process
    # obj=PreProcessText()
    # transform_message=obj.remove_punctuation(input_message)
    # vectorise
    # bow_transformer = CountVectorizer(analyzer=obj.token_words).fit(transform_message)

    # vector_input=tfidf.transform([transform_message])
    # tfidf_transformer.transform([transform_message])
    # predict 
    # result=model.predict(vector_input)[0]
    # if result==0:
    #     st.header("scam")
    # else:
    #     st.header("no scam")






# new

def main():
    st.title("FlukeFinders")
    # file uploader
    # uploaded_file=st.file_uploader("upload an audio file",type=["mp3"])
    audio_file=st.file_uploader("Upload audio",type=["wav","mp3","m4a","mp4"])
    model=whisper.load_model("base")
    st.sidebar.text("whisper model loaded")

    if audio_file is not None:
        if st.button("Analyze audio"):
            col1,col2,col3=st.columns([0.4,0.5,0.3])

            with col1:
                st.info("Transcription below")
                st.sidebar.success("transcribing audio")
                st.text(audio_file.name)
                transcription=model.transcribe(audio_file.name)
                st.markdown(transcription['text'])
                


                
                # audio_clip=load_audio(uploaded_file)
                # result=classify_audio_clip(audio_clip)
                # result=result.item()
                # st.info("result probability:{result}")
                # st.success(f"the uploaded audio is{result*100:.2f}%likely to be ai generated")
            
            with col2:
                input_message=transcription["text"]
                obj=PreProcessText()
                transform_message=obj.remove_punctuation(input_message)
                vector_input=tfidf.transform([transform_message])
                result=prediction_model.predict(vector_input)[0]
                
            
                st.info("your uploaded audio is below")
                st.audio(audio_file)
                # st.text(transcription['text'])


                # fig=px.line()
                # fig.add_scatter(x=list(range(len(audio_clip.squeeze()))),y=audio_clip.squeeze())

                # fig.update_layout(
                #     title="waveform plot",
                #     xaxis_title="time",
                #     yaxis="amplitude"
                # )

                # st.plotly_chart(fig,use_container_width=True)


            with col3:
                st.info("Result Below")
                if result==0:
                    st.header("Alert this can be a Scam")
                else:
                    st.header("There is No Scam")
                
                

if __name__ == "__main__":
    main()


