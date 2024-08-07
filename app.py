import tkinter as tk
from tkinter import ttk, font as tkFont
from firebase_admin import credentials, initialize_app, db

cred = credentials.Certificate('******************')
initialize_app(cred, {'databaseURL': '*********************************'})

detalhes_produtos = {}

def pesquisar():
    termo = entrada_pesquisa.get()
    lista_produtos.delete(0, tk.END)

    ref = db.reference('/')
    produtos = ref.get()

    if produtos is not None:
        detalhes_produtos.clear()

        for produto in produtos:
            descricao = produto.get('Descricao', '')
            codigo = produto.get('Codigo', '')
            codigo_barras = produto.get('Codigo_de_Barras', '')
            if pesquisa_inteligente(termo.lower(), descricao.lower()) or termo in codigo or termo in codigo_barras:
                lista_produtos.insert(tk.END, descricao)
                detalhes_produtos[descricao] = {
                    'Descricao': descricao,
                    'Codigo': codigo,
                    'Codigo_de_Barras': codigo_barras,
                    'Venda': produto.get('Venda', ''),
                }
    else:
        lista_produtos.insert(tk.END, "Não foi possível obter os dados do Firebase.")

def pesquisa_inteligente(termo_pesquisa, descricao_produto):
    palavras_chave = termo_pesquisa.split('%')
    for palavra in palavras_chave:
        if palavra.strip() and palavra not in descricao_produto:
            return False
    return True

def mostrar_detalhes(event=None):
    selecao = lista_produtos.curselection()
    if selecao:
        indice = selecao[0]
        termo = lista_produtos.get(indice)

        if termo in detalhes_produtos:
            detalhes = detalhes_produtos[termo]
            texto_detalhes.config(state=tk.NORMAL)
            texto_detalhes.delete(1.0, tk.END)
            texto_detalhes.insert(tk.END, f"Descrição: {detalhes['Descricao']}\n")
            texto_detalhes.insert(tk.END, f"Código: {detalhes['Codigo']}\n")
            texto_detalhes.insert(tk.END, f"Código de Barras: {detalhes['Codigo_de_Barras']}\n")
            texto_detalhes.insert(tk.END, f"Venda: {detalhes['Venda']}")
            texto_detalhes.config(state=tk.DISABLED)

def navegar_lista(event):
    if event.keysym == 'Up':
        indice_atual = lista_produtos.curselection()[0]
        if indice_atual > 0:
            lista_produtos.select_clear(indice_atual)
            lista_produtos.select_set(indice_atual - 1)
            mostrar_detalhes()
    elif event.keysym == 'Down':
        indice_atual = lista_produtos.curselection()[0]
        if indice_atual < lista_produtos.size() - 1:
            lista_produtos.select_clear(indice_atual)
            lista_produtos.select_set(indice_atual + 1)
            mostrar_detalhes()

janela = tk.Tk()
janela.title("Consulta de Produtos")
janela.geometry("1280x720")

style = ttk.Style()
style.theme_use("clam")

frame_pesquisa = ttk.Frame(janela)
frame_pesquisa.pack(fill=tk.X, padx=10, pady=10)

label_pesquisa = ttk.Label(frame_pesquisa, text="Pesquisa:")
label_pesquisa.grid(row=0, column=0)

entrada_pesquisa = ttk.Entry(frame_pesquisa)
entrada_pesquisa.grid(row=0, column=1, sticky="ew")

botao_pesquisar = ttk.Button(frame_pesquisa, text="Pesquisar", command=pesquisar)
botao_pesquisar.grid(row=0, column=2, sticky="ew", padx=(0, 10))

entrada_pesquisa.bind("<Return>", lambda event=None: [pesquisar(), mostrar_detalhes()])

frame_detalhes = ttk.Frame(janela)
frame_detalhes.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

frame_produtos = ttk.Frame(janela)
frame_produtos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lista_produtos = tk.Listbox(frame_produtos, selectmode=tk.SINGLE, height=10, width=40)
lista_produtos.pack(fill=tk.BOTH, expand=True)

texto_detalhes = tk.Text(frame_detalhes, height=5, width=40, state=tk.DISABLED)
texto_detalhes.pack(fill=tk.BOTH, expand=True)

fonte_detalhes = tkFont.nametofont("TkTextFont")
fonte_detalhes.configure(family="Tahoma", size=16)
texto_detalhes.configure(font=fonte_detalhes)

lista_produtos.bind("<ButtonRelease-1>", mostrar_detalhes)

janela.bind("<Up>", navegar_lista)
janela.bind("<Down>", navegar_lista)

janela.grid_columnconfigure(1, weight=7)

janela.mainloop()
