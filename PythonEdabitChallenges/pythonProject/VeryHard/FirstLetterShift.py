# Link to Challenge: https://edabit.com/challenge/ojNRprg7fKpWJpj47
def shift_sentence(sentence=""):
    shifted_word = ""
    words = sentence.split(" ")
    if words.__len__() == 1: return print(sentence)
    words_count = words.__len__()
    for i in range(words_count):
        shifted_word += words[i].replace(words[i][0], words[i - 1 % words_count][0])
        if i + 1 == words_count: continue
        shifted_word += " "
    print(shifted_word)


shift_sentence("create a function") # freate c aunction
shift_sentence("it should shift the sentence")# st ihould shift she tentence
shift_sentence("the output is not very legible")# lhe tutput os iot nery vegible
shift_sentence("where is the butter")# bhere ws ihe tutter
shift_sentence("she sells sea shells")# she sells sea shells
shift_sentence("one plus one equals two")# tne olus pne oquals ewo
shift_sentence("tey ghis uot hnscrambled")# hey this got unscrambled
shift_sentence("i love to eat scrambled eggs and ham")# h iove lo tat ecrambled sggs end aam
shift_sentence("mitochondria is the powerhouse of the cell")# citochondria ms ihe towerhouse pf ohe tell
shift_sentence("sarah the key is under the door mat")# marah she tey ks inder uhe toor dat
shift_sentence("elephants dance about bravely in thailand")# tlephants eance dbout aravely bn ihailand
shift_sentence("untouched")# untouched
shift_sentence("edabit")# edabit

