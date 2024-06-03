from tkinter import *
from tkinter import ttk

from funcionalidades.multiplicacao import multiplicacao
from funcionalidades.potenciacao import potenciacao
from theme.colors import *

# Criem as funcionalidades de soma, subtração, divisão, multiplicação, módulo(resto da divisão), potenciação na pasta de funcionalidades com o nome da funcionalidade no arquivo, EX: soma.py, multiplicacao.py...

if __name__ == "__main__":
  janela = Tk()
  janela.title("Calculadora")
  janela.geometry("300x335")
  janela.resizable(False, False)
  janela.config(bg=fundoGrey)

  frame_display = Frame(janela, width=300, height=50, bg=cor2)
  frame_display.grid(row=0, column=0)

  frame_body = Frame(janela, width=300, height=350)
  frame_body.grid(row=1, column=0)

  texto_em_tela = ""

  def escrever(event):
    global texto_em_tela
    texto_em_tela = texto_em_tela + str(event)
    valor_atual.set(texto_em_tela)

  def limpar_display():
    valor_atual.set("0")
    global texto_em_tela
    texto_em_tela = ""

  def calcular():
    global texto_em_tela
    # Essa variável é onde esta armazenada a expressão que o usuario digitou para ser calculado
    valores_para_calcular = str(texto_em_tela)

    if len(valores_para_calcular) > 4:
      texto_em_tela = eval(valores_para_calcular)

    if '**' in valores_para_calcular:
      a, b = map(float, valores_para_calcular.split('**'))
      texto_em_tela = potenciacao(a, b)
    elif '*' in valores_para_calcular:
      a, b = map(float, valores_para_calcular.split('*'))
      texto_em_tela = multiplicacao(a, b)
        
    valor_atual.set(texto_em_tela)

  # Label
  valor_atual = StringVar()
  app_label = Label(frame_display, textvariable=valor_atual, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor2, fg=cor1)
  app_label.place(x=0, y=0)
  valor_atual.set("0")

  # Buttons
  # primeira linha
  clean_btn = Button(frame_body, text="C", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: limpar_display())
  clean_btn.place(x=0, y=0)

  module_btn = Button(frame_body, text="%", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("%"))
  module_btn.place(x=140, y=0)

  division_btn = Button(frame_body, text="/", width=5, height=2, bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("/"))
  division_btn.place(x=220, y=0)

  # segunda linha
  seven_btn = Button(frame_body, text="7", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("7"))
  seven_btn.place(x=0, y=56)

  eight_btn = Button(frame_body, text="8", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("8"))
  eight_btn.place(x=65, y=56)

  nine_btn = Button(frame_body, text="9", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("9"))
  nine_btn.place(x=140, y=56)

  multiply_btn = Button(frame_body, text="*", width=5, height=2, bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("*"))
  multiply_btn.place(x=220, y=56)

  # terça linha
  four_btn = Button(frame_body, text="4", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,command=lambda: escrever("4"))
  four_btn.place(x=0, y=112)

  five_btn = Button(frame_body, text="5", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,command=lambda: escrever("5"))
  five_btn.place(x=65, y=112)

  six_btn = Button(frame_body, text="6", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,command=lambda: escrever("6"))
  six_btn.place(x=140, y=112)

  subtraction_btn = Button(frame_body, text="-", width=5, height=2, bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("-"))
  subtraction_btn.place(x=220, y=112)

  # quarta linha
  one_btn = Button(frame_body, text="1", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("1"))
  one_btn.place(x=0, y=168)

  two_btn = Button(frame_body, text="2", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,command=lambda: escrever("2"))
  two_btn.place(x=65, y=168)

  three_btn = Button(frame_body, text="3", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,command=lambda: escrever("3"))
  three_btn.place(x=140, y=168)

  sum_btn = Button(frame_body, text="+", width=5, height=2, bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("+"))
  sum_btn.place(x=220, y=168)

  # quinta linha
  zero_btn = Button(frame_body, text="0", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE,command=lambda: escrever("0"))
  zero_btn.place(x=0, y=224)

  point_btn = Button(frame_body, text=".", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: escrever("."))
  point_btn.place(x=140, y=224)

  equal_btn = Button(frame_body, text="=", width=5, height=2, bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: calcular())
  equal_btn.place(x=220, y=224)

  janela.mainloop()
