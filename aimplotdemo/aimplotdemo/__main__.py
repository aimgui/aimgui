import sys

from aimplotdemo import App


app = App()

app.use('index')
app.use('demo')
app.use('line')

app.show('line')

app.run()
