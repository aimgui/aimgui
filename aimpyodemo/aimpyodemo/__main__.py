import sys

from aimpyodemo import App


app = App()

#app.use('basic')
app.use('help')
app.use('intro')
app.use('controls')

app.show('about')

app.run()
