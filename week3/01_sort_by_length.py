def sort_by_length(names:list)->None:
    names_length:int=len(names)

    for i in range(names_length):
        swapped = False

        for j in range(0,names_length - i - 1):

            if len(names[j])>len(names[j+1]):
                names[j],names[j+1]=names[j+1],names[j]
                swapped = True

        if not swapped:
            break
# TODO: capatal by index

def capetal_by_index(names:list)->None:
    for i in range(len(names)):
        if len(names[i])-1<i:
            names[i]=names[i].lower()
            continue
        # print(i)
        names[i]=str(names[i][0:i]).lower()+names[i][i].upper()+str(names[i][i+1:]).lower()
    


def main():
    names:list = ["ANiket", "HAripreetam", "Ram", "Vishal", "Wagh", "Rahul"]
    # sort_by_length(names=names)
    capetal_by_index(names=names)
    print(names)  
   

if __name__ == "__main__":
    main()
