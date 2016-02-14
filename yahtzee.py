#!/usr/bin/python

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def combination(hand, length):
    """
    Combine all possiable valuses in hand by length
    """
    ans = set([()])
    outer = 0
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            if len(seq) > 0:
                outer = seq[len(seq) - 1] + 1
            for item in range(outer, len(hand)):
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(sorted(new_seq)))
            ans = temp

    res = set()
    for item in ans:
        val = []
        for idx in range(len(item)):
            val.append(hand[item[idx]])
        res.add(tuple(val))

    return res

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    score_value = 0
    for item in hand:
        tmp_score = list(hand).count(item) * int(item)
        if tmp_score > score_value:
            score_value = tmp_score
    return score_value


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    expected = 0
    outcomes = range(1, num_die_sides + 1)
    all_sequences = [held_dice + seq for seq in gen_all_sequences(outcomes, num_free_dice)]
    for item in all_sequences:
        expected += score(item) * (1 / float(num_die_sides ** num_free_dice))
    return expected


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    ans = set()
    for idx in range(len(hand) + 1):
        obj = combination(hand, idx)
        for item in obj:
            ans.add(item)
    return ans


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    ans = ()
    expected_val = 0
    held_set = gen_all_holds(hand)
    for held_dice in held_set:
        num_free_dice = len(hand) - len(held_dice)
        tmp_exp = expected_value(held_dice, num_die_sides, num_free_dice)
        if tmp_exp > expected_val:
            expected_val = tmp_exp
            ans = held_dice
    return (expected_val, ans)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()
