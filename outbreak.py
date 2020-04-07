from random import random, choice

class Simulation:
    def __init__(self, n=12000, infected=10):
        """
        Instantiates a simulation

        >>> sim = Simulation(n=6000, infected=6)
        >>> len(sim.people)
        6000

        >>> sim.count_infected()
        6
        """

        self.people = [Person() for _ in range(n)]

        for i in range(infected):
            self.people[i].contract()

    def count_infected(self):
        return len([p for p in self.people if p.infected])

    def run_step(self):
        for person in self.people:
            if person.infected:
                for _ in range(30):
                    choice(self.people).expose()

                person.update()

    def run(self):
        while self.count_infected() > 0:
            self.run_step()
            self.print_state()

    def print_state(self):
        print(f"{self.count_infected()}")
    
class Person:
    def __init__(self):
        self.infected = False
        self.recovered = False
        self.deceased = False

    def recover(self):
        self.recovered = True
        self.infected = False

    def succomb(self):
        self.deceased = True
        self.infected = False

    def contract(self):
        self.infected = True

    def expose(self):
        if not self.recovered and random() < .03:
            self.contract()

    def update(self):
        if self.infected and random() < .10:
            self.recover()

if __name__ == '__main__':
    sim = Simulation(n=12000, infected=10)
    sim.run()
