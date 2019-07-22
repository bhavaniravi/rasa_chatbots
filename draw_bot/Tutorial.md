# Draw Bot 

Draw bot is a chatbot that draw the shapes that you ask it to.

This bot is a bit complicated than the other two bots. 

Again we will be playing around with intent and entity but instead of using `rasa shell` we will build our own UI and use Rasa webhook

Why that way?

Because, we need a UI to draw the shapes. We can't plug that into rasa shell.
Also this is to show you you can write scripts or just frontend to interact with rasa.


## Let's get on to action

1. Like always let's start with a `rasa init` and get rid of things we don't need.
2. On writing down the intent, entitiy and action train the bot with `rasa train`
3. Run `rasa test` to make sure everything works fine.