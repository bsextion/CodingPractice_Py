from abc import ABC, abstractmethod

class ResearchGuideline(ABC):

    # Template Method definition:
    def templateMethod(self):
        # Calling all the steps
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    # Defining the Template Method Steps
    def step1(self):
        pass

    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    def step4(self):
        pass


class UniversityA(ResearchGuideline):
    def step2(self):
        print("Step 2 - Applied by University A")

    def step3(self):
        print("Step 3 - Applied by University A")


class UniversityB(ResearchGuideline):
    def step1(self):
        print("Step 1 - Applied by University B")

    def step3(self):
        print("Step 3 - Applied by University B")

    def step4(self):
        print("Step 4 - Applied by University B")


def clinentCall(type: ResearchGuideline):
    type.templateMethod()


uni1 = UniversityA()
clinentCall(uni1)