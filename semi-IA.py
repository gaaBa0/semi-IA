import speech_recognition as sr
import pyttsx3 
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import tkinter as tk
import pyautogui
import pyperclip
from time import sleep

def speaktext(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

app = 'notepad.exe'

login = input(str('Login: '))
pas = input(str('Senha: '))

if login == 'admin' and pas == 'ad@1405':

    speaktext('Bem vindo Sr!')

    while(1):

        try:

            with sr.Microphone() as source:

                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                texto = r.recognize_google(audio,language='pt-BR')
                texto.lower()

                if texto == 'código 1405' or texto == '1405':

                    print(f'Você disse: {texto}')
                    speaktext(f'Você disse: {texto}')
                    print(f'O que você gostaria de fazer?')
                    speaktext('O que você gostaria de fazer?')

                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    texto = r.recognize_google(audio,language='pt-BR')
                    texto.lower()

                    if texto == 'código 001' or texto == '001':

                        print(f'Executando código 001')
                        speaktext(f'Executando código 001')
                        speaktext(f'Abrindo Bloco de Notas')

                        os.system(app)

                        exit()

                    elif texto == 'código 002' or texto == '002':

                        print(f'Executando código 002')
                        speaktext(f'Executando código 002')
                        print('Este código ainda é experimental e apenas funciona enquanto o script estiver rodando, caso haja um reinicio da máquina o agendamento será perdido.\nDeseja continuar?')
                        speaktext('Este código ainda é experimental e apenas funciona enquanto o script estiver rodando, caso haja um reinicio da máquina o agendamento será perdido.\nDeseja continuar?')
                        res = input('>>')
                        res.lower()
                        
                        if res == 'sim' or res in 'Ss':
                            print(f'Escreva abaixo o ano, mês, dia, hora e minuto em que gostaria de agendar. (Exemplo: \n2023\n12\n3\n16\n54).')
                            speaktext(f'Escreva abaixo o ano, mês, dia, hora e minuto em que gostaria de agendar.')
                            def tarefa_agendada():
                                def centralizar_janela(janela):
                                    largura_janela = 400
                                    altura_janela = 400

                                    largura_tela = janela.winfo_screenwidth()
                                    altura_tela = janela.winfo_screenheight()

                                    pos_x = (largura_tela - largura_janela) // 2
                                    pos_y = (altura_tela - altura_janela) // 2

                                    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

                                janela = tk.Tk()
                                janela.title("Agendamento")

                                janela.configure(bg="black")

                                texto = "Horário Agendado"
                                rotulo = tk.Label(janela, text=texto, fg="red", bg="black", font=("Impact", 14))

                                centralizar_janela(janela)

                                rotulo.pack(pady=20)  

                                janela.mainloop()

                            y = int(input('Ano: '))
                            m = int(input('Mês: '))
                            d = int(input('Dia: '))
                            h = int(input('Hora: '))
                            mi = int(input('Minuto: '))

                            scheduler = BackgroundScheduler()

                            scheduler.add_job(tarefa_agendada, CronTrigger(year=y,month=m,day=d,hour=h,minute=mi))

                            try:
                                scheduler.start()
                                while True:
                                    pass
                            except (KeyboardInterrupt, SystemExit):
                                scheduler.shutdown()
                        else:
                            exit()

                    elif texto == 'código 003' or texto == '003':

                        print(f'Executando código 003')
                        speaktext(f'Executando código 003!')

                        while True:
                            print(f'Me diga o que deseja pesquisar.')
                            speaktext('Me diga o que deseja pesquisar.')
                            r.adjust_for_ambient_noise(source, duration=0.5)
                            audio = r.listen(source)
                            texto = r.recognize_google(audio,language='pt-BR')
                            texto.upper()

                            comando = 'start "" "https://www.google.com"'
                            os.system(comando)

                            sleep(2)

                            pyautogui.write(texto)
                            pyautogui.press('enter')
                            
                            break

                        exit()
                    
                    elif texto == 'código 004' or texto == '004':

                        def emailAutomatico():

                            url = 'https://mail.google.com/mail/u/1/#inbox'
                            comando = f'start "" "{url}"'

                            #Abrindo o gmail
                            os.system(comando)

                            sleep(4)

                            pyautogui.moveTo(120,190)
                            pyautogui.click() # Clicando no botão "Escrever"

                            pyautogui.moveTo(1320,485)
                            pyautogui.click()
                            pyperclip.copy(dest)
                            pyautogui.hotkey('ctrl','v') #  Preenchendo o destinatário

                            pyautogui.moveTo(1320,545)
                            pyautogui.click()
                            pyperclip.copy(assu)
                            pyautogui.hotkey('ctrl','v') # Preenchendo o assunto

                            pyautogui.moveTo(1320,565)
                            pyautogui.click()
                            pyperclip.copy(msg)
                            pyautogui.hotkey('ctrl','v') #  Preenchendo as mensagens
                            pyautogui.press('enter')

                            pyautogui.moveTo(1300,1000)
                            pyautogui.click() # Indo até o botão de enviar e clicando

                        print('Executando código 004.')
                        speaktext('Executando código 004.')

                        print('Digite abaixo o email do destinatário')
                        speaktext('Digite abaixo o email do destinatário')
                        dest = str(input('>>'))

                        print('Diga o assunto do email.')
                        speaktext('Diga o assunto do email.')

                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source)
                        texto = r.recognize_google(audio,language='pt-BR')
                        assu = f'{texto}'
                        assu.capitalize()

                        print('Diga o conteúdo do email, apenas sem anexos.')
                        speaktext('Diga o conteúdo do email, apenas sem anexos.')
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source)
                        texto = r.recognize_google(audio,language='pt-BR')
                        msg = f'{texto}'
                        msg.capitalize()

                        emailAutomatico()

                        print('Email escrito, revise e faça a correção que precisar.')
                        speaktext('Email escrito, revise e faça a correção que precisar.')

                        exit()

                elif texto == 'código terminal':

                    print(f'Executando código terminal')
                    speaktext(f'Executando código terminal')
                    speaktext(f'Desligando app')

                    exit()

                else:
                    print(f'Você disse: {texto}')
                    speaktext(f'Você disse: {texto}')
                    print('Código Incorreto')
                    speaktext(f'Código Incorreto')

        except sr.RequestError as e:
            print("Não pûde obter resultados; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Erro desconhecido encontrado!")

else:
    speaktext('Login ou senha não reconhecido, você será barrado!')
    exit()