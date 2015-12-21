from __future__ import division
import random
import string
from numpy import mean

def monthlyPayment(L, i, n):
    i = round(i, 4)
    print i
    return L / sum([(1.0 / (1.0 + i))**exp for exp in range(1, n)])

def cantorSet(n):
    return (1/3.0)*(1 + sum([(2/3.0)**exp for exp in range(1, n - 1)]))

def sierpinskiTriangleColored(n):
    return (math.sqrt(3.0)/16.0)*(1 + sum([(3/4.0)**exp for exp in range(1, n)]))

def sierpinskiTriangleRemaining(n):
    return (math.sqrt(3.0)/4.0)*(1 + sum([-((3.0**(exp - 1.0))/(4.0**exp)) for exp in range(1, n + 1)]))
    

def sixSidedDie():
    die = [1, 2, 3, 4, 5, 6]
    sums = dict.fromkeys(range(2, 12 + 1))
    n = 10000000
    for i in range(n):
        sum_die = random.choice(die) + random.choice(die)
        if sums[sum_die] == None:
            sums[sum_die] = 1
        else:
            sums[sum_die] += 1
    
    probs = []
    tot = 0.0
    for key in sums.keys():
        tot += sums[key]
    for key in sums.keys():
        probs.append((key, sums[key]/tot))
    
    return probs

def deckOfCards():
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    cards = [card for card in range(1, 13 + 1)]
    card_dict = dict.fromkeys(suits)
    for key in card_dict.keys():
        card_dict[key] = dict.fromkeys(cards)
    n = 1000000
    for i in range(n):
        suit = random.choice(suits)
        card = random.choice(cards)
        if card_dict[suit][card] == None:
            card_dict[suit][card] = 1
        else:
            card_dict[suit][card] += 1
    
    tot = 0.0
    
    for outer_key in card_dict.keys():
        for inner_key in card_dict[outer_key]:
            tot += card_dict[outer_key][inner_key]
    
    prob_dict = dict.fromkeys(suits)
    for key in prob_dict.keys():
        prob_dict[key] = dict.fromkeys(cards)
        
    for outer_key in card_dict.keys():
            for inner_key in card_dict[outer_key]:
                prob_dict[outer_key][inner_key] = card_dict[outer_key][inner_key] / tot
    
    return prob_dict

def lemonadeStand():
    prob = 0.5
    rainyDays = dict.fromkeys([0, 1, 2, 3])
    n = 10000000
    for i in range(n):
        dayTotal = 0   
        day_1 = random.random() < prob
        if day_1:
            dayTotal += 1
        day_2 = random.random() < prob
        if day_2:
            dayTotal += 1
        day_3 = random.random() < prob
        if day_3:
            dayTotal += 1
        if rainyDays[dayTotal] == None:
            rainyDays[dayTotal] = 1
        else:
            rainyDays[dayTotal] += 1
            
    probs = []
    for key in rainyDays.keys():
        probs.append(rainyDays[key] / float(n))
    
    return probs

def clothingCombo():
    pants = ['brown', 'purple', 'blue', 'green', 'black']
    shirts = ['black', 'brown', 'green']
    combos = dict.fromkeys(['twoB', 'oneB', 'noB'])
    for key in combos.keys():
        combos[key] = 0
    n = 10000000
    for i in range(n):
        pant = random.choice(pants)[0]
        shirt = random.choice(shirts)[0]
        if pant == 'b' and shirt == 'b':
            combos['twoB'] += 1
        elif pant == 'b' or shirt == 'b':
            combos['oneB'] += 1
        else:
            combos['noB'] += 1  
    for key in combos.keys():
        print key, combos[key] / float(n)
        
        
  
def lottery(ticket):
    
    letter = ticket[2]
    
    letters = string.ascii_uppercase
    numbers = string.digits
    
    match_dict = {'complete':0, 'letter':0, 'none':0}
    
    n = 10000000
    
    for i in range(n):
        number_choice = str(random.choice(numbers)) + str(random.choice(numbers))
        letter_choice = random.choice(letters)
        choice = str(number_choice) + letter_choice
        if choice == ticket:
            match_dict['complete'] += 1
        elif letter_choice == letter:
            match_dict['letter'] += 1
        else:
            match_dict['none'] += 1
    
    print 'complete matches: {}, letter matches : {}, none: {}'.\
    format(match_dict['complete']/float(n), match_dict['letter']/float(n), match_dict['none']/float(n))


    
def marvinTheMonkey():
    n = 10000000
    prob = 0.5
    correct_answers_dict = dict.fromkeys([0, 1, 2, 3, 4])
    for i in range(n):
        correct_answers = []
        for j in range(4):
            correct = random.random() < prob
            correct_answers.append(correct)
        number_correct = sum(correct_answers)
        if correct_answers_dict[number_correct] == None:
            correct_answers_dict[number_correct] = 1
        else:
            correct_answers_dict[number_correct] += 1
    
    for key in correct_answers_dict.keys():
        correct_answers_dict[key] = correct_answers_dict[key] / float(n)
    
    return correct_answers_dict

def samTheSquirrel():
    paints = ['red', 'green', 'white', 'black', 'purple', 'yellow']
    sidings = ['red', 'green', 'white']
    matched = 0
    n = 10000000
    for i in range(n):
        paint = random.choice(paints)[0]
        siding = random.choice(sidings)[0]
        if paint == siding:
            matched += 1
    
    return matched / float(n)

