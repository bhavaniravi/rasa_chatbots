# Echo Bot

A bot that repeats whatever you say.

## Check List

- [ ] Checked prerequisites
- [ ] Installed `requirements.txt`

## Bot without nlp

python bot_without_nlp.py

## Bot with Rasa

1. Make sure your current dir is `echo_bot`
2. `cd bot_with_nlu`
3. `rasa init --no-prompt`
4. Don't get scared. This creates a bunch of necessary files for new. 
5. Now it comes with a default bot which we will modify to supprt our echo bot.
6. Goto `data/nlu.md` and delete everything other than `hello` and `goodbye`.
7. Next you will be working with `data/stories.md`. I removed all complicated parts. Just copy paste `hello` and `goodbye` parts.
8. I know it's a bit boring but let's do the same in `Domain.yml` file too.
9. That's all we are almost done
10. `rasa train`
11. Open a new terminal in the same path `rasa run actions`
12. Go back to our main terminal and run `rasa shell`