import os

def fileNameGen(name, filename, i):
    no = str(i)
    outName = ''

    ext = str(filename).split('.')[::-1]
    outName = str(name) + '-' + str(no) + '.' + str(ext[0])
    
    return outName


def rename():
    path = ''

    while True:
        try:
            path = input("Enter path you want to do bulk rename : ")
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

    while True:
        try:
            name = input("Enter a const name for your files : ")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            if (name != ' ' or name != ''): 
                break
            else:
                print("Error occurred: name can't be blank!")

            print('')

    list = os.listdir(path)
    a = 1

    for i in range(len(list)):
        if (list[i] != '.DS_Store'):
            filePath = os.path.join(path, list[i])
            outName = fileNameGen(name, list[i], a)
            fileOut = os.path.join(path, outName)

            os.rename(filePath, fileOut)
            a += 1

        if i == len(list) - 1:
            print('Finished!')
