import re

def split_text_into_subsentences(text):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")
    return [sentence.strip() for sentence in sub_sentences if sentence.strip()]

def calculate_ego_score(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.lower() 
        words = sentence.split(' ')
        if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
            ego_score += 1
    return ego_score

test = [
    "Ik ga naar de winkel. Wanneer kom je? Omdat ik graag wil kopen.",
    "Mijn huis is groot, en ik hou ervan. Zodat ik iedereen kan uitnodigen.",
    "Het is een mooie dag. Want de zon schijnt, en ik ben blij.",
    "Geen gebruik van ego woorden in deze zin."
]

for text in test:
    sub_sentences = split_text_into_subsentences(text)
    ego_score = calculate_ego_score(sub_sentences)
    print(f"Text: '{text}'\nEgo Score: {ego_score}\n")
