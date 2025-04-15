import speech_recognition as sr
import pyaudio

def transcribir_audio():
    # Crear un objeto de reconocimiento
    recognizer = sr.Recognizer()

    # Usar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

    try:
        # Usar Google Web Speech API para transcribir el audio a texto
        texto = recognizer.recognize_google(audio, language="en-US")
        print(f"Transcripción: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print(f"Error en la solicitud al servicio de reconocimiento de voz; {e}")
        return ""

# Llamar a la función para transcribir el audio
transcripcion = transcribir_audio()
