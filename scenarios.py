"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "c1 human writing",
        "criterion": 1,
        # Real human writing: r/books comments from my TakeMeter labels.csv,
        # standing in for "5 pieces I wrote myself" (see README). The first
        # five are the plainest (shortest average sentence); the last five are
        # ordinary.
        "texts": [
            "For me, Henry James is black licorice. I get why people love him. Intellectually, I can admire his craft and construction and understand why he was massively influential and important. He just is really not for me. I've tried. I've read a few of his books. Nope. I like plenty of literature of that era. I can get with realism and modernism. Just not Henry James. I just find his writing really fussy and wooden and pretty much unreadable.",
            "He writes like it's a movie. Things keep moving and the action is frequent. Sure the dialogue isn't realistic. Neither is Shakespeare's. Not that Sanderson has anything to do with Shakespeare, but you don't need realistic dialogue in something that's not trying to be realistic. The dialogue establishes the characters and their relationships well. And of course, the settings are vivid and cool.",
            "Red, White & Royal Blue. I'm down for a fun romance but the wiring style was so... I don't know. You know how there's some style of speech that's everywhere online but you never hear people irl that speak that way? It was like that for me.",
            "I regularly DNF books when the writing itself sucks. Iron Widow, for example, was really popular when it came out and won awards (?), but I have legitimately read higher quality prose from high schoolers. You can beta read better work from random internet people. I tried. I couldn't.",
            "I really hated My Year of Rest and Relaxation. Yes, I understand she's supposed to be unlikeable. I generally enjoy books with unlikeable characters! But there was nothing about that book that compelled me or made feel even remotely interested in what was happening. However I will say that the ending was good.",
            'One of the greatest autobiographies ever. I posted this on another subreddit the other day. Both the book and the audiobook are exceptional.I would also give a shout out to Kwame Onwauchi’s Notes From A Young Black Chef. His self deprecating and humorous writing style is similar to Bourdain’s and the explanation of getting through the school of hard knocks is similar to Bourdain. Like Bourdain, both the book and audiobook are great.Kitchen Confidential still stands out as one of the greatest biographies I’ve ever read.',
            "I enjoyed most of the book but one thing I disliked was the multiple instances where he said a good employee is someone who never calls out sick. It was worded in a way that gave the impression he'd definitely hold it against them regardless of the reason for calling out. Ew.",
            'Personally, and this feels very nitpicky, I really struggle with quotation-less dialogue. I found The Heart in Winter by Kevin Barry at a bookshop recently and the blurb and employee review hit all the points for me, but when I opened it to take a peek? Ouch. I might still check it out from the library and give it a go, but not having quotation marks just trips me up.',
            "I've been both reading and gaming since childhood. And yes, reading usually takes more focus, depending on the book. Also if you ever feel like you're forcing yourself to finish a book, it might not be your concentration that's the issue but the book itself. Don't feel compelled to finish every book you start, you can always decide you don't like something and go read a book you enjoy more.",
            'It did make me anxious, for exactly these reasons. Realizing how real this is for many people, and also that it will probably be a reality for the "middle class" within a few generations, if not sooner, and feeling helpless to fix it. I couldn\'t finish it the first time I tried, but this time I\'m listening like you, and I only have a half hour left. I love the narrator\'s voice, too!',
        ],
    },
    {
        "name": "c2 clear AI and human",
        "criterion": 2,
        # First five: generated by an AI assistant, unedited. Last five: more
        # real r/books comments, different from criterion 1's.
        "texts": [
            'Reading regularly offers numerous benefits for personal growth and well-being. It enhances vocabulary, improves concentration, and fosters empathy by allowing readers to experience diverse perspectives. Furthermore, reading can reduce stress and provide a valuable escape from the demands of daily life. By incorporating reading into a daily routine, individuals can unlock a wide range of cognitive and emotional advantages.',
            "Effective time management is a crucial skill in today's fast-paced world. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can significantly enhance their productivity. Additionally, taking regular breaks and maintaining a healthy work-life balance are essential for preventing burnout and ensuring long-term success.",
            'Climate change represents one of the most significant challenges facing humanity today. Rising global temperatures, melting ice caps, and increasingly frequent extreme weather events highlight the urgent need for action. Addressing this issue requires a collaborative effort from governments, businesses, and individuals to reduce greenhouse gas emissions and transition to sustainable energy sources.',
            'Learning a new language can be a rewarding and enriching experience. It opens doors to new cultures, enhances cognitive abilities, and improves career prospects. To succeed, learners should practice consistently, immerse themselves in the language, and embrace mistakes as valuable learning opportunities. With dedication and patience, anyone can achieve fluency.',
            "Regular physical activity plays a vital role in maintaining overall health and well-being. Exercise strengthens the cardiovascular system, improves mood, and helps maintain a healthy weight. Moreover, it can reduce the risk of chronic diseases such as diabetes and heart disease. Incorporating even moderate exercise into one's daily routine can lead to significant long-term benefits.",
            'I had that reaction with "The Three Body Problem" by Liu Cixin. The style was very blunt and plot-oriented, with very little description or character development. I did finish the book, and began to feel (not sure if this was correct) that the writing style reflected the trend in Chinese writing, and maybe even thought, as I was reading it in English translation. Overall, not sorry I read it, but did not invest time in the sequels.',
            "My only complaint about this book was that it wasn't long enough. It feels like a great overview of TB that touches on a lot of different ideas surrounding it but doesn't dig that deeply into any single one.Okay? Do you have any meaningful response to make or just going to dodge that? If criticism is too much for you just engage with commenters (or even the other part of my comment), that are about the book.",
            "people should read more things they dislike. I think getting perspective on things and getting more experiences from reading is fantastic, even if you didn't love the material. I'm not advocating for reading truly heinous stuff, but I think being exposed to poor writing, bad characters, and flimsy plots reinforces strong writing, complex characters, and intricate plots.",
            'I don\'t care how many books you\'ve read this year.That goes for any book. There\'s a reason Dr. Seuss is so popular, not because kids like him (though they do), but because adult like him. They are a pleasure to read to your children, and so they are good books in their own right, not because they have been "dumbed down." There\'s nothing dumb about a Dr Seuss book, for all it\'s silliness.',
            'I agree so much with you! I thought Lorena was endlessly captivating and very strong in het own way in the harsh environment she was living in. I also thought her trauma was written well and with reverence. Someone else called her the stereotypical female character who always needs saving and really? When July Johnson exists? He needs more saving than her.',
        ],
    },
    {
        "name": "c3 lightly edited AI",
        "criterion": 3,
        # The five AI texts above, lightly reworded by hand. Criterion 3 reads
        # these together with criterion 2's ten, for 15 inputs.
        "texts": [
            "Reading a lot is good for you in more ways than people think. It builds your vocabulary, helps you focus, and lets you see the world through other people's eyes. It can also take the edge off a stressful day. Make it part of your routine and the benefits add up.",
            "Managing your time well matters, especially when everything moves this fast. Prioritize, set clear goals, and cut the distractions - you'll get more done. Take breaks too. Burnout is real, and balance is what keeps you going long term.",
            'Climate change is one of the biggest problems we face. Temperatures are rising, ice caps are melting, and extreme weather keeps getting more common. Fixing it means governments, companies and ordinary people all cutting emissions and moving to cleaner energy. Nobody can do it alone.',
            "Learning a new language is worth the effort. You get access to a new culture, your brain gets a workout, and it can help your career. The trick is to practice every day, surround yourself with the language, and not be scared of mistakes. Stick with it and you'll get there.",
            "Exercise is one of the best things you can do for your health. It's good for your heart, your mood and your weight. It also lowers your risk of things like diabetes and heart disease. You don't need a gym - even a bit of moderate exercise every day makes a real difference.",
        ],
    },
    {
        "name": "c5 bad input",
        "criterion": 5,
        # Five of criterion 5's six cases. The sixth, a body that isn't a JSON
        # object, can't be a dict here, so run_checks.py sends it.
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "    ", "creator_id": "eval_bad_space"},
            {"text": "Hello", "creator_id": "eval_bad_oneword"},
            {"text": "word " * 10000, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
