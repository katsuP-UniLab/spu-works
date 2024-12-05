def Menu(rename, fileArrange):
  while True:
    print('1. Bulk Rename')
    print('2. File Arranger')
    print('0. Exit')
    
    while True:
        try:
            inp = int(input("Enter your choice : "))
        except ValueError:
            print("Enter a valid value!!")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
          if (inp == 1):
            rename()
          elif (inp == 2):
            fileArrange()
          elif (inp == 0):
            break
      
    print('Good bye!')
    break
    