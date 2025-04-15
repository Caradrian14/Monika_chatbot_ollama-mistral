import sounddevice as sd
import soundfile as sf
import numpy as np

def grabar_audio(duracion, frecuencia_muestreo, nombre_archivo):
    print("Grabando audio...")
    audio = sd.rec(int(duracion * frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=2)
    sd.wait()  # Esperar a que termine la grabación
    print("Grabación completa.")

    # Guardar el archivo de audio
    sf.write(nombre_archivo, audio, frecuencia_muestreo)
    print(f"Audio guardado como {nombre_archivo}")

# Parámetros de grabación
duracion = 5  # Duración en segundos
frecuencia_muestreo = 44100  # Frecuencia de muestreo en Hz
nombre_archivo = "grabacion.wav"  # Nombre del archivo de salida

# Grabar el audio
grabar_audio(duracion, frecuencia_muestreo, nombre_archivo)