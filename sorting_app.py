import streamlit as st

# Sorting algorithms
def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps

def selection_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

def merge_sort(arr, steps):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, steps)
        merge_sort(R, steps)

        i = j = k = 0
        while i < len(L) and j < len(R):
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

        steps.append(arr.copy())
    return steps

def quick_sort(arr, low, high, steps):
    if low < high:
        pi = partition(arr, low, high, steps)
        quick_sort(arr, low, pi - 1, steps)
        quick_sort(arr, pi + 1, high, steps)
    return steps

def partition(arr, low, high, steps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps.append(arr.copy())
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append(arr.copy())
    return i + 1

# Streamlit UI
st.title("Sorting Algorithms Visualizer | PAOLO PACALDO")
st.write("Enter a list of integers to see sorting in action!")

# Input array
input_data = st.text_input("Enter numbers separated by commas (e.g., 5,2,9,1,5,6):")
if input_data:
    try:
        array = list(map(int, input_data.split(',')))
        st.write(f"Original Array: {array}")

        # Choose sorting algorithm
        algo = st.selectbox("Choose a sorting algorithm:", 
                            ["Bubble Sort", "Selection Sort", "Merge Sort", "Quick Sort"])

        if st.button("Sort and Show Solution"):
            steps = []
            if algo == "Bubble Sort":
                steps = bubble_sort(array.copy())
            elif algo == "Selection Sort":
                steps = selection_sort(array.copy())
            elif algo == "Merge Sort":
                steps = merge_sort(array.copy(), steps)
            elif algo == "Quick Sort":
                quick_sort(array.copy(), 0, len(array) - 1, steps)

            st.write("Sorted Array:", steps[-1])
            st.write("Steps to Sort:")
            for i, step in enumerate(steps):
                st.write(f"Step {i + 1}: {step}")
    except ValueError:
        st.error("Please enter a valid list of integers.")
