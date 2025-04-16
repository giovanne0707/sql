import tkinter as tk
from tkinter import messagebox
import conexao  # Importando o módulo de conexão

# Função para conectar ao banco com os dados inseridos
def conectar():
    global conn  # Variável global para armazenar a conexão
    server = entry_server.get()
    database = entry_database.get()
    username = entry_username.get()
    password = entry_password.get()

    conn = conexao.conectar_bd(server, database, username, password)
    if conn:
        messagebox.showinfo("Sucesso", "Conectado ao banco de dados!")
        criar_tela_cadastro()
    else:
        messagebox.showerror("Erro", "Falha na conexão!")

# Função para salvar dados no banco
def salvar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if not nome or not email or not telefone:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuarios (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Cadastro realizado!")
        listar_dados()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar: {e}")

# Função para listar os dados na interface
def listar_dados():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nome, email, telefone FROM Usuarios")
        lista_dados.delete(0, tk.END)
        for row in cursor.fetchall():
            lista_dados.insert(tk.END, f"{row.nome} | {row.email} | {row.telefone}")
        cursor.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar os dados: {e}")

# Função para criar tela de cadastro após conexão bem-sucedida
def criar_tela_cadastro():
    global entry_nome, entry_email, entry_telefone, lista_dados
    root.destroy()  # Fecha a tela de conexão

    cadastro = tk.Tk()
    cadastro.title("Cadastro de Usuário")

    tk.Label(cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(cadastro)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="E-mail:").grid(row=1, column=0, padx=10, pady=5)
    entry_email = tk.Entry(cadastro)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)
    entry_telefone = tk.Entry(cadastro)
    entry_telefone.grid(row=2, column=1, padx=10, pady=5)

    btn_salvar = tk.Button(cadastro, text="Salvar", command=salvar_dados)
    btn_salvar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    lista_dados = tk.Listbox(cadastro, width=50)
    lista_dados.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    listar_dados()  # Carregar dados ao abrir a tela

    cadastro.mainloop()

# Criando a tela de conexão inicial
root = tk.Tk()
root.title("Conectar ao Banco de Dados")

tk.Label(root, text="Servidor:").grid(row=0, column=0, padx=10, pady=5)
entry_server = tk.Entry(root)
entry_server.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Banco de Dados:").grid(row=1, column=0, padx=10, pady=5)
entry_database = tk.Entry(root)
entry_database.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Usuário:").grid(row=2, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Senha:").grid(row=3, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=3, column=1, padx=10, pady=5)

btn_conectar = tk.Button(root, text="Conectar", command=conectar)
btn_conectar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()