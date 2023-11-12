import streamlit as st

def classify_entrepreneur(answers):
    counts = {
        'Builder': answers.count('a'),
        'Opportunist': answers.count('b'),
        'Visionary': answers.count('c'),
        'Thought Leader': answers.count('d'),
        'Empire Builder': answers.count('e'),
        'Socialpreneur': answers.count('f'),
    }
    result = max(counts, key=counts.get)
    return result

def main():
    st.title("Entrepreneur Mindset Classifier")

    #language_options = ['English', 'Thai', 'Chinese']
    language_options = ['English', 'None']
    selected_language = st.selectbox("Select Language", language_options)

    questions = {
        'English': [
            ("When considering a new business idea, what is most important to you?",
             {'a': 'Solving a problem or fulfilling a need',
              'b': 'Being your own boss',
              'c': 'Making a lot of money',
              'd': 'Building something great',
              'e': 'Creating jobs for others',
              'f': 'Disrupting an industry'}),
            ("How do you react when faced with obstacles or setbacks?",
             {'a': 'Get discouraged and want to quit',
              'b': 'See it as a learning experience',
              'c': 'Double down and work even harder',
              'd': 'Pivot and try a new approach',
              'e': 'Take a break and come back refreshed',
              'f': 'Ask others for help and support'}),
            ("What motivates you the most?",
             {'a': 'Money and financial success',
              'b': 'Creativity and building new things',
              'c': 'Helping people and making a difference',
              'd': 'Recognition and fame',
              'e': 'Freedom and flexibility',
              'f': 'Competing and winning'}),
            ("Which skills are most important for entrepreneurs?",
             {'a': 'Technical/engineering skills',
              'b': 'Interpersonal/communication skills',
              'c': 'Marketing and sales abilities',
              'd': 'Resilience and determination',
              'e': 'Financial and analytical skills',
              'f': 'Creativity and vision'}),
            ("How comfortable are you with risk?",
             {'a': 'Very uncomfortable, avoid risk when possible',
              'b': 'Willing to take calculated risks',
              'c': 'Comfortable with moderate risks',
              'd': 'Love the thrill of high risks',
              'e': 'Risks don\'t scare me if the payoff is big enough',
              'f': 'Risks are required to get ahead'}),
            ("How do you prefer to work?",
             {'a': 'Independently, on my own schedule',
              'b': 'Closely with a few trusted partners',
              'c': 'As part of a larger team',
              'd': 'With mentors and advisors for guidance',
              'e': 'In a highly competitive environment',
              'f': 'In a collaborative, casual work culture'}),
            ("Which is more important?",
             {'a': 'Working on what you care about',
              'b': 'Working with people you like',
              'c': 'Making a big impact on the world',
              'd': 'Leaving a legacy for the future',
              'e': 'Achieving work/life balance',
              'f': 'Gaining experience and skills'}),
            ("How do you decide what business to start or problems to solve?",
             {'a': 'Based on your personal interests and passions',
              'b': 'By identifying trends and upcoming markets',
              'c': 'Solving your own problems and frustrations',
              'd': 'Noticing overlooked needs and gaps in the market',
              'e': 'Copying/improving existing successful businesses',
              'f': 'Using your existing skills and experience'}),
            ("How organized are you?",
             {'a': 'Prefer a flexible, spontaneous approach',
              'b': 'Somewhat organized, but okay with a bit of chaos',
              'c': 'Very scheduled and regimented',
              'd': 'Organized only when absolutely necessary',
              'e': 'Comfortable with any level of organization',
              'f': 'Let others handle the organizational details'}),
            ("Which entrepreneurial quote resonates with you the most?",
             {'a': 'Do what you love and you\'ll never work a day in your life',
              'b': 'You miss 100\% \of the shots you don\'t take',
              'c': 'Move fast and break things',
              'd': 'Innovation distinguishes between a leader and a follower',
              'e': 'It\'s better to own a piece of a big pie than the whole of a small pie',
              'f': 'Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work'}),
            ("How do you handle failure?",
             {'a': 'Take it very hard, get depressed',
              'b': 'Learn from it but ultimately move on',
              'c': 'Don\'t take it personally, keep working to succeed',
              'd': 'Blame external factors, don\'t accept responsibility',
              'e': 'Use it as motivation to try even harder',
              'f': 'Believe I don\'t actually fail, just produce results'}),
            ("As an entrepreneur, is it better to copy an existing successful business or try something completely new?",
             {'a': 'Copy it, but make incremental improvements',
              'b': 'Try something new, be an innovator',
              'c': 'Combine elements of existing successes into a hybrid',
              'd': 'Depends on the specific opportunity',
              'e': 'Copy first, innovate later',
              'f': 'Innovate first, consolidate later'}),
            ("How important is passion?",
             {'a': 'Absolutely critical, won\'t succeed without it',
              'b': 'Helpful but execution is more important',
              'c': 'Overrated, discipline is more key',
              'd': 'Important initially, fades over time',
              'e': 'Not very, many successful founders aren\'t passionate',
              'f': 'Critical ONLY if paired with pragmatism'}),
            ("Should you launch a business as soon as possible and iterate, or wait until you have the perfect product?",
             {'a': 'Launch ASAP and iterate rapidly',
              'b': 'Somewhere in between, don\'t wait too long to launch',
              'c': 'Wait until the product is nearly perfect',
              'd': 'Depends on the type and complexity of the product',
              'e': 'Test the concept quickly with a basic MVP',
              'f': 'Fundraise first to have cash on hand pre-launch'}),
            ("Who is responsible for your success?",
             {'a': 'It\'s all due to my hard work and persistence',
              'b': 'My mentors, teachers and supporters deserve a lot of credit',
              'c': 'It was luck and good timing',
              'd': 'My brilliant and innovative ideas',
              'e': 'My partnerships with smart people',
              'f': 'My family\'s wealth and connections'}),
            ("How do you balance work and life?",
             {'a': 'Work should always come first',
              'b': 'Strive for balance, though sometimes work has to take priority',
              'c': 'Work hard and play hard',
              'd': 'Easy, I divide time neatly between them',
              'e': 'Schedule life around work obligations',
              'f': 'Life comes first, work flexes to accommodate it'}),
            ("Is being an entrepreneur primarily about freedom, money, impact or challenge?",
             {'a': 'Freedom - being your own boss',
              'b': 'Money - profitability and wealth',
              'c': 'Impact - changing the world',
              'd': 'Challenge - accomplishment and pushing yourself',
              'e': 'Freedom and money',
              'f': 'Impact and challenge'}),
            ("What role should ethics play in entrepreneurship?",
             {'a': 'Critical, won\'t cross ethical lines for profit',
              'b': 'Important, though some exceptions can be made',
              'c': 'Overrated, the market dictates what\'s ethical',
              'd': 'Not very, entrepreneurship means doing whatever is needed to succeed',
              'e': 'Crucial, unethical ventures usually fail in the long run',
              'f': 'Irrelevant, amoral capitalism works best'}),
            ("Is entrepreneurship for you mainly about starting businesses, or growing personally?",
             {'a': 'It\'s all about starting and scaling businesses',
              'b': 'Mostly about starting businesses, personal growth is secondary',
              'c': 'Equally about business growth and personal development',
              'd': 'Skews toward personal growth, business is just the medium',
              'e': 'Totally about self-actualization, specific ventures are just vehicles',
              'f': 'Businesses, personal development happens accidentally along the way'}),
            ("Which type of business partner is ideal?",
             {'a': 'Similar personality and work style to you',
              'b': 'Complementary skills and different perspectives',
              'c': 'Shared vision and values',
              'd': 'Impressive credentials and track record',
              'e': 'Opportunities for mentorship',
              'f': 'Someone you get along with really well'}),
        ],
        'None': [
            # Thai questions translation goes here
        ]
    }

    answers = []

    for i, (question, options) in enumerate(questions[selected_language]):
        selected_option = st.radio(f"{i + 1}. {question}", list(options.keys()), format_func=lambda x: options[x])
        answers.append(selected_option)

    if st.button("Classify"):
        result = classify_entrepreneur(answers)

        if result == "Builder":
            detail = "Builders are practical, execution-focused founders who aim to build functional, profitable businesses. They solve real problems by creating products and services people need. Builders tend to be methodical, starting small and scaling through customer traction and revenue rather than rapid expansion. They value organization, discipline and incremental progress towards their business goals. Builders measure success in stability, profitability and maintaining control over their ventures."
        elif result == "Opportunist":
            detail = "Opportunists are flexible, adaptable founders who are constantly exploring and capitalizing on new opportunities. They move quickly, tweak their business models frequently and thrive in uncertainty. Opportunists make data-driven decisions to maximize their options. They are motivated by financial gains and exiting investments at the optimal time. Opportunists network extensively and leverage relationships to find advantageous deals. They are willing to pivot when current opportunities are exhausted or no longer lucrative."
        elif result == "Visionary":
            detail = "Visionaries are innovative big picture thinkers seeking to transform industries. They imagine future possibilities and have bold ideas for bringing new technologies or business models to life. Visionaries are drawn to disruption, innovation and high-growth opportunities. They inspire others with an aspirational vision and build companies around their ideas. Visionaries thrive on inventing, strategizing and evoking passion in others for their vision of the future."
        elif result == "Thought Leader":
            detail = "Thought leaders value knowledge, expertise and influence. They aim to be respected voices and intellectual authorities in their domains. Thought leaders build personal brands, distribute content and educate audiences to demonstrate their knowledge. They founder companies that leverage their ideas, theories and thought leadership to attract customers and talent. Thought leaders measure success primarily through recognition and amplification of their thought leadership rather than financial gains."
        elif result == "Empire Builder":
            detail = "Empire builders prioritize rapid growth and scaling above all else. They start companies with ambitions to become industry dominating forces. Empire builders are drawn to high risk, high reward opportunities. They raise large amounts of capital to fuel aggressive expansion plans and accept high burn rates in pursuit of meteoric growth. Empire builders measure success first by capturing market share and dominance. They leverage their status and distribution channels once achieved."
        else:
            detail = "Social entrepreneurs aim to combine profit with purpose, giving back to society. They build mission-driven companies designed to solve social or environmental problems. Socialpreneurs measure success through positive impact as much as financial gains. They build diverse, inclusive teams unified by a shared higher purpose beyond profits. Socialpreneurs utilize sustainable practices and ethical approaches aligned with their values. They aim to inspire systemic change on societal issues through the power of business."

        st.success(f"You have a {result} mindset! {detail}")

if __name__ == "__main__":
    main()