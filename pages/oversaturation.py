import streamlit as st
import os

from themes import setup_theme, render_theme_toggle, handle_theme_refresh

st.set_page_config(layout='wide', page_title="A Turning Point")
setup_theme()
render_theme_toggle() 
handle_theme_refresh()


st.header("OverSaturation")
st.caption("24th Oct, 2025")

st.image(os.path.join(os.getcwd(), 'assets', 'wallpaper.jpg'))

st.subheader("Idea (Motivation)")

st.divider()

st.write("So the thought of me writing this post stems from the time I first read [Namish's Perspective](https://namishh.com/blog/talks/development) on this matter and well also personal experiences with peers I interact with so I wanted to tackle some topics on it and talk about the insane saturation of the CS field in India.")

st.subheader("Coding - the new JEE?")

st.divider()

st.write("If I am being 100% honest, I can't lie the way software engineering is being treated like in India, it is lowkey the new JEE")
st.write("My personal favorites being: ")

text1 = "'Bhaiya yeh :red[**DSA**] karu ya **Python**?'"
text2 = "'Is ML Data Science :green[**worth**] it?'"
text3 = "'Bhai mai toh socch raha yeh :blue[**roadmap**] karunga aur fir 1 cr package'"

with st.container(border=True):
    st.markdown(text1)
    st.markdown(text2)
    st.markdown(text3)

st.write("Honestly though, I don't necessarily blame their attitude as it should be considered that for most part Indian families see CSE as a way of getting out of poverty," \
" a more common trend is the emergence of people forcing upon themselves to learn coding even when they don't want to.")

st.write("This is accompanied by the fact that there are so many YouTube channels who focus on " \
" 'yeh karlo aur andha paisa' and the idea they sell that if you complete the XYZ roadmap you are destined " \
" to greatness, now to make it clear software is vast and there is no one roadmap that teaches it all" \
" ultimately your journey as a SWE comes down to how enthusiastic you're about **learning**.")

st.write("And no, learning Java Springboot or React is not gonna directly land you a 6-figure job.")

code = '''def fundamentals():
    print(f"Couple of CS grads don't even know what's the difference between a tuple and list!")'''
st.code(code, language="python")

st.subheader("Roadmaps - a Scam?")
st.divider()

st.write("One of the things that killed creativity or any novel ideas is partially the existence of these CS roadmaps" \
", now I don't think that if you are referring or planning to learn a particular language or framework in a concise or " \
"planned manner is bad at all, infact I think it is a great way of learning. However the problem comes from the fact that " \
"no matter how many tutorials you watch, guides you read or go through lines of code of a friend's project " \
"as long as you don't do it yourself in the end it kindof becomes pointless.")

st.write("This has led to so many CS grads being unable to write a single line of code despite the fact that" \
" they chose to study this subject for 4 years. Now don't get me wrong, CS degree doesn't necessarily teach you" \
" programming but rather **Computer Science** as a whole -> covering computer architecture, memory management, database handling" \
" and then a high level programming language with ton of abstractions such as python or for enterprise reasons : _JAVA_")

st.write("Roadmaps are like training wheels, they give you an idea of what you should be doing however " \
"you can only learn how to ride a bike if you let go of those." \
"This just leads to the standard 3-4 coding projects of :violet[MERN STACK APP] to-do lists." \
"  In Indian tech scene the issue which I have been rambling" \
" on about for quite some time now in this post has been this idea of"
"")

with st.container(border= True):
    st.markdown("10 HR 1 SHOT VIDEO OF C++ !!! AB **GSOC/FAANG** PAKKA!!!!")

st.write("The way the prospect of GSOC has been treated here, it doesn't even resemble the original intention " \
"that google had started this initiative for, the insane amount of videos that you stumble upon these " \
"influencers making of the stipend offers is just crazy. It is just baffling to me how like none of these videos actually" \
" focus on why open source contributions matter at all or why this maybe a great learning opportunity for a fellow " \
"programmer or open source enthusiast but it's just littered with this nonsense of get 1.8L stipend with this one trick.")

st.subheader("AI - _Bubble_")
st.divider()

st.write("Now this is an issue that is worldwide and not in just this country so for sometime I want to also talk about this topic " \
"while I'm yapping about oversaturation in the field of CS")

st.write("Thanks to ChatGPT, Gemini, Claude, Cursor, V0, Bolt and all such AI chatbots/code-assistants " \
"you see daily YouTube Shorts or Instagram Reels of dudes saying AI will replace SWEs " \
"'why coding is no longer a useful skill anymore', 'AI IS COMING FOR YOUR JOB' " \
"and my god it has to be one of the most annoying things I've seen in a while.")

st.write("For AI to be really efficient at a level where it can replace proper SWEs it needs to be able to write production level code" \
" that needs to maintainable by other maintainers and most of the times SWEs just can't comprehend the ungodly amount of slop" \
" that ChatGPT spits out, and if you think 'eh I will improve on this with more vibe coding'.")

