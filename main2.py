#FOR TEAM_CHECKER.HTML 

from pyscript import display, document


def intrams_checker(e):

 #REGISTRATION
    registration_input = document.querySelector('input[name="registration"]:checked')
    if registration_input is None:
        display("Please select if you have registered online.", target='output')
        return
    registration = registration_input.value
    # resulted in several errors when no option was selected so here we are 
    # shows up when no registration input is selected 
    

    #CLEARANCE 
    clearance_input = document.querySelector('input[name="clearance"]:checked')
    if clearance_input is None:
        display("Please select your medical clearance status.", target='output')
        return
    clearance = clearance_input.value
    #shows up when no clearance option is selected 



    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display(f'Whoops! Looks like you did not register! Ask your PE teacher regarding the online registraton.', target='output')
    elif clearance != 'cleared':
        display(f'Oh no! You need a medical clearance to join. Go to your campus clinic and secure your clearance.', target='output')
    elif section == 'emerald':
        display(f"LET'S GO BLUE BEARS !!!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/blue bears.jpg" alt="Blue Bears" style="max-width:200px;">'


    elif section == 'ruby':
        display(f"BOOM! GO RED BULLDOGS!!!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/red bulldogs.jpg" alt="Red Bulldogs" style="max-width:200px;">'


    elif section == 'sapphire':
        display(f"RISE UP! YELLOW TIGERS!!!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/yellow tigers.jpg" alt="Yellow Tigers" style="max-width:200px;">'


    else: 
        display(f"FIGHT STRONG! GO GREEN HORNETS!", target='output')
        document.getElementById("image").innerHTML = '<img src="images/green hornets.jpg" alt="Green Hornets" style="max-width:200px;">'
