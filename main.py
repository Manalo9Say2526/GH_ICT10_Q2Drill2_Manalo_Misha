from pyscript import display, document  # type: ignore

def club_name(e):
    document.getElementById('output').InnerHTML = ' ' 
    first_name = document.getElementById('firstname').value.title()
    last_name = document.getElementById('lastname').value.title()
    full_name = first_name + " " + last_name
    
    volleyball_members = [
        'Elise Lim', 
        'Adri Allas', 
        'Kaitlyn Nardo', 
        'Jasmine Kaur', 
        'Samantha Rebadulla', 
        'Mark Gervacio' 
    ]

    member_checker = full_name in volleyball_members

    display_message = (f'Sorry, {full_name} is not included in the club', f'{full_name} is included in the club')
    
    display(display_message[member_checker], target='output')