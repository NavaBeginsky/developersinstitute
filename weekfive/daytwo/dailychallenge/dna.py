import random


class Genes():
    def __init__(self):
        self.value = random.randrange(0, 2)

    def mutate(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value == 0


class Chromosomes():
    def __init__(self):
        self.gene_sequence = [Genes() for index in range(10)]

    def mutate(self):
        for gene in self.gene_sequence:
            if choose_whether_to_mutate():
                gene.mutate()


class DNA():
    def __init__(self):
        self.chromosome_sequence = [Chromosomes() for index in range(10)]

    def mutate(self):
        for chrom in self.chromosome_sequence:
            if choose_whether_to_mutate():
                chrom.mutate()


def choose_whether_to_mutate(mutation_probability=0.5):
    num = random.random()
    if num < mutation_probability:
        return True


class Organism(DNA):
    def __init__(self, mutation_probability):
        DNA.__init__(self)
        self.mutation_probability = mutation_probability

    def mutate(self):
        if choose_whether_to_mutate(self.mutation_probability):
            super().mutate()

    def count_mutations(self):
        value = []
        mutation_count = 0
        while True:
            for chrosome in self.chromosome_sequence:
                for gene in chrosome.gene_sequence:
                    value.append(gene.value)
            if len(set(value)) == 1 and 1 in set(value):
                break
            else:
                self.mutate()
                mutation_count += 1
                value = []
        return mutation_count


organism_1 = Organism(0.5)
organism_2 = Organism(0.2)
organism_3 = Organism(0.8)

print(organism_1.count_mutations())
print(organism_2.count_mutations())
print(organism_3.count_mutations())
