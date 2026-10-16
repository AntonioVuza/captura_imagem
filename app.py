import cv2

def capturar_e_salvar():

    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return  # early return (cancela tudo que ta fazendo)

    fonte = cv2.FONT_HERSHEY_SIMPLEX
    escala = 0.6
    cor_texto = (255, 255, 255)
    espessura = 1

    while True: #do-while
        status, frame = webcam.read()

        if not status:
            print("Falha ao receber o frame da webcam")
            break

        frame_limpo = frame.copy()

        cv2.rectangle(frame, (10, 10), (320, 75), (0, 0, 0), -1)
        cv2.putText(frame,"[ESPACO] Salvar foto", (20, 35), fonte, escala, cor_texto, espessura)
        cv2.putText(frame, "[ESCAPE] Sair", (20, 60), fonte, escala, cor_texto, espessura)
        
        
        # Inverte o frame horizontalmente (efeito espelho)
        # frame = cv2.flip(frame, 1)

        cv2.imshow("Captura de webcam local", frame)

        tecla = cv2.waitKey(1) & 0xff

        if tecla == 32:
            cv2.imwrite("foto.jpg", frame_limpo)
            print("Foto salva: foto.jpg")

            foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("foto_cinza.jpg", foto_cinza)

            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)

            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)

            foto_canny =cv2.Canny(foto_cinza, 100, 200)
            cv2.imwrite("foto_canny.jpg", foto_canny)

        elif tecla == 27:
            print("Encerrando câmera...")
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__": #verifica se esta sendo executado diretamente.
    capturar_e_salvar()