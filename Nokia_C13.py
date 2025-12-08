menu = """ 
   || NOKIA C13 || 
    1. Phone Book
    2. Messages
    3. Chat
    4. Call Register
    5. Tones
    6. Settings
    7. Call Divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM Services
  ------------------------- """
print(menu)
       
menuOption = int(input("Enter Option: "))
match menuOption: 
    case 1:
        menu = """ 
            -----Phone Book-----
        1. Search
        2. Service Nos.
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b'card
        8. Option
        9. Speed dials
        10. Voice tags
      ---------------------- """
        print(menu)
        menuOption = int(input("Enter Option: "))
        match menuOption: 
            case 1: 
                print("Search")
            case 2: 
                print("Service Nos.")
            case 3: 
                print("Add name")
            case 4: 
                print("Erase")
            case 5: 
                print("Edit")
            case 6: 
                print("Assign tone")
            case 7: 
                print("Send b'card")
            case 8: 
                menu = """
                        ----- OPTIONS ------
                            1. Type of views
                            2. Memory Status
                        --------------------"""
                print(menu)
                menuOption = int(input("Enter Option: "))
                match menuOption: 
                    case 1: 
                        print("Type of views")
                    case 2: 
                        print("Memory Status")
                
            case 9: 
                print("Speed dials")
            case 10:
                print("Voice tags")
                
    case 2: 
        menu = """ 
        -------- MESSAGES ------
        1. Write Message
        2. Inbox
        3. Outbox
        4. Picture Messages
        5. Template
        6. Smileys
        7. Messages settings
        8. Info Service
        9. Voice mailbox number
        10. Service command editor
        ------------------------------ """
        print(menu)
        menuOption = int(input("Enter Option: "))

        match menuOption: 
                case 1: 
                    print("Write message")
                case 2: 
                    print("Inbox")
                case 3: 
                    print("Outbox")
                case 4: 
                    print("Picture messages")
                case 5:
                    print("Template")
                case 6:
                    print("Smileys")
                case 7: 
                    menu = """ 

                        1. Set 1 
                        2. Common 3 

                       --------------"""
                    print(menu)
                  
                    menuOption = int(input("Enter Option: "))
                    
                    match menuOption: 
                        case 1: 
                            menu = """  
            
                                1. Message centre number
                                2. Messages sent as
                                3.Message validity  
                              _____________________ """; 
                            print(menu)
                            menuOptin = int(input("Enter Option "))
                            match menuOption: 
                                case 1: 
                                    print("Message centre number") 
                                case 2: 
                                    print("Messages sent as")
                                case 3: 
                                    print("Message validity")                      
                        case 2: 
                            menu = """ 
            
                                1. Delivery reports
                                2. Reply via same centre
                                3. Character support
                              _____________________ """; 
                            print(menu)
                            menuOptin = int(input("Enter Option "))
                            match menuOption: 
                                case 1: 
                                    print("Delivery reports") 
                                case 2: 
                                    print("Reply via same centre")
                                case 3: 
                                    print("Character Support")   
                        
                case 8: 
                    print("Info services")
                case 9: 
                    print("Voice mailbox number")
                case 10: 
                    print("Service command editor")   
    case 3:
        print("Chat")

    case 4: 
         menu = """ 
            -----Call Register------
            
            1. Missed calls
            2. Received calls
            3. Dialled numbers
            4. Erase recent call lists
            5. Show call duration. 
            6. Show call cost. 
            7. Call cost limit.
            8. prepaid credit. 
          --------------------------"""; 
         print(menu)
         menuOption = int(input("Enter Option: "))
         match menuOption: 
            case 1: 
                print("Missed calls")
            case 2: 
                print("Recieved calls")
            case 3: 
                print("Dailed numbers") 
            case 4: 
                print("Erase recent call lists")
            case 5: 
                menu = """

             -----Show call duration------ 
                1. Last call duration
                2. All calls’ duration
                3. Received calls’ duration
                4. Dialled calls’ duration
                5. Clear timers
            -------------------------------"""; 
                print(menu)
                menuOption = int(input("Enter Option: "))
                match menuOption: 
                    case 1: 
                        print("Last call duration")
                    case 2: 
                        print("All call's duration'")
                    case 3: 
                        print("Recieved calls' duration'")
                    case 4: 
                        print("Dailled calls' duration")
                    case 5: 
                        print("Clear timers")  

            case 6: 
                menu =""" 
             -------Show call costs------
                1. Last call cost
                2. All calls’ cost
                3. Clear counters 
            ----------------------------""";  

































