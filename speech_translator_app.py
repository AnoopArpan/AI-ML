{
 "cells": [
  {
   "execution_count": 1,
   "id": "9e547e4e-e459-4a87-b265-c6bb3403b334",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: googletrans==4.0.0-rc1 in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (4.0.0rc1)\n",
      "Requirement already satisfied: httpx==0.13.3 in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from googletrans==4.0.0-rc1) (0.13.3)\n",
      "Requirement already satisfied: certifi in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (2024.8.30)\n",
      "Requirement already satisfied: hstspreload in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (2025.1.1)\n",
      "Requirement already satisfied: sniffio in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (1.3.0)\n",
      "Requirement already satisfied: chardet==3.* in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (3.0.4)\n",
      "Requirement already satisfied: idna==2.* in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (2.10)\n",
      "Requirement already satisfied: rfc3986<2,>=1.3 in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (1.5.0)\n",
      "Requirement already satisfied: httpcore==0.9.* in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (0.9.1)\n",
      "Requirement already satisfied: h11<0.10,>=0.8 in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1) (0.9.0)\n",
      "Requirement already satisfied: h2==3.* in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1) (3.2.0)\n",
      "Requirement already satisfied: hyperframe<6,>=5.2.0 in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1) (5.2.0)\n",
      "Requirement already satisfied: hpack<4,>=3.0 in c:\\users\\anoop arpan\\anaconda3\\lib\\site-packages (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1) (3.0.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install googletrans==4.0.0-rc1"
   ]
  },
  {
   "execution_count": 2,
   "id": "5213abac-d5ad-4dfb-9a31-10fd6197600e",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-05 11:10:30.781 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Anoop Arpan\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "from googletrans import Translator  \n",
    "from gtts import gTTS\n",
    "import os\n",
    "import streamlit as st\n",
    "st.title(\"Speech Translator with Playback\")\n",
    "if st.button(\"Start Listening\"):\n",
    "    recog=sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        st.info(\"Please start speak....\")\n",
    "        recog.adjust_for_ambient_noise(source)\n",
    "        try:\n",
    "           audio=recog.listen(source,timeout=5,phrase_time_limit=10)\n",
    "           text=recog.recognize_google(audio)\n",
    "           st.success(\"Your text is:\",text)\n",
    "        except sr.UnknownValueError:\n",
    "            st.error(\"Audio is not recognize!!!\")\n",
    "            text=None\n",
    "        except sr.WaitTimeoutError:\n",
    "            st.error(\"Timeout: Didn't get any audio input!!!\")\n",
    "            text= None\n",
    "    if text:\n",
    "        lang=st.text_input(\"enter the target language\")\n",
    "        translator=Translator()\n",
    "        translated=translator.translate(text,lang)\n",
    "        st.write(\"Translated text:\",translated.text)\n",
    "        tts=gTTS(text=translated.text,lang=\"hi\")\n",
    "        tts.save(\"output.mp3\")\n",
    "        st.audio(\"output.mp3\", format=\"audio/mp3\")\n"
   ]
  },
  {
   "id": "e8eeb5ce-c12d-4e0c-9c3a-e5476a118434",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
