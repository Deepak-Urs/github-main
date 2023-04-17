def insertionSort(customList):
    for i in range(1, len(customList)): # O(n)
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]: # O(n)
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    
    print(customList)

customList = [2,1,7,6,5,3,4,9,8]
insertionSort(customList)

# Time Complexity -> O(n^2)
# Space Complexity -> O(1)