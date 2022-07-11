import PySimpleGUI as sg
import mysql.connector as mysql

def banco():

    nome = values['-nome-']
    telefone = values['-telefone-']
    matricula = values['-matricula-']
    senha = values['-senha-']

    try:
        conexao = mysql.connect(
            host="127.0.0.1", # ip do servidor
            user="root", # usuario
            password="", # senha do usuario
            database="BDcadastro" # base de dados
        )
        print("Conexão realizada com sucesso.")
        print("Salvando no banco de dados...")

        cursor = conexao.cursor()

        sql = "INSERT INTO info(nome,telefone,matricula, senha) VALUES (%s, %s, %s, %s)"
        vals = (nome,telefone,matricula, senha) # devem ser passados como tupla

        cursor.execute(sql, vals)

        conexao.commit()
        print("Salvo com sucesso.")
    except mysql.Error as e:
        print(e.msg)

def logar():
    BPAD = ((20, 20), (20, 10))

    # bloco cabeçalho
    top_banner = [
        [sg.Text('UCB\t\t             Brasília - DF' + ' ' * 64, font='Helvetica 15',text_color='white', background_color=DARK_HEADER_COLOR)]]
    # bloco topo
    top = [[sg.Text(f'Cadastro Portal Do Aluno   ', font='Any 20')],
           [sg.Text(f'Universidade Católica de Brasilia  ', font='Any 11')]]
    # bloco login
    block = [[sg.Text('Login', font='Any 15')],
             [sg.Text('Matrícula')],
             [sg.Input(key='matricula')],
             [sg.Text('Senha')],
             [sg.Input(key='senha', password_char='*')],
             [sg.Text('')],
             [sg.Button('Login', button_color='green',font='Helvetica'), sg.Button('Exit', button_color='red',font='Helvetica')],
             [sg.Text('\t\tSem cadastro ainda?'), sg.Button('Clique aqui')]]
    # configurações do Layout
    layout = [[sg.Column(top_banner, size=(380, 60), pad=(0, 0), background_color=DARK_HEADER_COLOR)],
              [sg.Column(top, size=(340, 90), pad=BPAD)],
              [sg.Column(block, size=(340, 250), pad=BPAD)]]

    return sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0, 0), background_color=BORDER_COLOR,
                       no_titlebar=True, grab_anywhere=True,finalize=True)

#configurações dos dashboards, cores e espessura das bordas
theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('BlueMono')
# cores da borda e do cabeçalho
BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
#coordenadas
BPAD = ((20, 20), (20, 10))

def cadastrar():
    BPAD = ((20, 20), (20, 10))
    # bloco cabeçalho
    top_banner = [
        [sg.Text('UCB\t\t             Brasília - DF' + ' ' * 64, font='Helvetica 15',text_color='white', background_color=DARK_HEADER_COLOR)]]
    # bloco cadastro
    block2 = [[sg.Text('Caso não tenha login preencha abaixo', font='Any 14')],
              [sg.Text('Nome')],
              [sg.Input(key='-nome-')],
              [sg.Text('Telefone')],
              [sg.Input(key='-telefone-')],
              [sg.Text('Matrícula ')],
              [sg.Input(key='-matricula-')],
              [sg.Text('Senha')],
              [sg.Input(key='-senha-', password_char='*')],
              [sg.Text('')],
              [sg.Button('Cadastro', button_color='green',font='Helvetica'), sg.Text('  \t\t\t'), sg.Button('Voltar', button_color='Blue',font='Helvetica')],
              [sg.Text('')]]
    # configurações do Layout
    layout = [[sg.Column(top_banner, size=(380, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
                [sg.Column(block2, size=(340,380),  pad=BPAD)]]
    return sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0, 0), background_color=BORDER_COLOR,
                       no_titlebar=True, grab_anywhere=True,finalize=True)
def inicio():
    BPAD = ((20, 20), (20, 10))
    # bloco cabeçalho
    top_banner = [
        [sg.Text('UCB\t\t             Brasília - DF' + ' ' * 64, font='Helvetica 15',text_color='white', background_color=DARK_HEADER_COLOR)]]
    # bloco topo
    top = [[sg.Text(f'Portal Do Aluno   ', font='Any 20')],
           [sg.Text(f'Universidade Católica de Brasilia  ', font='Any 11')]]
    # bloco inico pós login
    block3 = [[sg.Text('Mais serviços em breve...')],
              [sg.Text('Digite sua matrícula para revisar seus Dados')],
              [sg.Input(key='matricula')],
              [sg.Text(' '),sg.Button('Revisão')],
              [sg.Text('')],
              [sg.Text('\t\t\t      '),sg.Button('Desconectar', button_color='red',font='Helvetica')]]

    # configurações do Layout
    layout = [[sg.Column(top_banner, size=(380, 60), pad=(0, 0), background_color=DARK_HEADER_COLOR)],
              [sg.Column(top, size=(340, 90), pad=BPAD)],
              [sg.Column(block3, size=(340, 200), pad=BPAD)]]

    return sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0, 0), background_color=BORDER_COLOR,
                       no_titlebar=True, grab_anywhere=True,finalize=True)

