class KnowledgeGraph:

    def __init__(self):
        self.triples = []

    def add_fact(self, subject, predicate, obj):
        self.triples.append(
            (subject, predicate, obj)
        )

    def query(self, subject=None,
              predicate=None,
              obj=None):

        results = []

        for s, p, o in self.triples:

            if subject is not None and s != subject:
                continue

            if predicate is not None and p != predicate:
                continue

            if obj is not None and o != obj:
                continue

            results.append((s, p, o))

        return results

    def display(self):

        print("\nKNOWLEDGE GRAPH\n")

        for s, p, o in self.triples:
            print(f"{s} --{p}--> {o}")