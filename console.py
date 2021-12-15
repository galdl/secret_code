#!/usr/bin/env python3
"""Can be compiled to binary via: pyinstaller -F --paths=/Users/galdalal/.conda/envs/rl_delay/lib/python3.7/site-packages console.py"""

CORRECT_VEC = [['be37ccebe21815559666b60338ec1492670b8fd2bf6cc63c5c943639ddcc50981003846b75b9e97ad0c0c19484292f59b1d30b45c7b07d1f8973bae68a3b8431'],
           ['be37ccebe21815559666b60338ec1492670b8fd2bf6cc63c5c943639ddcc50981003846b75b9e97ad0c0c19484292f59b1d30b45c7b07d1f8973bae68a3b8431'],
               ['81d45df984803e8bbcd28fa5480ee0c34800c1c3e68533f03a5708f5277ab3deb9eed06742cb77b878f16dd04ac7114610810fa360668149b11bbbf2ef42d81b',
                '74a49c698dbd3c12e36b0b287447d833f74f3937ff132ebff7054baa18623c35a705bb18b82e2ac0384b5127db97016e63609f712bc90e3506cfbea97599f46f']]
MESSAGE_VEC = ['What is the 1st address digit?', 'What is the 2nd address digit?', 'What is the floor number?']

print('Hi, sha512 is your friend. He likes binary dudes...')

def ask_for_code(correct, message):
   curr_guess = input(message).lower()
   while curr_guess not in correct:
      print('You are a failure :(')
      curr_guess = input(message).lower()
   print('Great success!!!')


for j in range(3):
      ask_for_code(CORRECT_VEC[j], MESSAGE_VEC[j])


input("Good luck! https://ibb.co/Jt0y2XD")