def baseballGame():
    attendance = range(1, 50001)
    count_dict = {'product':0, 'last':0, 'sum':0}
    n = 1000000
    
    def product(number_string):
        product = 1
        for number in number_string:
            number = int(number)
            product *= number
        if product % 2 == 0:
            return True
            
    def last(number_string):
        last = int(number_string[-1])
        if last % 2 == 0:
            return True
    
    def sum_last(number_string):
        last_digit = int(number_string[-1]) 
        try:
            second_last_digit = int(number_string[-2]) 
        except IndexError:
            second_last_digit = 0
        sum_last = last_digit + second_last_digit
        if sum_last <= 10 and sum_last >= 1:
            return False
        elif sum_last >= 11:
            return True
        else:
            return None
    
    for i in range(n):
        actual_attendance = random.choice(attendance)
        if product(str(actual_attendance)):
            count_dict['product'] += 1
        if last(str(actual_attendance)):
            count_dict['last'] += 1
        if sum_last(str(actual_attendance)):
            count_dict['sum'] += 1
    
    for key in count_dict.keys():
        count_dict[key] = count_dict[key] / float(n)
    
    return count_dict
            

def lunch():
    choices = [1, 2, 3, 4]
    n = 1000000
    success = []
    for i in range(n):
        bob_choice = random.choice(choices)  
        anna_choice = random.choice(choices) 
        if bob_choice == anna_choice:
            success.append(True)
        else:
            success.append(False)
    print sum(success) / float(len(success))

def inLaws():
    prob = 0.7
    visits = dict.fromkeys(range(3))
    n = 10000000
    for i in range(n):
        num_visits = 0
        for j in range(2):
            does_visit = random.random() < prob
            if does_visit:
                num_visits +=1
        if visits[num_visits] == None:
            visits[num_visits] = 1
        else:
            visits[num_visits] += 1
    
    for key in visits.keys():
        visits[key] = visits[key] / float(n)
        
    return visits

            
def companies():
    
    def smallProfit():
        success = 0
        n = 1000000
        for i in range(n):
            trial = []
            for j in range(4):
                trial.append(random.random() < 0.9)
            num_success = sum(trial)
            if num_success == 4:
                success += 1
        print success / float(n)
    
    def largeProfit():
        success = 0
        n = 1000000
        for i in range(n):
            trial = []
            for j in range(2):
                trial.append(random.random() < 0.2)
            num_success = sum(trial)
            if num_success == 2:
                success += 1
        print success / float(n)

def job():
    n = 10000000
    waiter_prob = 0.6
    cook_prob = 0.5
    manager_prob = 0.4
    promotion_dict = {'waiter':0, 'cook':0, 'manager':0, 'none':0}
    for i in range(n):
        if random.random() < waiter_prob:
            promotion_dict['waiter'] += 1
            if random.random() < cook_prob:
                promotion_dict['cook'] += 1
                promotion_dict['waiter'] -= 1
                if random.random() < manager_prob:
                    promotion_dict['manager'] += 1
                    promotion_dict['cook'] -= 1
        else:
            promotion_dict['none'] += 1
    
    for key in promotion_dict.keys():
        promotion_dict[key] = promotion_dict[key] / float(n)
    
    return promotion_dict
        
def moneyBall():
    first_prob = 0.6
    second_prob = 0.7
    n = 10000000
    shot_dict = {'first':0, 'second':1, 'neither':0, 'both':0}
    for i in range(n):
        neither = True
        both = False
        first = False
        if random.random() < first_prob:
            shot_dict['first'] += 1
            neither = False
            first = True
        if random.random() < second_prob:
            if first:
                shot_dict['both'] += 1
                shot_dict['first'] -= 1
            else:
                shot_dict['second'] += 1
                neither = False
        if neither:
            shot_dict['neither'] += 1
    
    for key in shot_dict.keys():
        shot_dict[key] = shot_dict[key] / float(n)
    
    return shot_dict
    
def forwardEuler(initial, stop, n):
    
    startX = initial[0]
    startY = initial[0]
    
    def f(x, y):
        return 2*x + 2*y + 2
    
    step = (stop - startX) / float(n)
    print step
    
    n_list = [0, ]
    X = [startX, ]
    Y = [startY, ]
    dydx = [f(startX, startY), ]
    
    for i in range(1, n + 1):
        n_list.append(i)
        X.append(X[i - 1] + step)
        Y.append(Y[i - 1] + dydx[i - 1]*step)
        dydx.append(f(X[i], Y[i]))    
    
    print n_list, X, Y  

def baguettes():
    burn_prob = 0.4
    basket = []
    n = 1000000
    for i in range(n):
        package = []
        for j in range(2): 
           if random.random() < burn_prob:
               package.append('burned')
           else:
               package.append('regular')
       
        basket.append(package)
    
    regular = 0
    mixed = 0
    burned = 0
   
    for package in basket:
        if package == ['regular', 'regular']:
            regular +=1
        elif package == ['burned', 'burned']:
            burned += 1
        else:
            mixed += 1
    
    print 'Regular: {}, Mixed: {}, Burned: {}'.format(regular/float(n), mixed/float(n), burned/float(n))
        

def halfLife():
    amt_list = [300,]
    for i in range(1, 10):
        amt = (0.5*amt_list[i - 1] + 300)
        amt_list.append(amt)
    return amt_list
        
        
        
        