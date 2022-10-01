# simple_form.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green


def create_simple_form():
    c = canvas.Canvas('simple_form.pdf')

    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Employment Form')
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 700, 'Date:')
    form.textfield(name='date', tooltip='Date',
                   x=110, y=685, borderStyle='inset',
                   borderColor=magenta, fillColor=pink,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 650, 'First Name:')
    form.textfield(name='fname', tooltip='First Name',
                   x=110, y=635, borderStyle='inset',
                   borderColor=magenta, fillColor=pink,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 600, 'Last Name:')
    form.textfield(name='lname', tooltip='Last Name',
                   x=110, y=585, borderStyle='inset',
                   borderColor=green, fillColor=magenta,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 550, 'Address:')
    form.textfield(name='address', tooltip='Address',
                   x=110, y=535, borderStyle='inset',
                   width=400, forceBorder=True)

    c.drawString(10, 500, 'City:')
    form.textfield(name='city', tooltip='City',
                   x=110, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(250, 500, 'State:')
    form.textfield(name='state', tooltip='State',
                   x=350, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 450, 'Zip Code:')
    form.textfield(name='zip_code', tooltip='Zip Code',
                   x=110, y=435, borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 350, 'Choose a letter:')
    options = [('A', 'Av'), 'B', ('C', 'Cv'),
               ('D', 'Dv'), 'E', ('F',), ('G', 'Gv')]
    form.choice(name='choice1', tooltip='Field choice1',
                value='A',
                x=165, y=345, width=72, height=20,
                borderColor=magenta, fillColor=pink,
                textColor=blue, forceBorder=True, options=options)

    c.drawString(10, 300, 'Choose an animal:')
    options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
    form.choice(name='choice2', tooltip='Field choice2',
                value='Cat',
                options=options,
                x=165, y=295, width=72, height=20,
                borderStyle='solid', borderWidth=1,
                forceBorder=True)

    form.checkbox(name='cb1', tooltip='Field cb1',
                  x=110, y=245, buttonStyle='check',
                  borderColor=magenta, fillColor=pink,
                  textColor=blue, forceBorder=True)

    c.save()


if __name__ == '__main__':
    create_simple_form()