janela1,janela2,janela3=logar(),None,None

while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event =='Exit': break
    if window == janela1 and event == "Login":
        conexao = mysql.connect(
            host="127.0.0.1",  # ip do servidor
            user="root",  # usuario
            password="",  # senha do usuario
            database="BDcadastro"  # base de dados
        )
        cursor = conexao.cursor()
        sql = "SELECT * FROM info WHERE BINARY matricula = '%s' AND BINARY senha = '%s'" % (
            values['matricula'], values['senha'])
        val = values['matricula']
        cursor.execute(sql)
        if cursor.fetchone():
            sg.popup('Login feito\ncom sucesso',image=sg.EMOJI_BASE64_CLAP, keep_on_top=True)
            janela3 = inicio()
            janela1.hide()
        else:
            sg.popup('Credenciais erradas ou vazias, digite novamente',image=sg.EMOJI_BASE64_CRY , keep_on_top=True)
    if window == janela1 and event == 'Clique aqui':
        janela2=cadastrar()
        janela1.hide()
    elif event == "Cadastro":
        matricula = values['-matricula-']
        senha = values['-senha-']
        nome = values['-nome-']
        telefone = values['-telefone-']
        if senha == '' or senha == ' ' or len(senha)<6 or matricula == '' or matricula == ' ' or nome == '' or nome == ' ' or telefone == '' or telefone == ' ':
            sg.popup('Preencha\n     os\n  dados!\nsenha com \nno minimo 6\ncaracteres!',image=sg.EMOJI_BASE64_DEAD, keep_on_top=True)
            continue
        else:
            banco()
            sg.popup('Cadastro\nRealizado\n    com\n sucesso', image=sg.EMOJI_BASE64_HAPPY_JOY, keep_on_top=True)
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Revisão':
        conexao = mysql.connect(
            host="127.0.0.1",  # ip do servidor
            user="root",  # usuario
            password="",  # senha do usuario
            database="BDcadastro"  # base de dados
        )
        cursor = conexao.cursor()
        sql = "SELECT * FROM info WHERE matricula = %s"
        val = (values['matricula'],)
        aux = values['matricula']
        cursor.execute(sql, val)
        myresult = cursor.fetchall()

        if values['matricula'] == '' or values['matricula'] == ' ' or len(values['matricula'])<=9:
            sg.popup('Matrícula errada,\ndigite novamente',image=sg.EMOJI_BASE64_SAD, keep_on_top=True)
        else:
            for i in myresult:
                sg.popup('    Nome          telefone           matrícula       senha',i,image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE, keep_on_top=True)

    if window == janela3 and event == 'Desconectar':
        janela3.hide()
        janela1.un_hide()

window.close()