import pyodbc

# Definir parâmetros de conexão
server = 'GAS'
database = 'satkbase_20240809'
username = 'sa'
password = '1'

# String de conexão
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Conectar ao banco de dados
try:
    conn = pyodbc.connect(conn_str)
    print("Conexão bem-sucedida!")

    # Criar um cursor
    cursor = conn.cursor()

    # Executar uma consulta de exemplo
    cursor.execute("SELECT TOP 10 * FROM tbfilial")
    for row in cursor.fetchall():
        print(row)

    # Fechar a conexão
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")


class Banco:
    pass


class Banco:
    pass