# madlips template,user input
class madlibs:
    def init(self, wordtype, template):
        self.template = template
        self.wordtype = wordtype


# user input segment
def user_input(word_type):
    word_type = ["noun", "adverb", "adjective", "pronoun"]  # list of word types
    words = []
    print("please provide the following words: ")
    for word in word_type:
        user_input = input(word)
        words.append(user_input + " ")
    return words


# building the story
def create_story(template, words):
    # template="I want to buy a  luxurious {}","When I finish school."
    # words=user_input(["noun","adverb","adjective","pronoun"])
    story =template.format(*words)
    return story

template="I want to buy a  luxurious {}","When I finish school."
words=user_input(["noun","adverb","adjective","pronoun"])
story = create_story(template,words)
print(story)