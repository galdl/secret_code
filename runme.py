import hashlib

hash_vals = dict(
    underground_floor_num=3126036111279364564811870328294994087531800723932366874418949063743656542083194778802284738287816965911966448078396462401579026727846676796714159259692731,
    license_plate=13025041851706967392009076299877051814615351935307854265581592908703089796033852124746612164874490224277586918407297716117916061201408392963291773510300813
)

def is_correct(attempt):
    assert type(attempt) == int, 'is_correct expects an int!'

    hashed = int(hashlib.sha512(str(attempt).encode('utf-8')).hexdigest(), 16)
    for k, v in hash_vals.items():
        if hashed == v:
            print('Found {}! \n{}'.format(k, attempt))

if __name__ == "__main__":
    print('Modify me to find the two secret codes, each up to 7 digits!')
    # add your code here