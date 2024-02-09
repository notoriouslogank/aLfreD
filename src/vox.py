#!/usr/bin/env python3

import speech_recognition as sr


def get_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'hello' or 'goodbye'!")
        audio = r.listen(source)

    try:
        out_text = r.recognize_google(
            audio, key="AIzaSyBn3qjw5M3-sjtSxBAkKHGPCFoBSOZ75d0"
        )
        return out_text

    except sr.UnknownValueError:
        print("Error: Could not understand.")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )


if get_input() == "hello":
    print("Howdy, partner.")
if get_input() == "goodbye":
    print("See you later, Space Cowboy.")
else:
    print("idk what you said lol")
