import sys

from aimpyodemo import App


app = App()

app.use('index')
app.use('basic')

app.show('basic')

app.run()