st.write("All the power to you my guy, cause goodluck trying to debug code of an LLM which it spat out without any contextual awareness")
st.write("Or even better, trying to maximize LLMs use till it reaches a particular temperature where it can longer generate responses or start hallucinating.")

st.image(os.path.join(os.getcwd(), 'assets', 'vibe_coders.webp'))

st.write("The fact is that for AI to generate 'production-ready' code and be able to manage all workflows to be fully automated" \
        " we unfortunately still need more SWEs to make that happen thus more demand for software jobs and for creation of more software this cycle continues" \
        ", who would have even thought?? and for the day that AI is fully aware and able to self-assign and maintain large codebases and databases. Trust me buddy, your **job is the last thing you would be wanting to worry about**" \
        " since we would have reached dystopia straight outta Isaac Asimov's novel")

st.subheader("My personal Journey")
st.divider()

st.write("Throughout this post, I've been just ranting about all the negative aspects of CS stream so ... I wanted to take a moment and talk about my own journey and why I feel the way about this field the way I do."\
    " So without further ado let me start")

st.write("I started programming seriously around June of 2024 when a senior I used to talk to a lot during entrance time would tell he was starting to learn C and I was well yessir lets do it" \
    " and I started reading [Beej's Guide](https://beej.us/guide/bgc/pdf/bgc_usl_c_1.pdf) and I'm glad I did cause goddamn it was an interesting approach to programming which was the fuck around and find out,"\
    " an approach which I think is how a lot of software should be and is if you think deep about it.")

st.image(os.path.join(os.getcwd(), 'assets', 'dunning_kruger.webp'))

st.write("I genuinely believe that breaking your code multiple times or reverse-engineering an already existing application will help" \
         " you understand what happens underneath the hood of any application. That feel when you fuck up multiple times to be finally able to grasp how stuff works"\
        " is a feeling of its own.")

st.write("A lot of programmers might get discouraged when they see something they have been working on for years might have already been done at a massive scale"\
         " but the thing is that this notion may not always be correct. Imagine if Linus Torvalds"\
        " had the same thought for his linux kernel (Freax was the original name lol) when Microsoft had a booming Windows and an Apple DOS"\
        ", we would have never had such a revolutionary open source movement ever. Today Linux helps powers 90-95% of all cloud and web servers."\
        " and again just a friendly reminder, Linus Torvalds only started this as a [HOBBY PROJECT](https://fossbytes.com/wp-content/uploads/2016/08/linus-torvald-first-linux-email.png) yea nothing much serious obviously lol.")

st.write("And thank god for Linux, it has been my preferred OS to work with (oh, I added this segment cause I'm an Arch User and I love linux)")

st.image(os.path.join(os.getcwd(), 'assets', 'fastfetch.png'))
st.caption("I love how much customization I can get from my command line and editing config files")

st.write("Another thing that struck me is the in video game dev scene, where you often see indie game devs works on games for years and years"\
         " with no guarantee of success but still do it cause of their love and passion for making video games. And I 100% LOVE this mentality"\
        ", Balatro was a game made by a dev who was asked by his employer to take break for sometime, and his ideal vacation? making a card game that he and his family members would enjoy."\
        " and it became a smash hit due its interesting design style and the feel that the dev gave it.")

st.image(os.path.join(os.getcwd(), 'assets', 'balatro.jpg'))


st.write("More recently Team Cherry made silk song a sequel to hollow knight and again with bare minimum marketing managed to surpass 5M Players in 3 days and crashed steam cause of the insane demand."\
         "beating major game titles from AAA corps. only other game whose hype is as much if not more is _GTAVI_ which has a rumored 75M$ for marketing and overall 2B for total dev cost."\
        " The immense love for their creation of software is often seen in their games so much even the pirating subreddits went against pirating silk song which is absolutely insane.")

st.subheader("Final Thoughts")

st.write("So... what even was the point of all this rambling? well I'll explain it with a case of my good [friend](https://rv178.is-a.dev/) (also shoutout to my guy, follow him aswell) who is a self taught dev"\
         ", no one ever told him that 'bhai yeh karle is ke baad toh job/internship pakka' he just did what he did purely cause he wanted to (and was well bored in lockdown lol)"\
        " but he still has more practical software knowledge than the average **leetcode bandar**. You might see a couple of tweets online of dweebs criticizing balatro's source code" \
        " and yes balatro or other indie devs might not have created O(1) card-stacking game but tell me who has a more practical grasp in game dev, these dweebs or LocalThunk?")

st.write("For me, its not like I've never been exposed to Software Dev prior but I never got onto it till the thought came into my mind that I could practically create anything I want" \
         " as long as I have an idea how to proceed with it from a creative and a technical standpoint. And that is how I believe true innovation comes from" \
        " multiple failed attempts but continuing for the love of the game goddammit and that's how it should be, software can be an art if you want it to")

st.write("But again this is all just purely my opinion. That's about it for today, thanks for checking out and See ya Later!!! ^_^")