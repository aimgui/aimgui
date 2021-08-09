import sys

sys.path.append('.')

from aimflodemo import App

app = App()

app.use('basic')
app.use('connect')
app.use('sine')
app.use('sparks')

app.show('basic')

app.run()
