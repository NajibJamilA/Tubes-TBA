#Najib Jamil Abdurrahman / 1301204250
#Muhammad Daffa Adhima Yudhistira / 1301204464
#Bahasa Prancis

import streamlit as st

import string

#input sentences
st.write("""
# PROGRAM LEXICAL ANALYZER AND PARSER
Program ini untuk mengidentifikasi apakah sebuah lexical/token/kata valid sesuai simbol terminal yang telah
didefinisikan dan apakah susunan token/kata sudah memenuhi aturan pada Grammar yang sudah ditentukan(S V O).
List Kata : """)
st.write('S (Subject) >> | pere | | mere |')
st.write('V (Verb) >> | tuer | | boisson | | voir |')
st.write('O (Object) >> | robe | | cigarette | | jus | | fleur | | lapin |')
st.write('Contoh : pere voir lapin (bentuklah kalimat S V O)')
st.write('------------------------------------------------------------------------')
sentence = st.text_input("Masukkan Kalimat: ", placeholder="Masukkan kalimat S V O")
cek = st.button("Cek Kalimat")

input_string = sentence.lower()+'#'
tokens = sentence.lower().split()
tokens.append('EOS')


#initailzation
alphabet_list= list(string.ascii_lowercase)
state_list = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16',
            'q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33']

transition_table = {}

for state in state_list :
    for alphabet in alphabet_list :
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'


#spaces before input string
transition_table['q0', ' '] = 'q0'

#update the transition for the following token : pere
transition_table[('q0', 'p')] = 'q1'
transition_table[('q1', 'e')] = 'q2'
transition_table[('q2', 'r')] = 'q3'
transition_table[('q3', 'e')] = 'q4'


transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#transiotion for new token
transition_table[('q33', 'p')] = 'q1'
transition_table[('q33', 'm')] = 'q1'
transition_table[('q33', 'r')] = 'q5'
transition_table[('q33', 'j')] = 'q7'
transition_table[('q33', 'c')] = 'q9'
transition_table[('q33', 'v')] = 'q16'
transition_table[('q33', 'l')] = 'q19'
transition_table[('q33', 't')] = 'q22'
transition_table[('q33', 'b')] = 'q24'

