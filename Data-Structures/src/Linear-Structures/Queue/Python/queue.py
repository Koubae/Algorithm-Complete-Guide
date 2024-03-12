"""
    Queue Implementations in Python
    @Author: Federico Baù
    @Creation Date: 20 - Jan - 2021
    @Updated: N/a
    
"""

# ========================= < Queue > ========================= #

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)


# ========================= < Flavius Josephus' Problem > ========================= #
# Josephus Problem -> https://cp-algorithms.com/others/josephus_problem.html

def flavius_josephus(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


print(flavius_josephus(["Tim", "David", "Susan", "Federico", "Kent", "Brad"], 7))


# ========================= < Tasks -- Printer > ========================= #

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.wait_time(current_second))
            lab_printer.start_next(nexttask)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(
        f"Average Wait {average_wait:6.2f} secs" \
        + f"{print_queue.size():3d} tasks remaining."
    )


def new_print_task():
    num = random.randrange(1, 181)
    return num == 180


for i in range(10):
    simulation(3600, 5)

# Average Wait 165.38 secs 2 tasks remaining.
# Average Wait  95.07 secs 1 tasks remaining.
# Average Wait  65.05 secs 2 tasks remaining.
# Average Wait  99.74 secs 1 tasks remaining.
# Average Wait  17.27 secs 0 tasks remaining.
# Average Wait 239.61 secs 5 tasks remaining.
# Average Wait  75.11 secs 1 tasks remaining.
# Average Wait  48.33 secs 0 tasks remaining.
# Average Wait  39.31 secs 3 tasks remaining.
# Average Wait 376.05 secs 1 tasks remaining.