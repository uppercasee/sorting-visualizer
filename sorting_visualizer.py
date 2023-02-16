import tkinter as tk
import random


class SortVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sorting Visualizer")
        self.num_elements = 25
        self.array = self.generate_array(self.num_elements)
        self.sort_algorithm = tk.StringVar(value="Bubble Sort")
        self.sorting = False
        self.pivot_element = None
        self.current_element = None
        self.lowest_element = None
        self.sorted_element = None
        self.delay_time = 50
        self.setup_gui()
        self.root.mainloop()

    def generate_array(self, num_elements) -> list:
        array = []
        for _ in range(num_elements):
            array.append(random.randint(10, 790))
        return array

    def draw_array(self, array) -> None:
        self.canvas.delete("all")
        for i in range(len(array)):
            x1 = i * 1000 / (len(array) + 1)
            y1 = 800 - array[i]
            x2 = (i + 1) * 1000 / (len(array) + 1)
            y2 = 800
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            if i == self.pivot_element:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#00FF00")
            if i == self.current_element:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FF0000")
            if i == self.lowest_element:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FF8C00")
        self.root.update()

    def bubble_sort(self) -> None:
        n = len(self.array)
        for i in range(n):
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.pivot_element = j
                    self.current_element = j + 1
                    self.draw_array(self.array)
                    self.root.update()
                    self.root.after(self.delay_time)
                    self.array[j], self.array[j +
                                              1] = self.array[j + 1], self.array[j]
                    self.draw_array(self.array)
                    self.root.update()
                    self.root.after(self.delay_time)
                    self.pivot_element = None
            self.current_element = None
            self.sorted_element = n - i - 1
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)

    def selection_sort(self) -> None:
        n = len(self.array)
        for i in range(n):
            self.pivot_element = i
            self.lowest_element = i
            for j in range(i + 1, n):
                self.current_element = j
                self.draw_array(self.array)
                self.root.update()
                self.root.after(self.delay_time)
                if self.array[j] < self.array[self.lowest_element]:
                    self.lowest_element = j
            self.array[i], self.array[self.lowest_element] = self.array[self.lowest_element], self.array[i]
            self.pivot_element = None
            self.lowest_element = None
            self.current_element = None
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)

    def insertion_sort(self) -> None:
        n = len(self.array)
        for i in range(1, n):
            self.pivot_element = i
            self.current_element = i
            for j in range(i-1, -1, -1):
                self.current_element = j + 1
                self.lowest_element = j
                self.draw_array(self.array)
                self.root.update()
                self.root.after(self.delay_time)
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j +
                                              1] = self.array[j+1], self.array[j]
                else:
                    break
            self.pivot_element = None
            self.current_element = None
            self.lowest_element = None
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)

    def merge_sort(self) -> None:
        pass

    def quick_sort(self) -> None:
        pass

    def heap_sort(self) -> None:
        pass

    def final_sort(self) -> None:
        """
        This is just for the aesthetic of the program. It just looks fun to watch.
        """
        self.delay_time = 30
        for i in range(len(self.array)):
            self.pivot_element = i
            self.draw_array(self.array)
            self.root.update()
            self.root.after(self.delay_time)
        self.pivot_element = None
        self.draw_array(self.array)
        self.root.update()
        self.root.after(self.delay_time)
        self.sorting = True

    def run_sorting(self) -> None:
        sorting_algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort,
        }
        sort_function = sorting_algorithms.get(self.sort_algorithm.get())
        if sort_function:
            sort_function()
            self.final_sort()
        self.sorting = False

    def handle_sort_button(self) -> None:
        if not self.sorting:
            self.sorting = True
            self.run_sorting()

    def setup_gui(self) -> None:
        self.canvas = tk.Canvas(self.root, width=1000, height=800, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=4)

        self.slider = tk.Scale(
            self.root,
            from_=3,
            to=500,
            resolution=1,
            orient=tk.HORIZONTAL,
            label="Number of elements",
            command=self.handle_slider,
            length=500,
        )
        self.slider.set(self.num_elements)
        self.slider.config(bg="#EAA222", fg="black",
                           highlightbackground="black")
        self.slider.grid(row=0, column=0)

        self.delay_slider = tk.Scale(
            self.root,
            from_=0,
            to=2.5,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            label="Delay (s)",
            command=self.handle_delay_slider,
            length=300,
        )
        self.delay_slider.set(self.delay_time / 1000)
        self.delay_slider.config(
            bg="#EAA222", fg="black", highlightbackground="black")
        self.delay_slider.grid(row=0, column=1)

        self.sort_options = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
        self.dropdown = tk.OptionMenu(
            self.root, self.sort_algorithm, *self.sort_options
        )
        self.dropdown.config(bg="yellow", fg="black",
                             highlightbackground="black")

        self.dropdown.grid(row=0, column=2)

        self.sort_button = tk.Button(
            self.root, text="Sort", command=self.handle_sort_button
        )
        self.sort_button.config(bg="#00FF00", fg="black",
                                highlightbackground="black")
        self.sort_button.grid(row=0, column=3)

        self.draw_array(self.array)

    def handle_slider(self, value) -> None:
        self.num_elements = int(value)
        if self.num_elements != len(self.array):
            self.array = self.generate_array(self.num_elements)
            self.draw_array(self.array)

    def handle_delay_slider(self, value) -> None:
        self.delay_time = int(float(value) * 1000)