#update the transition for the following token : mere
transition_table[('q0', 'm')] = 'q1'
transition_table[('q1', 'e')] = 'q2'
transition_table[('q2', 'r')] = 'q3'
transition_table[('q3', 'e')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : robe
transition_table[('q0', 'r')] = 'q5'
transition_table[('q5', 'o')] = 'q6'
transition_table[('q6', 'b')] = 'q3'
transition_table[('q3', 'e')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : jus
transition_table[('q0', 'j')] = 'q7'
transition_table[('q7', 'u')] = 'q8'
transition_table[('q8', 's')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : cigarette
transition_table[('q0', 'c')] = 'q9'
transition_table[('q9', 'i')] = 'q10'
transition_table[('q10', 'g')] = 'q11'
transition_table[('q11', 'a')] = 'q12'
transition_table[('q12', 'r')] = 'q13'
transition_table[('q13', 'e')] = 'q14'
transition_table[('q14', 't')] = 'q15'
transition_table[('q15', 't')] = 'q3'
transition_table[('q3', 'e')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : voir
transition_table[('q0', 'v')] = 'q16'
transition_table[('q16', 'o')] = 'q17'
transition_table[('q17', 'i')] = 'q18'
transition_table[('q18', 'r')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : lapin
transition_table[('q0', 'l')] = 'q19'
transition_table[('q19', 'a')] = 'q20'
transition_table[('q20', 'p')] = 'q21'
transition_table[('q21', 'i')] = 'q29'
transition_table[('q29', 'n')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : tuer
transition_table[('q0', 't')] = 'q22'
transition_table[('q22', 'u')] = 'q23'
transition_table[('q23', 'e')] = 'q18'
transition_table[('q18', 'r')] = 'q4'


transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : boisson
transition_table[('q0', 'b')] = 'q24'
transition_table[('q24', 'o')] = 'q25'
transition_table[('q25', 'i')] = 'q26'
transition_table[('q26', 's')] = 'q27'
transition_table[('q27', 's')] = 'q28'
transition_table[('q28', 'o')] = 'q29'
transition_table[('q29', 'n')] = 'q4'

transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : fleur
transition_table[('q0', 'f')] = 'q30'
transition_table[('q30', 'l')] = 'q31'
transition_table[('q31', 'e')] = 'q32'
transition_table[('q32', 'u')] = 'q18'
transition_table[('q18', 'r')] = 'q4'


transition_table[('q4', ' ')] = 'q33'
transition_table[('q4', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

# definition untuk simbol non-terminal dan simbol terminal
non_terminal = ['S', 'subject', 'verb', 'object']
terminals = ['pere', 'mere', 'robe', 'cigarette', 'jus', 
                'fleur', 'lapin', 'tuer', 'boisson', 'voir']

# definition untuk parse table
parse_table = {}

parse_table[('S', 'pere')] = ['subject', 'verb', 'object']
parse_table[('S', 'mere')] = ['subject', 'verb', 'object']
parse_table[('S', 'robe')] = ['error']
parse_table[('S', 'cigarette')] = ['error']
parse_table[('S', 'jus')] = ['error']
parse_table[('S', 'fleur')] = ['error']
parse_table[('S', 'lapin')] = ['error']
parse_table[('S', 'tuer')] = ['error']
parse_table[('S', 'boisson')] = ['error']
parse_table[('S', 'voir')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('subject', 'pere')] = ['pere']
parse_table[('subject', 'mere')] = ['mere']
parse_table[('subject', 'robe')] = ['error']
parse_table[('subject', 'cigarette')] = ['error']
parse_table[('subject', 'jus')] = ['error']
parse_table[('subject', 'fleur')] = ['error']
parse_table[('subject', 'lapin')] = ['error']
parse_table[('subject', 'tuer')] = ['error']
parse_table[('subject', 'boisson')] = ['error']
parse_table[('subject', 'voir')] = ['error']
parse_table[('subject', 'EOS')] = ['error']

parse_table[('verb', 'pere')] = ['error']
parse_table[('verb', 'mere')] = ['error']
parse_table[('verb', 'robe')] = ['error']
parse_table[('verb', 'cigarette')] = ['error']
parse_table[('verb', 'jus')] = ['error']
parse_table[('verb', 'fleur')] = ['error']
parse_table[('verb', 'lapin')] = ['error']
parse_table[('verb', 'tuer')] = ['tuer']
parse_table[('verb', 'boisson')] = ['boisson']
parse_table[('verb', 'voir')] = ['voir']
parse_table[('verb', 'EOS')] = ['error']

parse_table[('object', 'pere')] = ['error']
parse_table[('object', 'mere')] = ['error']
parse_table[('object', 'robe')] = ['robe']
parse_table[('object', 'cigarette')] = ['cigarette']
parse_table[('object', 'jus')] = ['jus']
parse_table[('object', 'fleur')] = ['fleur']
parse_table[('object', 'lapin')] = ['lapin']
parse_table[('object', 'tuer')] = ['error']
parse_table[('object', 'boisson')] = ['error']
parse_table[('object', 'voir')] = ['error']
parse_table[('object', 'EOS')] = ['error']

#lexical analyzer dan main program
if cek:
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept' :
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state =='q4':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q33':
            st.write('current token: ', current_token, ', valid')
            current_token = ''

        if state == 'error' :
            st.write('error') 
            break
        idx_char = idx_char + 1

#conclusion
    if state == 'accept':
        st.write('Semua token di input : ', sentence, ', valid')

    # parser and main program
    # Stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # Input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    # parsing
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        st.write('top= ', top)
        st.write('symbol= ', symbol)
        if top in terminals:
            st.write('Top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_token = idx_token+1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    st.write('isi stack: ', str(stack))
                    stack.pop()
            else:
                st.write('error')
                break
        elif top in non_terminal:
            st.write('Top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_paused = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_paused)-1, -1, -1):
                    stack.append(symbols_to_be_paused[i])
            else:
                st.write('error')
                break
        else:
            st.write('error')
            break
        st.write('Isi stack:', str(stack))
        st.markdown("""---""")

    # conclusion
    st.write()
    if symbol == 'EOS' and len(stack) == 0:
        st.success('Input string: '+sentence+' valid, sesuai Grammar')
        st.spinner('Please wait...')
        st.balloons()
    else:
        st.error('Error, input string '+sentence+' invalid, tidak sesuai dengan Grammar')