import os

def fileArrange():
    while True:
        try:
            path = input("Enter path you want to arrange your files : ")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            if (path != ' ' or path != ''): 
                if os.path.exists(path):
                    break
                else:
                    print("Error occurred: Path should be exist!")
            else:
                print("Error occurred: Path can't be blank!")

            print('')

    list = os.listdir(path)
    
    for file in list:
      ext = file.split('.')[::-1][0]
      outPath = os.path.join(path, ext)
      
      if os.path.exists(outPath) != True:
        os.makedirs(outPath)
        
      os.rename(os.path.join(path, file), os.path.join(outPath, file))
      
      if file == list[len(list) - 1]:
        print('Arranging file successfully')
