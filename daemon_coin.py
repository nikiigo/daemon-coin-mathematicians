import random
import re
import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

alive = 0
eaten = 0
for a in range(100000):
    apattern = []
    for x in range(2):
        coin = random.SystemRandom().randint(0,1)
        apattern.append(coin)
    pattern1 = ''.join(str(e) for e in apattern)
    logging.debug(f'Patter is {pattern1}')
    pattern2 = pattern1
    pattern1 = r"01"
    pattern2 = r"01"
#    pattern = r'(.)\0{1,}'
    mathematist1 = []
    mathematist2 = []
    string1 = ''
    string2 = ''
    for x in range(1000):
        coin = random.SystemRandom().randint(0,1)
        mathematist1.append(coin)
        coin = random.SystemRandom().randint(0,1)
        mathematist2.append(coin)
    string1 = ''.join(str(e) for e in mathematist1)
    logging.debug(f'String1 is {string1}')
    string2 = ''.join(str(e) for e in mathematist2)
    logging.debug(f'String2 is {string2}')
    index1 = re.search(pattern1, string1).start()
    logging.debug(f'Index1 is {index1}')
    index2 = re.search(pattern2, string2).start()
    logging.debug(f'Index2 is {index2}')
    if mathematist1[index2] == mathematist2[index1]:
        alive += 1
    else:
        eaten += 1
    percentage = alive / (alive + eaten)
    logging.info(f'{a}: Current patterns: [{pattern1} {pattern2}]. The survival ratio is approximately {percentage:2.2%}.')
