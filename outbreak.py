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

    def count_deceased(self):
        return len([p for p in self.people if p.deceased])

    def count_recovered(self):
        return len([p for p in self.people if p.recovered])

    def run_step(self):
        for person in self.people:
            if person.infected:
                for _ in range(30):
                    choice(self.people).expose()

                person.update()

    def run(self):
        day = 1
    
        while self.count_infected() > 0:
            self.run_step()
            self.print_state(day)
            day += 1

    def print_state(self, day):
        print(f"Day {day:<5}"
              f"    Infected: {self.count_infected():<7}"
              f"    Recovered: {self.count_recovered():<7}"
              f"    Deceased: {self.count_deceased():<7}")
    
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
        if self.infected:
            if random() < .10:
                self.recover()
            elif random() < .01:
                self.succomb()

if __name__ == '__main__':
    sim = Simulation(n=6000, infected=10)
    sim.run()
