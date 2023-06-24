#Junaid 
#Quick And Merge Sort
#PYTHON Developer


def mergeSort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr)//2 #floor division operator using for return round of value of division 
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
                                    #[1,4,5,7,9,2]
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    print("Sorted array is: ")
    for i in range(n):
        arr1[i]=arr1[i]
    print(arr1)
def partition(arr1, low, high):
    i = (low-1) # index of smaller element
    pivot = arr1[high] # pivot

    for j in range(low, high):
        if arr1[j] <= pivot:
            i = i+1
            arr1[i], arr1[j] = arr1[j], arr1[i]

    arr1[i+1], arr1[high] = arr1[high], arr1[i+1]
    return (i+1)
def quickSort(arr1, low, high):
    if len(arr1) == 1:
        return arr
    if low < high:
        pi = partition(arr1, low, high)
        quickSort(arr1, low, pi-1)
        quickSort(arr1, pi+1, high)
def printq(arr1):
    print("Sorted array is: ")
    for i in range(n):
        arr1[i]=arr1[i]
    print(arr1)

    
if __name__ == "_main_":
    print("Press 1 for Time Complexity of Quick Sort")
    print("Press 2 for Time Complexity of Merge Sort")
    print("Press 3 for Merge Sort")
    print("Press 4 for Quick Sort")
    print("Press 5 for Exit \n ")
    
    while(True):
        check = int(input("Enter 1 for Continue 2 for end"))
        if check == 1:                    
            arr = [1,2,3,4]

        #     a=int(input("Number of elements in the array:-"))
        #     n=list(map(int, input("elements of array:-").strip().split()))

        #     arr = n
            arr1=[]
            

            print("---------------------------")
            n1 = int(input("Enter Number"))
            if n1==1:
                arr2=[1,2,3,4]  
                print("In Quick Sort Best And Average Time Complexity is Same O(nlogn)")
                print("Worst ComPlexity Is O(n^2)")
                print("---------------------------")

                for i in range (len(arr2)-1):
                    if arr2[0]<arr2[i+1] and (len(arr2))>arr2[i-1]:
                        z="Worst Case"
                        print("---------------------------")

                    elif arr2[0]>arr2[i+1] and (len(arr2))<arr2[i-1]:
                        z="Best Case/Average Case"
                        print("---------------------------")

                print(z)
            elif n1==2:
                print("In Merge Sort Best,Worst And Average Time Complexity is Same O(nlogn)")
            elif n1 == 3 or 4:
                n = int(input("Please Enter a Total u Want to sort:\n"))
                print("---------------------------")
                for i in range(n):
                    r = int(input("Enter Number"))
                    arr1.append(r)
                print("Given array is", end="\n")
                print(arr1)
                print("---------------------------")

                if n1==3:
                    print("Merge Sort")

                    mergeSort(arr1)
                    print("Sorted array is: ", end="\n")
                    printList(arr1)    
                elif n1==4:
                    print("Quick Sort")
                    quickSort(arr1, 0, n-1)
                    printq(arr1)
                print("---------------------------")
        elif check == 2:
            break
        
        else:
            print("Enter Correct Key");