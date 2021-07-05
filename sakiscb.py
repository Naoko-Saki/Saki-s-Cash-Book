import csv
from datetime import date
import PySimpleGUI as sg

today = date.today().isoformat()

def createafile() -> None:
    fieldnames = 'date', 'details','spent'
    usefn = values['filename']
    with open(usefn, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)
    return fieldnames

def nyuryoku(kirokuyou) -> None:
    word = today, values['input_details'], values['input_spent']
    with open(kirokuyou, 'a', newline='') as f:  
        writer = csv.writer(f)
        writer.writerow(word)
    return kirokuyou
        
def spent(selfile) -> None:
    cb_list = []

    f = open(selfile,'r')

    rows = csv.reader(f)

    for row in rows:
        cb_list.append(row[2])

    del cb_list[0]
    nwlist = [int(i) for i in cb_list]
    totalam = sum(nwlist)
    print(f"この月は{totalam}円使っています")

    f.close()

    

def details(selectfile) -> None:
    with open(selectfile, 'r') as f :
        reader = csv.reader(f)
        for line in reader:
            print(line)
        

sg.theme('DarkTeal3')

layout = [  
    [sg.Text('Saki\'s Cash Book',font=('Skia', 20),text_color='#2f4f4f',relief=sg.RELIEF_RIDGE,background_color='#e6e6fa',border_width=2,pad=((10,10),(10,10)),justification='center')],
    [sg.Text('書き込みファイルは？')],
    [sg.Text('ファイルを新しく作る',size=(18,1)), sg.Input(key = 'filename',), sg.Button('Create a new file', key='create_file')],
    [sg.Text('ファイル指定する',size=(18,1)), sg.Input(key='sfile'), sg.FileBrowse('Select a file', key='kiroku_file_path')],
    [sg.Button('これまでの合計は', key='read_kiroku')],
    [sg.Text('用途と金額を入力してね')],
    [sg.Text('用途',size=(5,1)), sg.InputText(size=(10,1),key='input_details'), sg.Text('金額', size=(5,1)), sg.InputText(size=(10,1),key='input_spent'), sg.Text('円'), sg.Button('入力OK!', key='detail_spent')],
    [sg.Button('合計金額を見る', key='now_spent'), sg.Button('詳細表示する', key='thism_spent')],
    [sg.Text('見たいファイル指定してね')],
    [sg.Text('File', size=(5,1)), sg.Input(), sg.FileBrowse('Select a file', key='read_file_path')],
    [sg.Button('詳細表示する', key='read'), sg.Button('合計金額を見る！!', key='then_spent')],
    [sg.Output(size=(70, 20))],
    [sg.Button('Quit')]
]

window = sg.Window('Saki\'s Cash Book', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'filename':
        if values == None:
            sg.PopupGetText('input,something!', title='popwindow')

        
    if event == 'read_kiroku':
        spent(values['kiroku_file_path'])

    if event == 'create_file':
        createafile()
        
    if event == 'detail_spent':
        print(f"Added {values['input_details']}: {values['input_spent']}円")
        nyuryoku(values['kiroku_file_path'])

    if event == 'now_spent':
        spent(values['kiroku_file_path'])

    if event == 'thism_spent':
        details(values['kiroku_file_path'])

    if event == 'read':
        details(values['read_file_path'])
    
    if event == 'then_spent':
        spent(values['read_file_path'])

window.close()
