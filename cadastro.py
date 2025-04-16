import tkinter as tk
from tkinter import messagebox
import pyodbc

# Configuração da conexão ao banco de dados
server = 'gas'
database = 'cadastro'
username = 'dbatak'
password = '1'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'



# Função para salvar os dados no banco
def salvar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if not nome or not email or not telefone:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuarios (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Cadastro de Usuário")

# Labels e campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=60, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=60, pady=10)

tk.Label(root, text="E-mail:").grid(row=1, column=0, padx=60, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=60, pady=10)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=60, pady=10)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=60, pady=10)

# Botão de salvar
btn_salvar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_salvar.grid(row=3, column=0, columnspan=2, padx=60, pady=60)

# Executando a interface gráfica
root.mainloop()