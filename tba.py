import string


#input sentences
print('list_kata = pere, mere, robe, cigarette, jus, fleur, lapin, tuer, boisson, voir')
sentence = input("masukkan kata : ")
print('------------------------------------------------------------------------')
input_string = sentence.lower()+'#'

#initailzation
alphabet_list= list(string.ascii_lowercase)
state_list = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16',
            'q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32',]

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

#lexical analyzer
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept' :
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]

    if state =='q4':
        print('current token: ', current_token, ', valid')
        current_token = ''

    if state == 'error' :
        print('error') 
        break
    idx_char = idx_char + 1

#conclusion
print(' ')
if state == 'accept':
    print('semua token di input: ', sentence, ', valid')