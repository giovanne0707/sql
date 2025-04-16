import tkinter as tk
from tkinter import messagebox
import pyodbc

# Configuração da conexão ao banco de dados
#
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
        listar_dados()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")


# Função para excluir um registro selecionado
def excluir_dado():
    try:
        selecionado = lista_dados.curselection()
        if not selecionado:
            messagebox.showerror("Erro", "Selecione um registro para excluir!")
            return

        indice = selecionado[0]
        registro = lista_dados.get(indice)
        email = registro.split(" | ")[1]  # Pegando o email como referência para exclusão

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE email = ?", (email,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
        listar_dados()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir dados: {e}")


# Função para listar os dados no Listbox
def listar_dados():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT nome, email, telefone FROM Usuarios")
        lista_dados.delete(0, tk.END)  # Limpa a lista antes de adicionar novos itens
        for row in cursor.fetchall():
            lista_dados.insert(tk.END, f"{row.nome} | {row.email} | {row.telefone}")
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar os dados: {e}")


# Criando a interface gráfica
root = tk.Tk()
root.title("Cadastro de Usuário")

# Labels e campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="E-mail:").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

# Botão de salvar
btn_salvar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_salvar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Listbox para exibir os registros
lista_dados = tk.Listbox(root, width=50)
lista_dados.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Botão de excluir
btn_excluir = tk.Button(root, text="Excluir", command=excluir_dado)
btn_excluir.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Carregar dados iniciais
listar_dados()

# Executando a interface gráfica
root.mainloop()