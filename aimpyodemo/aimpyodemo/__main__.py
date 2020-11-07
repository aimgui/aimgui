import sys

from aimpyodemo import App


app = App()

#app.use('basic')
app.use('help')
app.use('intro')
#app.use('controls')
app.use('generators')
app.use('soundfiles')
app.use('envelopes')

app.show('about')

app.run()
