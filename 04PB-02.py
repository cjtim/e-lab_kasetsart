print("---<< Main Menu >>---")
print('    <B>urger Meal')
print('    <C>hicken Meal')
print('    <P>asta Meal')
MainMenu = input('Enter your choice: ')
if MainMenu == 'B' or MainMenu == 'b':
    print('---<< Burger Sub Menu >>---')
    print('    <R>egular Burger')
    print('    <C>heese Burger')
    print('    <D>ouble Cheese Burger')    
    SubMenu = input('Enter your choice: ')
    if SubMenu == 'R' or SubMenu == 'r':
        FinalMenu = 'Regular Burger'
        xx = 60
        print('Your',FinalMenu,'is',xx,'Baht.')
    elif SubMenu == 'C' or SubMenu == 'c':
        FinalMenu = 'Cheese Burger'
        xx = 75
        print('Your',FinalMenu,'is',xx,'Baht.')
    elif SubMenu == 'D' or SubMenu == 'd':
        FinalMenu = 'Double Cheese Burger'
        xx = 90
        print('Your',FinalMenu,'is',xx,'Baht.')
    else:
        print('Invalid sub menu choice.')    
elif MainMenu == 'C' or MainMenu == 'c':
    print('---<< Chicken Sub Menu >>---')
    print('    <F>ried Chicken')
    print('    <G>rilled Chicken')
    print('    <C>hef\'s Chicken')    
    SubMenu = input('Enter your choice: ')
    if SubMenu == 'F' or SubMenu == 'f':
        FinalMenu = 'Fried Chicken'
        xx = 120
        print('Your',FinalMenu,'is',xx,'Baht.')
    elif SubMenu == 'G' or SubMenu == 'g':
        FinalMenu = 'Grilled Chicken'
        xx = 150
        print('Your',FinalMenu,'is',xx,'Baht.')
    elif SubMenu == 'C' or SubMenu == 'c':
        FinalMenu = 'Chef\'s Chicken'
        xx = 180
        print('Your',FinalMenu,'is',xx,'Baht.')
    else:
        print('Invalid sub menu choice.')    
elif MainMenu == 'P' or MainMenu == 'p':
    print('---<< Pasta Sub Menu >>---')
    print('    <S>paghetti de Italiano')
    print('    <L>asagna Supreme')
    print('    <M>acaroni Special')       
    SubMenu = input('Enter your choice: ')
    if SubMenu == 'S' or SubMenu == 's':
        FinalMenu = 'Spaghetti de Italiano'
        xx = 90
        print('Your',FinalMenu,'is',xx,'Baht.')
    elif SubMenu == 'L' or SubMenu == 'l':
        FinalMenu = 'Lasagna Supreme'
        xx = 120
        print('Your',FinalMenu,'is',xx,'Baht.')
    elif SubMenu == 'M' or SubMenu == 'm':
        FinalMenu = 'Macaroni Special'
        xx = 100
        print('Your',FinalMenu,'is',xx,'Baht.')
    else:
        print('Invalid sub menu choice.')
else:
    print('Invalid main menu choice.')