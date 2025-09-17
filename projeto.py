
import speech_recognition as sr

def callback(recognizer, audio):
    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
    except sr.UnknownValueError: # se nao reconhecer a voz, deixa pra nao estorar no usuario
        pass  
    except sr.RequestError as e: # deixa isso pra nao estorar no usuario, caso de erro na api
        print("Nao reconheceu a voz", e)

def main():
    r = sr.Recognizer()
    mic_index = None  # se quiser usar microfone padrão, windows por algum motivo nao permite a opcao de escolher os mic, entao deixa none msm
    with sr.Microphone(device_index=mic_index) as source:
        print("Ajustando para ruído ambiente...")
        r.adjust_for_ambient_noise(source, duration=1) # ajusta o ruido do mic, deixa 1 ou 2 segundo, menos disso pode da defeito
        
    stop_listening = r.listen_in_background( sr.Microphone(device_index=mic_index), callback) 

    try:
        
        while True:
            pass  
    except KeyboardInterrupt: # deixa isso, pq quando o Ctrl+C e pressionado, aparece alguns logs e isso impede que polua
        stop_listening(wait_for_stop=False)
        print("\nPrograma encerrado")

if __name__ == "__main__": # deixa isso, caso tu importe algo daqui, nao execute o main
    main()