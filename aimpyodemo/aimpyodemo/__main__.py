import sys

from aimpyodemo import App


app = App()

app.use('help')
app.use('intro')
app.use('controls')
app.use('generators')
app.use('soundfiles')
app.use('envelopes')
app.use('filters')

#app.show('about')
app.show('dynamiccontrol')

app.run()
