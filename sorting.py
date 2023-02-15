import tkinter as tk
import random

class SortVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sorting Visualizer")
        self.num_elements = 50
        self.array = self.generate_array(self.num_elements)
        self.sort_algorithm = tk.StringVar(value="Bubble Sort")
        self.sorting = False
        self.pivot_element = None
        self.sorted_element = None
        self.delay_time = 10
        self.setup_gui()
        self.root.mainloop()

    # Define the generate_array method
    def generate_array(self, num_elements) -> list:
        array = []
        for i in range(num_elements):
            array.append(random.randint(10, 490))
        return array

    # Define the draw_array method which changes in size as the number of elements changes
    def draw_array(self, array) -> None:
        self.canvas.delete("all")
        for i in range(len(array)):
            x1 = i * 800 / (len(array) + 1)
            y1 = 500 - array[i]
            x2 = (i + 1) * 800 / (len(array) + 1)
            y2 = 500
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            if i == self.pivot_element:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        self.root.update()

    # Define the bubble_sort method
    def bubble_sort(self) -> None:
        n = len(self.array)
        for i in range(n):
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.pivot_element = j
                    self.draw_array(self.array)
                    self.root.update()
                    self.root.after(self.delay_time)
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array(self.array)
                    self.root.update()
                    self.root.after(self.delay_time)
                    self.pivot_element = None
            self.sorted_element = n - i - 1
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)

    # Define the selection_sort method
    def selection_sort(self) -> None:
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.pivot_element = i
            self.draw_array(self.array)
            self.root.update()
            self.root.after(10)
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)
            self.pivot_element = None
        self.sorted_element = n - i - 1
        self.draw_array(self.array)
        self.root.update()
        self.root.after(self.delay_time)

    def insertion_sort(self) -> None:
        # insertion sort method including the pivot element
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.pivot_element = j
                self.draw_array(self.array)
                self.root.update()
                self.root.after(self.delay_time)
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.pivot_element = None
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)
    
    
    def final_sort(self) -> None:
        '''
        This is just for the aesthetic of the program. It just looks fun to watch.
        '''
        for i in range(len(self.array)):
            self.pivot_element = i
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)
        self.pivot_element = None
        self.draw_array(self.array)
        self.root.update()
        self.root.after(self.delay_time)

    # Define the run_sorting method
    def run_sorting(self) -> None:
        if self.sort_algorithm.get() == "Bubble Sort":
            self.bubble_sort()
            self.final_sort()
        elif self.sort_algorithm.get() == "Selection Sort":
            self.selection_sort()
            self.final_sort()
        elif self.sort_algorithm.get() == "Insertion Sort":
            self.insertion_sort()
            self.final_sort()
        self.sorting = False
    
    # Define the handle_sort_button method
    def handle_sort_button(self) -> None:
        if not self.sorting:
            self.sorting = True
            self.run_sorting()

    # Define the setup_gui method
    def setup_gui(self) -> None:
        self.canvas = tk.Canvas(self.root, width=800, height=500, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.slider = tk.Scale(self.root, from_=3, to=500, resolution=1, orient=tk.HORIZONTAL, label="Number of elements", command=self.handle_slider, length=400)
        self.slider.grid(row=1, column=0)

        self.delay_slider = tk.Scale(self.root, from_=0, to=2.5, resolution=0.01, orient=tk.HORIZONTAL, label="Delay (s)", command=self.handle_delay_slider, length=200)
        self.delay_slider.grid(row=1, column=1)

        self.sort_options = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
        self.dropdown = tk.OptionMenu(self.root, self.sort_algorithm, *self.sort_options)
        self.dropdown.grid(row=1, column=2)

        self.sort_button = tk.Button(self.root, text="Sort", command=self.handle_sort_button)
        self.sort_button.grid(row=1, column=3)

        self.draw_array(self.array)

    # Define the handle_slider method
    def handle_slider(self, value) -> None:
        self.num_elements = int(value)
        if self.num_elements != len(self.array):
            self.array = self.generate_array(self.num_elements)
            self.draw_array(self.array)

    # Define the handle_delay_slider method
    def handle_delay_slider(self, value) -> None:
        self.delay_time = int(float(value) * 1000)