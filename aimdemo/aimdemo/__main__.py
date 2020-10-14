import sys

from aimdemo import App


app = App()

app.use('index')
app.use('bullet')
app.use('button')
app.use('checkbox')
app.use('child')
app.use('circle')
app.use('cloud')
app.use('collapsingheader')
app.use('coloredit')
app.use('colors')
app.use('columns')
app.use('combo')
app.use('demo')
app.use('dnd')
app.use('docking')
app.use('dragfloat')
app.use('dragint')
app.use('drawcallback')
app.use('dummy')
app.use('fireworks')
app.use('font')
app.use('fontimage')
app.use('framebuffer')
app.use('group')
app.use('image')
app.use('imagebutton')
app.use('imagedraw')
app.use('indent')
app.use('input')
app.use('line')
app.use('listbox')
app.use('overlay')
app.use('plot')
app.use('popup')
app.use('rect')
app.use('sameline')
app.use('selectable')
app.use('separator')
app.use('slider')
app.use('spacing')
app.use('sparks')
app.use('sprite')
app.use('tabs')
app.use('text')
app.use('textinput')
app.use('tooltip')
app.use('tree')
app.use('windowdraw')
app.use('windowmenu')
app.use('viewport')

app.show('drawcallback')

app.run()
